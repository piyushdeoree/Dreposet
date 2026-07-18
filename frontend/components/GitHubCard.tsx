import { GitHubResult } from "@/types";
import { Star } from "lucide-react";

export default function GitHubCard({ repo }: { repo: GitHubResult }) {
  return (
    <div className="bg-white border rounded-lg p-4 shadow-sm flex flex-col justify-between">
      <div>
        <div className="flex justify-between items-start mb-1">
          <h3 className="font-semibold text-base break-all">{repo.name}</h3>
          <span className="text-xs bg-gray-100 px-2 py-1 rounded text-gray-600 whitespace-nowrap ml-2">
            {repo.language}
          </span>
        </div>

        <p className="text-sm text-gray-600 mb-2 line-clamp-3">
          {repo.description}
        </p>

        <p className="text-xs text-gray-500 italic mb-3">
          {repo.why_recommended}
        </p>
      </div>

      <div className="flex items-center justify-between mt-2">
        <span className="text-xs text-gray-500 flex items-center gap-1">
          <Star size={12} className="fill-yellow-400 text-yellow-400" />
          {repo.stars.toLocaleString()}
        </span>

        <a
          href={repo.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm bg-gray-800 text-white px-3 py-1.5 rounded hover:bg-gray-900"
        >
          Open Repository
        </a>
      </div>
    </div>
  );
}