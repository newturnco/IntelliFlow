'use client';
import { useState } from 'react';
export default function AskAIChat() {
  const [message, setMessage] = useState('');
  // Web Speech API for voice + LangChain backend call
  return (
    <div className="chat-window">
      {/* Real-time chat with "Show me this month's revenue" → chart rendering */}
    </div>
  );
}