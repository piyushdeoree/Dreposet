export interface Analytics {
  detected_task: string;
  detected_domain: string;
  datasets_found: number;
  github_projects_found: number;
  average_similarity: number;
  sources_searched: string[];
  dataset_source_distribution: Record<string, number>;
  dataset_type_distribution: Record<string, number>;
}

export interface DatasetResult {
  id: number;
  name: string;
  source: string;
  description: string;
  url: string;
  tags: string[];
  similarity: number;
  final_score: number;
  why_recommended: string;
}

export interface GitHubResult {
  id: number;
  name: string;
  description: string;
  language: string;
  stars: number;
  url: string;
  similarity: number;
  final_score: number;
  why_recommended: string;
}

export interface SearchResponse {
  analytics: Analytics;
  datasets: DatasetResult[];
  github_repos: GitHubResult[];
}