from typing import Dict, Any, List, Optional, Union
from tabulate import tabulate

class BenchmarkReportGenerator:
    """
    Terminal Table & JSON Report Generator for Prompt Benchmark Results.
    """

    def generate_terminal_table(self, benchmark_results: List[Dict[str, Any]]) -> str:
        headers = ["Variant", "Word Count", "Specificity", "Clarity", "Quality Grade"]
        table_data = []

        for item in benchmark_results:
            metrics = item.get("metrics", {})
            table_data.append([
                item.get("variant", "unknown"),
                metrics.get("word_count", 0),
                metrics.get("specificity_score", 0.0),
                metrics.get("clarity_score", 0.0),
                metrics.get("overall_quality_grade", "N/A")
            ])

        return tabulate(table_data, headers=headers, tablefmt="github")

    def generate_json_report(self, benchmark_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            "total_variants_evaluated": len(benchmark_results),
            "results": benchmark_results,
            "status": "REPORT_GENERATED"
        }
