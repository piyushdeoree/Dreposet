import { DatasetResult } from "@/types";

export default function DatasetCard({ dataset }: { dataset: DatasetResult }) {
  return (
    <div className="bg-white border rounded-lg p-4 shadow-sm flex flex-col justify-between">
      <div>
        <div className="flex justify-between items-start mb-1">
          <h3 className="font-semibold text-base">{dataset.name}</h3>
          <span className="text-xs bg-gray-100 px-2 py-1 rounded text-gray-600 whitespace-nowrap ml-2">
            {dataset.source}
          </span>
        </div>

        <p className="text-sm text-gray-600 mb-2 line-clamp-3">
          {dataset.description}
        </p>

        {dataset.tags && dataset.tags.length > 0 && (
          <div className="flex flex-wrap gap-1 mb-2">
            {dataset.tags.slice(0, 4).map((tag) => (
              <span
                key={tag}
                className="text-xs bg-blue-50 text-blue-700 px-2 py-0.5 rounded"
              >
                {tag}
              </span>
            ))}
          </div>
        )}

        <p className="text-xs text-gray-500 italic mb-3">
          {dataset.why_recommended}
        </p>
      </div>

      <div className="flex items-center justify-between mt-2">
        <span className="text-xs text-gray-400">
          Similarity: {Math.round(dataset.similarity * 100)}%
        </span>

        <a
          href={dataset.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-sm bg-blue-600 text-white px-3 py-1.5 rounded hover:bg-blue-700"
        >
          Open Dataset
        </a>
      </div>
    </div>
  );
}