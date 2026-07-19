"use client";

import { useState } from "react";
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

  async function handleSearch() {
    if (!query.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${API_URL}/api/search`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });
      if (!res.ok) throw new Error("Search failed. Please try again.");
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
      setResult(null);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <SearchBar query={query} setQuery={setQuery} onSearch={handleSearch} loading={loading} />

      <main className="max-w-6xl mx-auto px-6 pb-12">
        {error && <p className="text-red-600 text-sm mb-4 text-center">{error}</p>}
        {loading && (
          <p className="text-gray-500 text-sm mb-4 text-center">
            Searching across Kaggle, Hugging Face, GitHub, and more...
          </p>
        )}

        {result && (
          <>
            <AnalyticsDashboard analytics={result.analytics} />
            <DatasetResults datasets={result.datasets} />
            <GitHubResults repos={result.github_repos} />
          </>
        )}
      </main>
    </div>
  );
}