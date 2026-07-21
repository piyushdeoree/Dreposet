"use client";

import { Search } from "lucide-react";

interface SearchBarProps {
  query: string;
  setQuery: (val: string) => void;
  onSearch: () => void;
  loading: boolean;
}

export default function SearchBar({ query, setQuery, onSearch, loading, hasResult }: SearchBarProps & { hasResult: boolean }) {
  return (
    <section className={`mx-auto flex max-w-4xl flex-col justify-center px-5 text-center ${hasResult ? "pb-12 pt-14 sm:pt-18" : "min-h-[calc(100vh-92px)] pb-24 pt-10 sm:pb-32"}`} id="top">
      <h1 className="mx-auto max-w-3xl text-4xl font-black tracking-[-0.045em] text-[#122047] sm:text-5xl">
        Find the data that moves your idea forward.
      </h1>
      <p className="mx-auto mt-4 max-w-2xl text-base leading-7 text-[#637092]">
        Describe what you&apos;re building in everyday language. We&apos;ll surface the most relevant datasets and open-source projects.
      </p>

      <div className="mt-8 flex items-center gap-3 rounded-2xl border border-[#dbe5f7] bg-white p-2 pl-4 text-left shadow-[0_16px_40px_rgba(27,55,102,0.1)] transition focus-within:border-[#759ce8] focus-within:shadow-[0_16px_40px_rgba(27,55,102,0.16)] sm:pl-5">
        <Search className="shrink-0 text-[#69789c]" size={21} />
        <input
          className="min-w-0 flex-1 bg-transparent py-2 text-sm text-[#152349] outline-none placeholder:text-[#8792ad] sm:text-base"
          placeholder="I want to build a fake news detector for social media..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && onSearch()}
          aria-label="Describe the dataset or project you need"
        />
        <button onClick={onSearch} disabled={loading} className="inline-flex shrink-0 items-center gap-1.5 rounded-xl bg-[#1B4EF5] px-3 py-3 text-sm font-bold text-white transition hover:bg-[#5996FF] disabled:cursor-not-allowed disabled:opacity-60 sm:px-4" aria-label="Search">
          <span className="hidden sm:inline">{loading ? "Searching" : "Discover"}</span>
        </button>
      </div>
    </section>
  );
}
