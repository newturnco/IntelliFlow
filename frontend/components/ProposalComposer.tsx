'use client';
import { useState } from 'react';
export default function ProposalComposer() {
  const [prompt, setPrompt] = useState('');
  const generate = async () => {
    const res = await fetch('/api/ai/generate-proposal', {
      method: 'POST',
      body: JSON.stringify({ deal_id: 123, style: 'Modern', instructions: prompt })
    });
    const data = await res.json();
    // Render markdown + PDF preview
  };
  return (
    <div>
      <textarea value={prompt} onChange={e => setPrompt(e.target.value)} placeholder="Describe your proposal..." />
      <button onClick={generate} className="bg-blue-600 text-white px-6 py-3">Generate with AI</button>
      {/* AI Writing Assistant, Readability, Tone buttons here */}
    </div>
  );
}