"use client";

import { useState } from "react";
import { DatasetResult, GitHubResult } from "@/types";
import DatasetCard from "./DatasetCard";
import GitHubCard from "./GitHubCard";

function EmptyState({ type, hasSearched }: { type: string; hasSearched: boolean }) {
  return <div className="grid min-h-48 place-items-center rounded-3xl border border-dashed border-[#cbd7ed] bg-white/70 p-8 text-center"><div><p className="font-semibold text-[#22355f]">{hasSearched ? `No ${type.toLowerCase()} matched this search.` : `${type} will appear here.`}</p><p className="mt-1 text-sm text-[#75829e]">{hasSearched ? "Try a broader description or different keywords." : "Use the search above to receive curated matches."}</p></div></div>;
}

function SeeMoreButton({ expanded, onClick }: { expanded: boolean; onClick: () => void }) {
  return <div className="mt-6 text-center"><button onClick={onClick} className="rounded-xl border border-[#1B4EF5] px-5 py-2.5 text-sm font-bold text-[#1B4EF5] transition hover:bg-[#1B4EF5] hover:text-white">{expanded ? "Show less" : "See more"}</button></div>;
}

export function DatasetResults({ datasets, hasSearched }: { datasets: DatasetResult[]; hasSearched: boolean }) {
  const [expanded, setExpanded] = useState(false);
  const visibleDatasets = expanded ? datasets : datasets.slice(0, 3);
  return <section className="mb-12"><div className="mb-5 flex items-end justify-between"><h2 className="text-2xl font-bold tracking-tight text-[#14254c]">Recommended datasets</h2>{datasets.length > 0 && <span className="text-sm text-[#73809b]">{datasets.length} matches</span>}</div>{datasets.length ? <><div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">{visibleDatasets.map((d) => <DatasetCard key={d.id} dataset={d} />)}</div>{datasets.length > 3 && <SeeMoreButton expanded={expanded} onClick={() => setExpanded((current) => !current)} />}</> : <EmptyState type="Datasets" hasSearched={hasSearched} />}</section>;
}

export function GitHubResults({ repos, hasSearched }: { repos: GitHubResult[]; hasSearched: boolean }) {
  const [expanded, setExpanded] = useState(false);
  const visibleRepos = expanded ? repos : repos.slice(0, 3);
  return <section><div className="mb-5 flex items-end justify-between"><h2 className="text-2xl font-bold tracking-tight text-[#14254c]">Similar projects</h2>{repos.length > 0 && <span className="text-sm text-[#73809b]">{repos.length} matches</span>}</div>{repos.length ? <><div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">{visibleRepos.map((r) => <GitHubCard key={r.id} repo={r} />)}</div>{repos.length > 3 && <SeeMoreButton expanded={expanded} onClick={() => setExpanded((current) => !current)} />}</> : <EmptyState type="GitHub repositories" hasSearched={hasSearched} />}</section>;
}
