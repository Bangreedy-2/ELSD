import React, { useRef, useMemo } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Grid, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface GCodeVisualizerProps {
  gcode: string;
}

const PathRenderer = ({ gcode }: { gcode: string }) => {
  const segments = useMemo(() => {
    const lines = gcode.split('\n');
    const segments: { points: THREE.Vector3[], color: string }[] = [];
    let currentPos = new THREE.Vector3(0, 0, 0);
    let currentSegment: THREE.Vector3[] = [currentPos.clone()];
    let lastCommand = '';

    lines.forEach(line => {
      const parts = line.trim().split(' ');
      const command = parts[0];
      
      if (command === 'G0' || command === 'G1') {
        if (command !== lastCommand && currentSegment.length > 1) {
          segments.push({ 
            points: currentSegment, 
            color: lastCommand === 'G0' ? '#6b7280' : '#6366f1' 
          });
          currentSegment = [currentPos.clone()];
        }

        const xMatch = line.match(/X([-+]?[0-9]*\.?[0-9]+)/);
        const yMatch = line.match(/Y([-+]?[0-9]*\.?[0-9]+)/);
        const zMatch = line.match(/Z([-+]?[0-9]*\.?[0-9]+)/);

        if (xMatch) currentPos.x = parseFloat(xMatch[1]);
        if (yMatch) currentPos.y = parseFloat(yMatch[1]);
        if (zMatch) currentPos.z = parseFloat(zMatch[1]);

        currentSegment.push(currentPos.clone());
        lastCommand = command;
      }
    });

    if (currentSegment.length > 1) {
      segments.push({ 
        points: currentSegment, 
        color: lastCommand === 'G0' ? '#6b7280' : '#6366f1' 
      });
    }

    return segments;
  }, [gcode]);

  return (
    <>
      {segments.map((seg, i) => (
        <line key={i}>
          <bufferGeometry attach="geometry">
            <bufferAttribute
              attach="attributes-position"
              count={seg.points.length}
              array={new Float32Array(seg.points.flatMap(p => [p.x, p.z, -p.y]))}
              itemSize={3}
            />
          </bufferGeometry>
          <lineBasicMaterial 
            attach="material" 
            color={seg.color} 
            linewidth={2} 
            transparent={seg.color === '#6b7280'} 
            opacity={seg.color === '#6b7280' ? 0.4 : 1}
          />
        </line>
      ))}
    </>
  );
};

export const GCodeVisualizer: React.FC<GCodeVisualizerProps> = ({ gcode }) => {
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
          <PathRenderer gcode={gcode} />
        </React.Suspense>
      </Canvas>
      <div style={{ position: 'absolute', bottom: 10, right: 10, color: '#666', fontSize: '0.7rem' }}>
        3D PREVIEW | INTERACTIVE
      </div>
    </div>
  );
};
