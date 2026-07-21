"use client";

import { useEffect, useState } from "react";
import Header from "@/components/Header";
import SearchBar from "@/components/SearchBar";
import AnalyticsDashboard from "@/components/AnalyticsDashboard";
import { DatasetResults, GitHubResults } from "@/components/ResultsSection";
import { SearchResponse } from "@/types";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export default function Home() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState<SearchResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const savedResult = window.localStorage.getItem("datafind-search-result");
    const savedQuery = window.localStorage.getItem("datafind-search-query");
    if (savedResult) {
      try { setResult(JSON.parse(savedResult) as SearchResponse); } catch { window.localStorage.removeItem("datafind-search-result"); }
    }
    if (savedQuery) setQuery(savedQuery);
  }, []);

  async function handleSearch() {
    if (!query.trim()) return;
    setLoading(true); setError(null);
    try {
      const res = await fetch(`${API_URL}/api/search`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ query }) });
      if (!res.ok) throw new Error("Search failed. Please try again.");
      const nextResult = await res.json() as SearchResponse;
      setResult(nextResult);
      window.localStorage.setItem("datafind-search-result", JSON.stringify(nextResult));
      window.localStorage.setItem("datafind-search-query", query);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong"); setResult(null);
    } finally { setLoading(false); }
  }

  function handleHome() {
    window.localStorage.removeItem("datafind-search-result");
    window.localStorage.removeItem("datafind-search-query");
    setQuery("");
    setResult(null);
    setError(null);
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  return <div className="min-h-screen bg-[#f7f9fe] bg-[radial-gradient(#dbe5f6_1px,transparent_1px)] bg-[size:20px_20px]">
    {loading && <div className="fixed inset-0 z-50 grid place-items-center bg-[#f7f9fe]/80 backdrop-blur-sm" role="status" aria-live="polite" aria-label="Searching for recommendations">
      <div className="flex flex-col items-center gap-4 rounded-3xl bg-white px-9 py-8 shadow-[0_18px_45px_rgba(27,78,245,0.18)]">
        <span className="h-12 w-12 animate-spin rounded-full border-4 border-transparent border-r-[#5996FF] border-t-[#5996FF]" />
        <p className="text-sm font-semibold text-[#1B4EF5]">Finding your best matches...</p>
      </div>
    </div>}
    <Header onHome={handleHome} />
    <SearchBar query={query} setQuery={setQuery} onSearch={handleSearch} loading={loading} hasResult={Boolean(result)} />
    {result && <main className="mx-auto max-w-6xl px-5 pb-16 sm:px-6">
      {error && <p className="mb-5 rounded-xl border border-red-200 bg-red-50 p-3 text-center text-sm text-red-600">{error}</p>}
      <AnalyticsDashboard analytics={result?.analytics} projects={result?.github_repos ?? []} />
      <DatasetResults datasets={result?.datasets ?? []} hasSearched={Boolean(result)} />
      <GitHubResults repos={result?.github_repos ?? []} hasSearched={Boolean(result)} />
    </main>}
  </div>;
}
