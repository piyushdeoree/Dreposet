"use client";

import { Home, Info, ShieldOff, Settings, LogIn } from "lucide-react";

function IconButton({ icon: Icon, label }: { icon: typeof Home; label: string }) {
  return (
    <button
      title={label}
      className="w-9 h-9 rounded-full bg-white/20 hover:bg-white/30 flex items-center justify-center transition-colors"
    >
      <Icon size={18} className="text-white" />
    </button>
  );
}

export default function Header() {
  return (
    <header className="bg-orange-500 px-6 py-3 flex items-center justify-between">
      <div className="flex items-center gap-2">
        <div className="w-9 h-9 bg-white rounded-md flex items-center justify-center font-bold text-orange-500">
          D
        </div>
        <span className="text-white font-bold text-lg tracking-wide">
          DREPOSET
        </span>
      </div>

      <nav className="flex items-center gap-3"> 
        <IconButton icon={Home} label="Home" />
        <IconButton icon={Info} label="About" />
        <IconButton icon={ShieldOff} label="Policy" />
        <IconButton icon={Settings} label="Settings" />
        <IconButton icon={LogIn} label="Login" />
      </nav>
    </header>
  );
}