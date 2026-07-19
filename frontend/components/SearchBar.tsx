"use client";

import { Search } from "lucide-react";

interface SearchBarProps {
  query: string;
  setQuery: (val: string) => void;
  onSearch: () => void;
  loading: boolean;
}

export default function SearchBar({ query, setQuery, onSearch, loading }: SearchBarProps) {
  return (
    <div className="max-w-2xl mx-auto mt-6 mb-8 px-6">
      <div className="flex items-center bg-gray-100 rounded-full px-4 py-2 shadow-sm">
        <input
          className="flex-1 bg-transparent outline-none text-sm"
          placeholder="Describe your project... e.g. 'I want to build a fake news detector'"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && onSearch()}
        />
        <button
          onClick={onSearch}
          disabled={loading}
          className="text-gray-500 hover:text-gray-800 disabled:opacity-40"
        >
          <Search size={18} />
        </button>
      </div>
    </div>
  );
}