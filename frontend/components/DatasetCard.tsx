import { Database } from "lucide-react";
import { DatasetResult } from "@/types";

export default function DatasetCard({ dataset }: { dataset: DatasetResult }) {
  return (
    <article className="flex min-h-72 flex-col rounded-3xl border border-[#e0e7f4] bg-white p-5 shadow-[0_8px_24px_rgba(29,48,90,0.05)] transition hover:-translate-y-1 hover:shadow-[0_16px_32px_rgba(29,48,90,0.1)]">
      <div className="flex items-start justify-between gap-3">
        <span className="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-[#eef3ff] text-[#1B4EF5]"><Database size={19} /></span>
        <span className="rounded-full bg-[#edf3ff] px-2.5 py-1 text-xs font-semibold text-[#45649d]">{dataset.source}</span>
      </div>
      <h3 className="mt-5 text-lg font-bold leading-6 text-[#162750]">{dataset.name}</h3>
      <p className="mt-2 line-clamp-3 text-sm leading-6 text-[#66738f]">{dataset.description}</p>
      <div className="mt-4 flex flex-wrap gap-1.5">{dataset.tags?.slice(0, 3).map((tag) => <span key={tag} className="rounded-md bg-[#f3f6fb] px-2 py-1 text-xs text-[#50617f]">{tag}</span>)}</div>
      <div className="mt-auto flex items-center justify-between border-t border-[#edf0f6] pt-4"><span className="text-xs font-medium text-[#71809c]">{Math.round(dataset.similarity * 100)}% match</span><a href={dataset.url} target="_blank" rel="noopener noreferrer" className="text-sm font-bold text-[#1B4EF5] hover:text-[#5996FF]">View</a></div>
    </article>
  );
}
