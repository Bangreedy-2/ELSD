import React, { useMemo, useState } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Grid, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface GCodeVisualizerProps {
  gcode: string;
}

interface Segment {
  points: THREE.Vector3[];
  type: 'G0' | 'G1';
  layerZ: number;
}

interface Bounds {
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
}

interface ParsedGCode {
  segments: Segment[];
  pausedZs: Set<number>;
  layerBounds: Map<number, Bounds>;
  globalBounds: Bounds;
}

// Colors
const COLOR_TRAVEL = '#6b7280';      // G0 rapid
const COLOR_EXTRUDE = '#6366f1';     // G1 print move
const COLOR_PAUSED_EXTRUDE = '#f59e0b'; // highlighted paused layer
const COLOR_PAUSED_TRAVEL = '#fbbf24';
const COLOR_PAUSE_SURFACE = '#22c55e';  // pause-layer surface (checkmark green)

function parseGCode(gcode: string): ParsedGCode {
  const lines = gcode.split('\n');
  const segments: Segment[] = [];
  const pausedZs = new Set<number>();
  const layerBounds = new Map<number, Bounds>();
  const globalBounds: Bounds = { minX: Infinity, maxX: -Infinity, minY: Infinity, maxY: -Infinity };

  const currentPos = new THREE.Vector3(0, 0, 0);
  let currentSegment: THREE.Vector3[] = [currentPos.clone()];
  let lastCommand: 'G0' | 'G1' | '' = '';
  // Layer height is tracked from layer-marker comments (preferred) and Z moves.
  let currentLayerZ = 0;

  const extendBounds = (z: number, x: number, y: number) => {
    let b = layerBounds.get(z);
    if (!b) { b = { minX: x, maxX: x, minY: y, maxY: y }; layerBounds.set(z, b); }
    else {
      b.minX = Math.min(b.minX, x); b.maxX = Math.max(b.maxX, x);
      b.minY = Math.min(b.minY, y); b.maxY = Math.max(b.maxY, y);
    }
    globalBounds.minX = Math.min(globalBounds.minX, x);
    globalBounds.maxX = Math.max(globalBounds.maxX, x);
    globalBounds.minY = Math.min(globalBounds.minY, y);
    globalBounds.maxY = Math.max(globalBounds.maxY, y);
  };

  const flush = () => {
    if (currentSegment.length > 1 && (lastCommand === 'G0' || lastCommand === 'G1')) {
      segments.push({ points: currentSegment, type: lastCommand, layerZ: currentLayerZ });
    }
  };

  lines.forEach(line => {
    const trimmed = line.trim();

    // Layer markers set the active layer height: "; layer 5, Z = 1.100"
    let m = trimmed.match(/^;\s*layer\s+\d+\s*,\s*z\s*=\s*([-\d.]+)/i);
    if (m) { currentLayerZ = parseFloat(m[1]); return; }
    // Friendly / DSL annotations: "; >> Layer 5 (Z=1.100mm)" or "; === Layer 5 (Z=1.100mm..."
    m = trimmed.match(/Layer\s+\d+\s*\(Z=([-\d.]+)mm/i);
    if (m) { currentLayerZ = parseFloat(m[1]); return; }

    // Pause detection (PAUSE comment precedes the M0). Stops emit "; STOP" and are
    // intentionally not treated as pauses.
    if (/^;\s*PAUSE\b/i.test(trimmed)) {
      pausedZs.add(currentLayerZ);
      return;
    }

    const parts = trimmed.split(/\s+/);
    const command = parts[0];
    if (command === 'G0' || command === 'G1') {
      if (command !== lastCommand && currentSegment.length > 1) {
        flush();
        currentSegment = [currentPos.clone()];
      }

      const xMatch = line.match(/X([-+]?[0-9]*\.?[0-9]+)/);
      const yMatch = line.match(/Y([-+]?[0-9]*\.?[0-9]+)/);
      const zMatch = line.match(/Z([-+]?[0-9]*\.?[0-9]+)/);

      if (xMatch) currentPos.x = parseFloat(xMatch[1]);
      if (yMatch) currentPos.y = parseFloat(yMatch[1]);
      if (zMatch) { currentPos.z = parseFloat(zMatch[1]); currentLayerZ = currentPos.z; }

      currentSegment.push(currentPos.clone());
      extendBounds(currentLayerZ, currentPos.x, currentPos.y);
      lastCommand = command;
    }
  });

  flush();
  return { segments, pausedZs, layerBounds, globalBounds };
}

const PathRenderer = ({
  segments,
  pausedZs,
  highlightPauses,
}: {
  segments: Segment[];
  pausedZs: Set<number>;
  highlightPauses: boolean;
}) => {
  return (
    <>
      {segments.map((seg, i) => {
        const isPaused = highlightPauses && pausedZs.has(seg.layerZ);
        const color = isPaused
          ? (seg.type === 'G0' ? COLOR_PAUSED_TRAVEL : COLOR_PAUSED_EXTRUDE)
          : (seg.type === 'G0' ? COLOR_TRAVEL : COLOR_EXTRUDE);
        const isTravel = seg.type === 'G0';
        return (
          <line key={i}>
            <bufferGeometry attach="geometry">
              <bufferAttribute
                attach="attributes-position"
                args={[new Float32Array(seg.points.flatMap(p => [p.x, p.z, -p.y])), 3]}
                count={seg.points.length}
                itemSize={3}
              />
            </bufferGeometry>
            <lineBasicMaterial
              attach="material"
              color={color}
              linewidth={2}
              transparent={isTravel && !isPaused}
              opacity={isTravel && !isPaused ? 0.4 : 1}
            />
          </line>
        );
      })}
    </>
  );
};

const PAUSE_SURFACE_PADDING = 3; // mm of overhang beyond the layer's print area

const PauseSurfaces = ({
  pausedZs,
  layerBounds,
  globalBounds,
}: {
  pausedZs: Set<number>;
  layerBounds: Map<number, Bounds>;
  globalBounds: Bounds;
}) => {
  return (
    <>
      {Array.from(pausedZs).map((z, i) => {
        // Use the paused layer's own XY extent; fall back to the whole-model
        // extent if that layer recorded no moves of its own.
        const b = layerBounds.get(z) ?? globalBounds;
        if (!isFinite(b.minX) || !isFinite(b.minY)) return null;
        const w = (b.maxX - b.minX) + PAUSE_SURFACE_PADDING * 2;
        const h = (b.maxY - b.minY) + PAUSE_SURFACE_PADDING * 2;
        const cx = (b.minX + b.maxX) / 2;
        const cy = (b.minY + b.maxY) / 2;
        // Path render space is [x, z, -y]; a horizontal layer is the world XZ
        // plane at height y = z, so lay the plane flat (rotate -90deg about X).
        return (
          <mesh key={i} position={[cx, z, -cy]} rotation={[-Math.PI / 2, 0, 0]}>
            <planeGeometry args={[Math.max(w, 1), Math.max(h, 1)]} />
            <meshStandardMaterial
              color={COLOR_PAUSE_SURFACE}
              emissive={COLOR_PAUSE_SURFACE}
              emissiveIntensity={0.25}
              transparent
              opacity={0.28}
              side={THREE.DoubleSide}
              depthWrite={false}
            />
          </mesh>
        );
      })}
    </>
  );
};

export const GCodeVisualizer: React.FC<GCodeVisualizerProps> = ({ gcode }) => {
  const [highlightPauses, setHighlightPauses] = useState(true);
  const { segments, pausedZs, layerBounds, globalBounds } = useMemo(() => parseGCode(gcode), [gcode]);
  const pauseCount = pausedZs.size;
  const hasPauses = pauseCount > 0;

  return (
    <div style={{ width: '100%', height: '100%', background: '#050505' }}>
      <Canvas shadows>
        <PerspectiveCamera makeDefault position={[50, 50, 50]} />
        <OrbitControls makeDefault />
        <ambientLight intensity={0.5} />
        <pointLight position={[100, 100, 100]} intensity={1} />

        <Grid
          infiniteGrid
          fadeDistance={100}
          sectionSize={10}
          sectionColor="#333"
          cellColor="#111"
        />

        <axesHelper args={[20]} />

        <React.Suspense fallback={null}>
          <PathRenderer segments={segments} pausedZs={pausedZs} highlightPauses={highlightPauses} />
          {highlightPauses && (
            <PauseSurfaces pausedZs={pausedZs} layerBounds={layerBounds} globalBounds={globalBounds} />
          )}
        </React.Suspense>
      </Canvas>

      {/* Pause highlight toggle */}
      <label
        style={{
          position: 'absolute',
          top: 15,
          right: 15,
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.4rem 0.75rem',
          borderRadius: '8px',
          background: 'rgba(15,15,18,0.8)',
          border: '1px solid rgba(255,255,255,0.1)',
          color: hasPauses ? '#e5e7eb' : 'rgba(255,255,255,0.35)',
          fontSize: '0.75rem',
          fontWeight: 600,
          cursor: hasPauses ? 'pointer' : 'default',
          userSelect: 'none',
        }}
      >
        <input
          type="checkbox"
          checked={highlightPauses}
          disabled={!hasPauses}
          onChange={(e) => setHighlightPauses(e.target.checked)}
          style={{ accentColor: COLOR_PAUSE_SURFACE, cursor: hasPauses ? 'pointer' : 'default' }}
        />
        <span style={{ color: COLOR_PAUSE_SURFACE }}>✓</span>
        Highlight pauses{hasPauses ? ` (${pauseCount})` : ' (none)'}
      </label>

      <div style={{ position: 'absolute', bottom: 10, right: 10, color: '#666', fontSize: '0.7rem' }}>
        3D PREVIEW | INTERACTIVE
      </div>
    </div>
  );
};
