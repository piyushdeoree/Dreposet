"use client";

import { CircleHelp, Home, LogIn, Settings, ShieldCheck } from "lucide-react";

const navigation = [
  { label: "Home", icon: Home },
  { label: "About", icon: CircleHelp },
  { label: "Policy", icon: ShieldCheck },
  { label: "Settings", icon: Settings },
  { label: "Login", icon: LogIn },
];

export default function Header({ onHome }: { onHome?: () => void }) {
  return (
    <header className="px-4 pt-4 sm:px-6 sm:pt-6">
      <div className="mx-auto flex max-w-6xl items-center justify-between rounded-2xl border border-blue-100 bg-white/85 px-3 py-2.5 shadow-[0_10px_30px_rgba(31,48,87,0.08)] backdrop-blur sm:px-4">
        <a className="flex items-center gap-2.5" href="#top" aria-label="Dataset Discovery home">
          {/* Replace public/logo.svg with your own logo image whenever you are ready. */}
          <img src="Dreposet.png" className="h-10 w-25  object-cover" />
        </a>

        <nav className="flex items-center gap-1.5" aria-label="Primary navigation">
          {navigation.map(({ label, icon: Icon }) => (
            <button key={label} title={label} aria-label={label} onClick={label === "Home" ? onHome : undefined} className="grid h-9 w-9 place-items-center rounded-xl text-[#314269] transition hover:bg-[#edf3ff] hover:text-[#1B4EF5] focus:outline-none focus:ring-2 focus:ring-[#9bbcff]">
              <Icon size={18} strokeWidth={2.2} />
            </button>
          ))}
        </nav>
      </div>
    </header>
  );
}
