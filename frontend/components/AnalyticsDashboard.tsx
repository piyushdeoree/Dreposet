"use client";

import { Analytics, GitHubResult } from "@/types";
import { BarChart3, Database, FolderGit2, Star, Target } from "lucide-react";
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";

const CHART_COLORS = ["#1B4EF5", "#80a8ff", "#73d6b3", "#ffbf63", "#c49cff", "#f48ba8"];

function Metric({ icon: Icon, label, value }: { icon: typeof Database; label: string; value: string | number }) {
  return <div className="rounded-2xl bg-white p-4 shadow-sm"><div className="flex items-center gap-2"><Icon size={18} className="text-[#1B4EF5]" /><p className="text-xs font-medium text-[#66738f]">{label}</p></div><p className="mt-4 truncate text-2xl font-bold text-[#172850] sm:text-3xl">{value}</p></div>;
}

export default function AnalyticsDashboard({ analytics, projects }: { analytics?: Analytics; projects: GitHubResult[] }) {
  const sourceData = analytics ? Object.entries(analytics.dataset_source_distribution).map(([name, value]) => ({ name, value })) : [];
  const topProjects = [...projects].sort((a, b) => b.stars - a.stars).slice(0, 3);

  return <section className="mb-12 overflow-hidden rounded-3xl bg-gradient-to-br from-[#1B4EF5] to-[#5996FF] p-6 text-white shadow-[0_20px_45px_rgba(27,78,245,0.24)] sm:p-8">
    <div className="grid grid-cols-2 gap-3 lg:grid-cols-4"><Metric icon={Target} label="Detected task" value={analytics?.detected_task || "—"} /><Metric icon={Database} label="Datasets found" value={analytics?.datasets_found ?? "—"} /><Metric icon={FolderGit2} label="GitHub projects" value={analytics?.github_projects_found ?? "—"} /><Metric icon={BarChart3} label="Match confidence" value={analytics ? `${Math.round(analytics.average_similarity * 100)}%` : "—"} /></div>

    <div className="mt-5 grid gap-6 rounded-2xl bg-white p-4 lg:grid-cols-[minmax(0,1fr)_minmax(330px,0.85fr)]">
      <div><p className="text-xs font-semibold text-[#172850]">Dataset sources</p>{sourceData.length > 0 ? <div className="mt-2 flex min-h-64 items-center gap-6"><div className="h-56 w-56 shrink-0"><ResponsiveContainer width="100%" height="100%"><PieChart><Pie data={sourceData} dataKey="value" nameKey="name" outerRadius={100}>{sourceData.map((item, index) => <Cell key={item.name} fill={CHART_COLORS[index % CHART_COLORS.length]} />)}</Pie><Tooltip /></PieChart></ResponsiveContainer></div><div className="flex flex-col gap-3">{sourceData.map((item, index) => <span key={item.name} className="flex items-center gap-2 text-sm text-[#172850]"><i className="h-2.5 w-2.5 rounded-full" style={{ backgroundColor: CHART_COLORS[index % CHART_COLORS.length] }} />{item.name} <b>{item.value}</b></span>)}</div></div> : <p className="mt-2 text-sm text-[#66738f]">Source distribution will appear after your search.</p>}</div>
      <div><p className="text-xs font-semibold text-[#172850]">Top 3 similar projects</p>{topProjects.length > 0 ? <div className="mt-2 grid gap-1.5">{topProjects.map((project) => <article key={project.id} className="flex flex-col rounded-lg bg-[#1B4EF5] px-3 py-2 text-white"><div className="min-w-0"><h3 className="truncate text-xs font-semibold">{project.name}</h3><p className="mt-0.5 line-clamp-1 text-[11px] text-[#e8efff]">{project.description || "Open-source project recommended for this search."}</p></div><div className="mt-1.5 flex items-center justify-between"><span className="flex items-center gap-1 text-[10px] text-[#edf2ff]"><Star size={11} className="fill-[#ffd563] text-[#ffd563]" />{project.stars.toLocaleString()} · {project.language || "Code"}</span><a href={project.url} target="_blank" rel="noopener noreferrer" className="rounded-md bg-white px-2 py-0.5 text-[11px] font-bold text-[#1B4EF5] transition hover:bg-[#eaf0ff]">View</a></div></article>)}</div> : <p className="mt-2 text-sm text-[#66738f]">Similar projects will appear after your search.</p>}</div>
    </div>
  </section>;
}
