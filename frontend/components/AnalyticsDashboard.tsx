"use client";

import { Analytics } from "@/types";
import {
  PieChart, Pie, Cell, ResponsiveContainer, Tooltip,
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Legend,
} from "recharts";

const COLORS = ["#4F46E5", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#06B6D4"];

function SummaryCard({ label, value }: { label: string; value: string | number }) {
  return (
    <div className="bg-white border rounded-lg p-4 shadow-sm">
      <p className="text-sm text-gray-500">{label}</p>
      <p className="text-xl font-semibold mt-1">{value}</p>
    </div>
  );
}

export default function AnalyticsDashboard({ analytics }: { analytics: Analytics }) {
  const sourceData = Object.entries(analytics.dataset_source_distribution).map(
    ([name, value]) => ({ name, value })
  );

  const typeData = Object.entries(analytics.dataset_type_distribution).map(
    ([name, value]) => ({ name, value })
  );

  return (
    <div className="mb-8">
      <h2 className="text-lg font-bold mb-4">Search Analytics Dashboard</h2>

      {/* Summary Cards */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3 mb-6">
        <SummaryCard label="Detected Task" value={analytics.detected_task} />
        <SummaryCard label="Detected Domain" value={analytics.detected_domain} />
        <SummaryCard label="Datasets Found" value={analytics.datasets_found} />
        <SummaryCard label="GitHub Projects" value={analytics.github_projects_found} />
        <SummaryCard
          label="Avg Similarity"
          value={`${Math.round(analytics.average_similarity * 100)}%`}
        />
        <SummaryCard
          label="Sources"
          value={analytics.sources_searched.join(", ")}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white border rounded-lg p-4 shadow-sm">
          <p className="text-sm font-medium mb-2">Dataset Source Distribution</p>
          <ResponsiveContainer width="100%" height={250}>
            <PieChart>
              <Pie
                data={sourceData}
                dataKey="value"
                nameKey="name"
                cx="50%"
                cy="50%"
                outerRadius={80}
                label
              >
                {sourceData.map((_, index) => (
                  <Cell key={index} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white border rounded-lg p-4 shadow-sm">
          <p className="text-sm font-medium mb-2">Dataset Type Distribution</p>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={typeData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" tick={{ fontSize: 12 }} />
              <YAxis allowDecimals={false} />
              <Tooltip />
              <Bar dataKey="value" fill="#4F46E5" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}