import Link from 'next/link';
import { MDXRemote } from 'next-mdx-remote/rsc';

export default function DocsHome() {
  return (
    <div className="max-w-4xl mx-auto p-8">
      <h1 className="text-5xl font-bold mb-8">IntelliFlow CRM Documentation</h1>
      <div className="grid grid-cols-2 gap-8">
        <Link href="/features" className="block p-6 bg-zinc-900 rounded-2xl hover:bg-zinc-800">Core Features</Link>
        <Link href="/deployment" className="block p-6 bg-zinc-900 rounded-2xl hover:bg-zinc-800">Deployment Guide</Link>
        <Link href="/api" className="block p-6 bg-zinc-900 rounded-2xl hover:bg-zinc-800">API Reference</Link>
        <Link href="/ai" className="block p-6 bg-zinc-900 rounded-2xl hover:bg-zinc-800">AI &amp; Proposal Builder</Link>
      </div>
    </div>
  );
}