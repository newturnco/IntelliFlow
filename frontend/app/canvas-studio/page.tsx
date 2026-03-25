'use client';
import { CanvasEditor } from '@/components/CanvasEditor';
export default function CanvasStudio() {
  return (
    <div className="h-screen">
      <CanvasEditor /> {/* React Flow + drag-drop layout JSON saved per tenant */}
    </div>
  );
}