import React, { useState, useEffect } from 'react';
import Editor from '@monaco-editor/react';
import { 
  Play, 
  Upload, 
  Download, 
  FileCode, 
  Box, 
  AlertCircle, 
  CheckCircle,
  Cpu,
  Settings,
  Layers,
  Terminal
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import { GCodeVisualizer } from './components/GCodeVisualizer';

const API_BASE = 'http://localhost:8000';

function App() {
  const [code, setCode] = useState<string>(`Temperature 200C
Wait for 1 minutes
Set speed to 1000

Move to X10 Y10

Repeat 3 times {
    Move to X15 Y15
    Move to X20 Y10
}
`);
  const [gcode, setGcode] = useState<string>('');
  const [logs, setLogs] = useState<{type: 'info' | 'error' | 'success', message: string}[]>([]);
  const [isCompiling, setIsCompiling] = useState(false);
  const [activeFile, setActiveFile] = useState('example.gg');

  const addLog = (type: 'info' | 'error' | 'success', message: string) => {
    setLogs(prev => [...prev, { type, message }]);
  };

  const handleCompile = async () => {
    setIsCompiling(true);
    addLog('info', 'Compiling GGCode to G-code...');
    try {
      const response = await axios.post(`${API_BASE}/compile`, { code });
      setGcode(response.data.gcode);
      addLog('success', 'Compilation successful!');
    } catch (error: any) {
      const detail = error.response?.data?.detail || error.message;
      addLog('error', `Compilation failed: ${detail}`);
    } finally {
      setIsCompiling(false);
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${API_BASE}/upload`, formData);
      setCode(response.data.content);
      setActiveFile(response.data.filename);
      addLog('info', `Loaded file: ${response.data.filename}`);
    } catch (error: any) {
      addLog('error', `Upload failed: ${error.message}`);
    }
  };

  const handleDownload = () => {
    if (!gcode) return;
    const blob = new Blob([gcode], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'output.gcode';
    a.click();
    addLog('success', 'G-code downloaded.');
  };

  const handleEditorWillMount = (monaco: any) => {
    monaco.languages.register({ id: 'ggcode' });
    monaco.languages.setMonarchTokensProvider('ggcode', {
      tokenizer: {
        root: [
          [/\b(STOP|PAUSE|AT|LAYER|TEMPERATURE|MOVE|TO|ADD|SQUARE|CENTER|LENGTH|WIDTH|RECTANGLE|CIRCLE|RADIUS|LINE|FROM|BASE|CENTER_POINT|ORIGIN|SET|DEFINE|AS|REPEAT|TIMES|IF|THEN|ELSE|WHILE|WAIT|FOR|SECONDS|MINUTES|USE|HOME)\b/i, 'keyword'],
          [/[{}()\[\]]/, 'delimiter'],
          [/[<>!=]=?/, 'operator'],
          [/\b\d+\b/, 'number'],
          [/\b\d+C\b/i, 'number.temperature'],
          [/\b[XYZxyzEe]-?\d+(\.\d+)?\b/, 'attribute.value'],
          [/\/\/.*/, 'comment'],
          [/\/\*.*\*\//, 'comment'],
          [/[a-zA-Z_][a-zA-Z0-9_]*/, 'identifier'],
        ]
      }
    });

    monaco.editor.defineTheme('ggcode-theme', {
      base: 'vs-dark',
      inherit: true,
      rules: [
        { token: 'keyword', foreground: '6366f1', fontStyle: 'bold' },
        { token: 'number', foreground: 'fbbf24' },
        { token: 'number.temperature', foreground: 'f87171' },
        { token: 'attribute.value', foreground: '34d399' },
        { token: 'comment', foreground: '6b7280' },
      ],
      colors: {
        'editor.background': '#0f0f12',
      }
    });
  };

  return (
    <div className="app-container">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="logo">
          <Cpu size={28} />
          <span>GREATER G-CODE</span>
        </div>

        <div className="section-title">Files</div>
        <div className="file-list">
          <div className={`file-item ${activeFile === 'example.gg' ? 'active' : ''}`} onClick={() => setActiveFile('example.gg')}>
            <FileCode size={18} />
            <span>example.gg</span>
          </div>
          <label className="file-item" style={{ cursor: 'pointer' }}>
            <Upload size={18} />
            <span>Upload .gg</span>
            <input type="file" hidden onChange={handleFileUpload} accept=".gg,.gcode" />
          </label>
        </div>

        <div className="section-title">Actions</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
          <button onClick={handleCompile} disabled={isCompiling}>
            <Play size={18} fill={isCompiling ? 'none' : 'currentColor'} />
            {isCompiling ? 'Compiling...' : 'Run Pipeline'}
          </button>
          <button className="secondary" onClick={handleDownload} disabled={!gcode}>
            <Download size={18} />
            Export G-code
          </button>
          <button className="secondary">
            <Settings size={18} />
            Settings
          </button>
        </div>

        <div style={{ marginTop: 'auto' }}>
          <div className="glass-card" style={{ fontSize: '0.8rem', opacity: 0.8 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
              <Layers size={14} />
              <span>Pipeline Status</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span>Backend</span>
              <span style={{ color: '#10b981' }}>Connected</span>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        <header className="toolbar">
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <span style={{ color: 'rgba(255,255,255,0.5)', fontSize: '0.9rem' }}>Project /</span>
            <span style={{ fontWeight: 600 }}>{activeFile}</span>
          </div>
          <div style={{ marginLeft: 'auto', display: 'flex', gap: '1rem' }}>
             <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.8rem', color: 'rgba(255,255,255,0.5)' }}>
               <Terminal size={14} />
               <span>DSL Mode</span>
             </div>
          </div>
        </header>

        <section className="editor-section">
          <Editor
            height="100%"
            language="ggcode"
            theme="ggcode-theme"
            beforeMount={handleEditorWillMount}
            value={code}
            onChange={(val) => setCode(val || '')}
            options={{
              fontSize: 14,
              fontFamily: "'Fira Code', monospace",
              minimap: { enabled: false },
              padding: { top: 20 },
              smoothScrolling: true,
              cursorBlinking: "smooth",
            }}
          />
        </section>

        <section className="preview-section">
          <div style={{ position: 'absolute', top: 15, left: 15, zIndex: 1, pointerEvents: 'none' }}>
            <div className="glass-card" style={{ padding: '0.5rem 1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Box size={16} color="#6366f1" />
              <span style={{ fontWeight: 600, fontSize: '0.8rem' }}>3D VIEWPORT</span>
            </div>
          </div>
          <GCodeVisualizer gcode={gcode} />
        </section>

        <footer style={{ height: '150px', background: '#0a0a0c', borderTop: '1px solid var(--border-color)', display: 'flex' }}>
          <div style={{ width: '100%', display: 'flex', flexDirection: 'column' }}>
            <div className="toolbar" style={{ padding: '0.5rem 1rem', borderBottom: 'none' }}>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'rgba(255,255,255,0.3)' }}>OUTPUT & CONSOLE</span>
            </div>
            <div className="output-panel">
              <AnimatePresence>
                {logs.map((log, i) => (
                  <motion.div 
                    key={i}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    className={log.type === 'error' ? 'error-msg' : log.type === 'success' ? 'success-msg' : ''}
                    style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}
                  >
                    {log.type === 'error' && <AlertCircle size={14} />}
                    {log.type === 'success' && <CheckCircle size={14} />}
                    <span>{`[${new Date().toLocaleTimeString()}] ${log.message}`}</span>
                  </motion.div>
                ))}
              </AnimatePresence>
              {logs.length === 0 && <div style={{ opacity: 0.3 }}>Waiting for actions...</div>}
            </div>
          </div>
        </footer>
      </main>
    </div>
  );
}

export default App;
