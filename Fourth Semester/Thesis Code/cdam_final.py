# ==========================================================
# ⚙️ CDAM (Constant Demand Auction Mechanism) - Final Version
# ----------------------------------------------------------
# Prints allocation summary to terminal and saves results to CSV
# ==========================================================

import pandas as pd
import numpy as np
import itertools
import time

# ------------------------------
# ⚙️ PARAMETERS
# ------------------------------
MU = 0.1
NU = 0.5e-4
OUTPUT_FILE = "cdam_allocation_results.csv"

# ------------------------------
# 📂 LOAD DATA
# ------------------------------
miners = pd.read_csv("miners.csv")
ecsps = pd.read_csv("ecsp.csv")
delta_df = pd.read_csv("connectivity_matrix.csv")
delta = delta_df.drop(columns=['Miner_ID']).to_numpy()

N, M = delta.shape

# ------------------------------
# 🧮 HELPER FUNCTIONS
# ------------------------------
def network_effect(mu, nu, dN):
    return (1 - np.exp(-nu * dN)) / (1 + mu * np.exp(-nu * dN))

def compute_social_welfare(bids, x, delta, mu, nu, demands, capacities):
    """
    Compute social welfare:
    S = Σ_i Σ_j b_i * ω(dN) * (d_i/D) * x_ij * δ_ij
    """
    # Expand demands and bids to 2D for broadcasting
    demands_2d = demands.reshape(-1, 1)
    bids_2d = bids.reshape(-1, 1)

    # Total allocated demand
    dN = np.sum(demands_2d * x * delta)

    # Total ECSP capacity
    D = np.sum(capacities)

    # Network effect
    omega = (1 - np.exp(-nu * dN)) / (1 + mu * np.exp(-nu * dN))

    # Compute welfare
    S = np.sum(bids_2d * omega * (demands_2d / D) * x * delta)
    return S


# ------------------------------
# 💰 CDAM ALGORITHM
# ------------------------------
def CDAM_allocation(miners, ecsps, delta, mu, nu):
    bids = miners["Bid_Value"].to_numpy()
    demands = miners["Weighted_Resource"].to_numpy()
    capacities = ecsps["Weighted_Capacity"].to_numpy()

    x = np.zeros((N, M))
    used_cap = np.zeros(M)

    pairs = [(i, j, bids[i]) for i, j in itertools.product(range(N), range(M)) if delta[i, j] == 1]
    pairs.sort(key=lambda x: x[2], reverse=True)

    for i, j, _ in pairs:
        if used_cap[j] + demands[i] <= capacities[j] and not x[i].any():
            x[i, j] = 1
            used_cap[j] += demands[i]

    S = compute_social_welfare(bids, x, delta, mu, nu, demands, capacities)
    winners = np.sum(x.sum(axis=1) > 0)
    satisfaction = winners / N * 100
    utilization = (used_cap.sum() / capacities.sum()) * 100

    return S, satisfaction, utilization, winners, x, used_cap

# ------------------------------
# 🚀 RUN CDAM
# ------------------------------
start = time.time()
S, sat, util, win, X, used_cap = CDAM_allocation(miners, ecsps, delta, MU, NU)
end = time.time()

# ------------------------------
# 📊 DISPLAY RESULTS
# ------------------------------
print("\n========== CDAM Allocation Results ==========")
print(f"Total Miners: {N}, ECSPs: {M}")
print(f"Social Welfare      : {S:.3f}")
print(f"Satisfaction (Win%) : {sat:.2f}%")
print(f"Resource Utilization: {util:.2f}%")
print(f"Winning Miners      : {win}")
print(f"Execution Time      : {end - start:.3f} sec")

print("\n--- ECSP Resource Usage ---")
for j in range(M):
    print(f"ECSP E{j+1}: Used = {used_cap[j]:.2f} / {ecsps['Weighted_Capacity'][j]:.2f}")

# ------------------------------
# 💾 SAVE RESULTS TO CSV
# ------------------------------
alloc_df = pd.DataFrame(X, columns=[f"E{j+1}" for j in range(M)])
alloc_df.insert(0, "Miner_ID", miners["Miner_ID"])
alloc_df["Allocated_ECSP"] = alloc_df.iloc[:, 1:].idxmax(axis=1)
alloc_df["Allocated"] = (alloc_df.iloc[:, 1:M+1].sum(axis=1) > 0).astype(int)

alloc_df.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Allocation details saved to: {OUTPUT_FILE}")
