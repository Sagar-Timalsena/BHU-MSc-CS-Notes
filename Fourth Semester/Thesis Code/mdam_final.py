#!/usr/bin/env python3
"""
CDAM vs MDAM Experiment Analysis
Uses existing CSV datasets (no Excel required)
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "comparison_plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ===============================
# LOAD DATA (USING YOUR FILES)
# ===============================
try:
    cdam_alloc = pd.read_csv("cdam_allocation_results.csv")
    mdam_alloc = pd.read_csv("mdam_allocation_results.csv")
    ecsp = pd.read_csv("ecsp_summary.csv")
except FileNotFoundError as e:
    print("❌ File not found:", e)
    exit(1)

# ===============================
# METRIC FUNCTION
# ===============================
def compute_metrics(alloc_df, ecsp_df, method):
    total_miners = len(alloc_df)
    winners = alloc_df[alloc_df["Allocated"] == 1]

    satisfaction = len(winners) / total_miners * 100
    miner_profit = winners["Miner_Profit"].sum()
    ecsp_profit = ecsp_df["ECSP_Profit"].iloc[0]
    utilization = ecsp_df["Utilization_weighted_pct"].iloc[0]
    social_welfare = miner_profit + ecsp_profit

    return {
        "Method": method,
        "Total Miners": total_miners,
        "Winners": len(winners),
        "Satisfaction (%)": round(satisfaction, 2),
        "Miner Profit": round(miner_profit, 4),
        "ECSP Profit": round(ecsp_profit, 4),
        "Social Welfare": round(social_welfare, 4),
        "Utilization (%)": round(utilization, 2)
    }

# ===============================
# COMPUTE METRICS
# ===============================
cdam_metrics = compute_metrics(cdam_alloc, ecsp, "CDAM")
mdam_metrics = compute_metrics(mdam_alloc, ecsp, "MDAM")

results_df = pd.DataFrame([cdam_metrics, mdam_metrics])

print("\n=== CDAM vs MDAM RESULTS ===")
print(results_df)

results_df.to_csv("combined_experiment_results.csv", index=False)

# ===============================
# GRAPH 1: SATISFACTION RATIO
# ===============================
plt.figure(figsize=(6,4))
plt.bar(results_df["Method"], results_df["Satisfaction (%)"])
plt.ylabel("Satisfaction (%)")
plt.title("Satisfaction Ratio: CDAM vs MDAM")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/satisfaction.png")
plt.close()

# ===============================
# GRAPH 2: UTILIZATION
# ===============================
plt.figure(figsize=(6,4))
plt.bar(results_df["Method"], results_df["Utilization (%)"])
plt.ylabel("Utilization (%)")
plt.title("ECSP Utilization Comparison")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/utilization.png")
plt.close()

# ===============================
# GRAPH 3: SOCIAL WELFARE
# ===============================
plt.figure(figsize=(6,4))
plt.bar(results_df["Method"], results_df["Social Welfare"])
plt.ylabel("Social Welfare")
plt.title("Social Welfare: CDAM vs MDAM")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/social_welfare.png")
plt.close()

# ===============================
# GRAPH 4: PROFIT COMPARISON
# ===============================
labels = ["Miner Profit", "ECSP Profit"]
cdam_vals = [cdam_metrics["Miner Profit"], cdam_metrics["ECSP Profit"]]
mdam_vals = [mdam_metrics["Miner Profit"], mdam_metrics["ECSP Profit"]]

x = range(len(labels))
plt.figure(figsize=(7,4))
plt.bar(x, cdam_vals, width=0.35, label="CDAM")
plt.bar([i+0.35 for i in x], mdam_vals, width=0.35, label="MDAM")
plt.xticks([i+0.175 for i in x], labels)
plt.ylabel("Profit")
plt.title("Profit Comparison: CDAM vs MDAM")
plt.legend()
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/profit.png")
plt.close()

print("\n✅ Analysis completed successfully")
print("📂 Output CSV  : combined_experiment_results.csv")
print("📊 Graphs in   :", OUTPUT_DIR)
