'use client';
import ReactFlow, { useNodesState, useEdgesState } from 'reactflow';
export default function CanvasEditor() {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  // ... full drag-drop editor for layouts, saved to /api/canvas
  return <ReactFlow nodes={nodes} edges={edges} onNodesChange={onNodesChange} />;
}