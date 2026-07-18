import { DatasetResult, GitHubResult } from "@/types";
import DatasetCard from "./DatasetCard";
import GitHubCard from "./GitHubCard";

export function DatasetResults({ datasets }: { datasets: DatasetResult[] }) {
  if (datasets.length === 0) return null;

  return (
    <div className="mb-8">
      <h2 className="text-lg font-bold mb-4">Recommended Datasets</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {datasets.map((d) => (
          <DatasetCard key={d.id} dataset={d} />
        ))}
      </div>
    </div>
  );
}

export function GitHubResults({ repos }: { repos: GitHubResult[] }) {
  if (repos.length === 0) return null;

  return (
    <div className="mb-8">
      <h2 className="text-lg font-bold mb-4">Similar GitHub Projects</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {repos.map((r) => (
          <GitHubCard key={r.id} repo={r} />
        ))}
      </div>
    </div>
  );
}