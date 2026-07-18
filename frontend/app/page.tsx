"use client";

import { useState } from "react";
import AnalyticsDashboard from "@/components/AnalyticsDashboard";
import { DatasetResults, GitHubResults } from "@/components/ResultsSection";
import { SearchResponse } from "@/types";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

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

      if (!res.ok) {
        throw new Error("Search failed. Please try again.");
      }

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
    <main className="p-8 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Dataset & GitHub Recommender</h1>

      <div className="flex gap-2 mb-2">
        <input
          className="border rounded p-2 flex-1"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSearch()}
          placeholder="Describe your project..."
        />
        <button
          onClick={handleSearch}
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-2 rounded disabled:opacity-50"
        >
          {loading ? "Searching..." : "Search"}
        </button>
      </div>

      {error && <p className="text-red-600 text-sm mb-4">{error}</p>}

      {loading && (
        <p className="text-gray-500 text-sm mb-4">
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
  );
}