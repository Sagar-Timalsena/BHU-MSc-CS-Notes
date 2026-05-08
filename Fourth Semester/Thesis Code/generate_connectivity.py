# ==========================================================
# 🔗 Connectivity Matrix Generator (Δ)
# ----------------------------------------------------------
# Generates: connectivity_matrix.xlsx / connectivity_matrix.csv
# Shows which miners can connect to which ECSPs
# ==========================================================

import pandas as pd
import numpy as np
import random

# ------------------------------
# ⚙️ CONFIGURATION
# ------------------------------
NUM_MINERS = 300       # same as miners
NUM_ECSP = 5           # same as ECSPs
CONNECT_PROB = 0.3     # probability of miner ↔ ECSP connectivity
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# ------------------------------
# 🔗 Generate Connectivity Matrix
# ------------------------------
connectivity = np.random.choice(
    [0, 1],
    size=(NUM_MINERS, NUM_ECSP),
    p=[1 - CONNECT_PROB, CONNECT_PROB]
)

# Convert to DataFrame
connectivity_df = pd.DataFrame(
    connectivity,
    columns=[f"E{j}" for j in range(1, NUM_ECSP + 1)]
)
connectivity_df.insert(0, "Miner_ID", [f"M{i}" for i in range(1, NUM_MINERS + 1)])

# ------------------------------
# 💾 Save to File
# ------------------------------
connectivity_df.to_csv("connectivity_matrix.csv", index=False)
connectivity_df.to_excel("connectivity_matrix.xlsx", index=False)
print("✅ connectivity_matrix.xlsx and connectivity_matrix.csv created successfully!")

# ------------------------------
# 📊 Summary
# ------------------------------
print(f"Connectivity Probability: {CONNECT_PROB * 100}%")
connected_links = np.sum(connectivity)
print(f"Total possible links: {NUM_MINERS * NUM_ECSP}")
print(f"Actual active connections: {connected_links}")
print(f"Average connections per miner: {connected_links / NUM_MINERS:.2f}")
