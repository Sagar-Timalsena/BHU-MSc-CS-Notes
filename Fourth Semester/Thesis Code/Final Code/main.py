# =========================================================
# MULTI-SERVER CONNECTIVITY AWARE RESOURCE ALLOCATION
# =========================================================

# =========================================================
# COUNT CONNECTED SERVERS FOR EACH MINER
# =========================================================
import numpy as np
connected_server_count = np.sum(

    connectivity,

    axis=1

)

# =========================================================
# CREATE MINER CONNECTIVITY INFORMATION
# =========================================================

miner_connectivity_info = []

for miner in range(NUM_MINERS):

    connected_servers = []

    for server in range(NUM_SERVERS):

        if connectivity[miner][server] == 1:

            connected_servers.append(

                servers["Server_ID"].values[server]

            )

    miner_connectivity_info.append({

        "Miner_ID":

        miners["Miner_ID"].values[miner],

        "Connected_Server_Count":

        connected_server_count[miner],

        "Connected_Servers":

        ",".join(connected_servers)

    })

# =========================================================
# SAVE CONNECTIVITY INFORMATION
# =========================================================

connectivity_info_df = pd.DataFrame(

    miner_connectivity_info

)

connectivity_info_df.to_excel(

    f"Allocation_Result/miner_connectivity_t{current_time}.xlsx",

    index=False

)

# =========================================================
# PRIORITY CALCULATION
# =========================================================

priority = (

    miners["Bid_Value"].values

    /

    (

        miners["CPU_Demand"].values

        *

        miners["Storage_Demand"].values

        *

        miners["Execution_Time"].values

        + 0.001

    )

)

# =========================================================
# FINAL SCORE
# =========================================================
#
# Miner having more connected servers
# gets higher score
#
# FinalScore =
#
# ConnectedServerCount × Priority
#
# =========================================================

final_score = (

    connected_server_count

    *

    priority

)

# =========================================================
# SORT MINERS
# =========================================================

sorted_miners = np.argsort(

    -final_score

)

# =========================================================
# SAVE SORTED MINER LIST
# =========================================================

sorted_miner_list = []

for rank, miner in enumerate(sorted_miners):

    connected_servers = []

    for server in range(NUM_SERVERS):

        if connectivity[miner][server] == 1:

            connected_servers.append(

                servers["Server_ID"].values[server]

            )

    sorted_miner_list.append({

        "Rank": rank + 1,

        "Miner_ID":

        miners["Miner_ID"].values[miner],

        "Connected_Server_Count":

        connected_server_count[miner],

        "Connected_Servers":

        ",".join(connected_servers),

        "Priority":

        priority[miner],

        "Final_Score":

        final_score[miner]

    })

sorted_df = pd.DataFrame(

    sorted_miner_list

)

sorted_df.to_excel(

    f"Allocation_Result/sorted_miners_t{current_time}.xlsx",

    index=False

)

# =========================================================
# RESOURCE ALLOCATION
# =========================================================

winners = 0

social_welfare = 0

winner_miners = []

runnerup_miners = []

for miner in sorted_miners:

    allocated = False

    # =====================================================
    # FIND ALL CONNECTED SERVERS
    # =====================================================

    possible_servers = []

    for server in range(NUM_SERVERS):

        if connectivity[miner][server] == 1:

            possible_servers.append(server)

    # =====================================================
    # SORT SERVERS BY AVAILABLE CPU
    # =====================================================

    possible_servers = sorted(

        possible_servers,

        key=lambda x: remaining_cpu[x],

        reverse=True

    )

    # =====================================================
    # TRY ALLOCATION
    # =====================================================

    for server in possible_servers:

        if (

            remaining_cpu[server]

            >=

            miners["CPU_Demand"].values[miner]

            and

            remaining_storage[server]

            >=

            miners["Storage_Demand"].values[miner]

        ):

            # =================================================
            # RESOURCE ASSIGNMENT
            # =================================================

            remaining_cpu[server] -= (

                miners["CPU_Demand"].values[miner]

            )

            remaining_storage[server] -= (

                miners["Storage_Demand"].values[miner]

            )

            winners += 1

            social_welfare += (

                miners["Bid_Value"].values[miner]

            )

            allocated = True

            # =================================================
            # STORE WINNER
            # =================================================

            winner_miners.append({

                "Time": current_time,

                "Miner_ID":

                miners["Miner_ID"].values[miner],

                "Allocated_Server":

                servers["Server_ID"].values[server],

                "Connected_Server_Count":

                connected_server_count[miner],

                "Connected_Servers":

                ",".join([

                    servers["Server_ID"].values[s]

                    for s in possible_servers

                ]),

                "Priority":

                priority[miner],

                "Final_Score":

                final_score[miner],

                "Bid_Value":

                miners["Bid_Value"].values[miner],

                "CPU_Demand":

                miners["CPU_Demand"].values[miner],

                "Storage_Demand":

                miners["Storage_Demand"].values[miner],

                "Execution_Time":

                miners["Execution_Time"].values[miner]

            })

            break

    # =====================================================
    # RUNNER-UP
    # =====================================================

    if allocated == False:

        runnerup_miners.append({

            "Time": current_time,

            "Miner_ID":

            miners["Miner_ID"].values[miner],

            "Connected_Server_Count":

            connected_server_count[miner],

            "Final_Score":

            final_score[miner],

            "Reason":

            "No Available Resource"

        })

# =========================================================
# SAVE WINNER LIST
# =========================================================

winner_df = pd.DataFrame(

    winner_miners

)

winner_df.to_excel(

    f"Allocation_Result/winners_t{current_time}.xlsx",

    index=False

)

# =========================================================
# SAVE RUNNER-UP LIST
# =========================================================

runnerup_df = pd.DataFrame(

    runnerup_miners

)

runnerup_df.to_excel(

    f"Allocation_Result/runnerups_t{current_time}.xlsx",

    index=False

)

# =========================================================
# PRINT RESULTS
# =========================================================

print("\n====================================")

print("MULTI-SERVER CONNECTIVITY ALLOCATION")

print("====================================")

print(f"\nWinner Miners: {winners}")

print(f"Social Welfare: {social_welfare}")

print(

    f"Average Connected Servers:",

    round(

        np.mean(connected_server_count),

        2

    )

)

# =========================================================
# IMPORTANT FORMULAS
# =========================================================

# ConnectedServerCount =
#
# Sum of all connected servers
#
# ---------------------------------------------------------
#
# FinalScore =
#
# ConnectedServerCount × Priority
#
# ---------------------------------------------------------
#
# Priority =
#
# Bid
# -----------------------------
# CPU × Storage × ExecutionTime
#
# =========================================================



# =========================================================
# GRAPH GENERATION FOR ALL COMPARISON FACTORS
# =========================================================

# =========================================================
# IMPORT LIBRARIES
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# =========================================================
# CREATE GRAPH FOLDER
# =========================================================

os.makedirs(

    "Comparison_Graphs",

    exist_ok=True

)

# =========================================================
# LOAD FINAL RESULT FILE
# =========================================================

results = pd.read_excel(

    "Allocation_Result/final_results.xlsx"

)

# =========================================================
# TIME AXIS
# =========================================================

time_axis = results["Time"]

# =========================================================
# GRAPH FUNCTION
# =========================================================

def draw_graph(

    x,
    y,
    xlabel,
    ylabel,
    title,
    filename

):

    plt.figure(figsize=(12,6))

    plt.plot(

        x,
        y,
        marker='o',
        linewidth=2

    )

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.title(title)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(

        f"Comparison_Graphs/{filename}"

    )

    plt.close()

# =========================================================
# 1. WINNER MINERS GRAPH
# =========================================================

draw_graph(

    time_axis,

    results["Winner_Miners"],

    "Time (sec)",

    "Winner Miners",

    "Winner Miners vs Time",

    "winner_miners.png"

)

# =========================================================
# 2. SOCIAL WELFARE GRAPH
# =========================================================

draw_graph(

    time_axis,

    results["Social_Welfare"],

    "Time (sec)",

    "Social Welfare",

    "Social Welfare vs Time",

    "social_welfare.png"

)

# =========================================================
# 3. RESOURCE UTILIZATION GRAPH
# =========================================================

draw_graph(

    time_axis,

    results["Resource_Utilization"],

    "Time (sec)",

    "Resource Utilization",

    "Resource Utilization vs Time",

    "resource_utilization.png"

)

# =========================================================
# 4. CONNECTIVITY RATIO GRAPH
# =========================================================

draw_graph(

    time_axis,

    results["Connectivity_Ratio"],

    "Time (sec)",

    "Connectivity Ratio",

    "Connectivity Ratio vs Time",

    "connectivity_ratio.png"

)

# =========================================================
# 5. RUNNER-UP MINERS GRAPH
# =========================================================

runnerups = (

    1000

    -

    results["Winner_Miners"]

)

draw_graph(

    time_axis,

    runnerups,

    "Time (sec)",

    "Runner-Up Miners",

    "Runner-Up Miners vs Time",

    "runnerup_miners.png"

)

# =========================================================
# BAR GRAPH FOR AVERAGE COMPARISON
# =========================================================

average_metrics = {

    "Winner Miners":

    np.mean(results["Winner_Miners"]),

    "Social Welfare":

    np.mean(results["Social_Welfare"]),

    "Resource Utilization":

    np.mean(results["Resource_Utilization"]),

    "Connectivity Ratio":

    np.mean(results["Connectivity_Ratio"]),

    "Runner-Up Miners":

    np.mean(runnerups)

}

# =========================================================
# BAR GRAPH
# =========================================================

plt.figure(figsize=(12,6))

plt.bar(

    average_metrics.keys(),

    average_metrics.values()

)

plt.ylabel("Average Value")

plt.title("Average Performance Comparison")

plt.xticks(rotation=10)

plt.grid(True)

plt.tight_layout()

plt.savefig(

    "Comparison_Graphs/average_comparison.png"

)

plt.close()

# =========================================================
# MULTI-LINE COMPARISON GRAPH
# =========================================================

plt.figure(figsize=(14,7))

plt.plot(

    time_axis,

    results["Winner_Miners"],

    marker='o',

    label="Winner Miners"

)

plt.plot(

    time_axis,

    results["Social_Welfare"],

    marker='s',

    label="Social Welfare"

)

plt.plot(

    time_axis,

    results["Resource_Utilization"],

    marker='^',

    label="Resource Utilization"

)

plt.plot(

    time_axis,

    results["Connectivity_Ratio"],

    marker='d',

    label="Connectivity Ratio"

)

plt.xlabel("Time (sec)")

plt.ylabel("Values")

plt.title("Overall System Performance Comparison")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(

    "Comparison_Graphs/overall_comparison.png"

)

plt.close()

# =========================================================
# PRINT OUTPUT
# =========================================================

print("\n====================================")

print("GRAPH GENERATION COMPLETED")

print("====================================")

print("\nGenerated Graphs:")

print("\n1. winner_miners.png")

print("2. social_welfare.png")

print("3. resource_utilization.png")

print("4. connectivity_ratio.png")

print("5. runnerup_miners.png")

print("6. average_comparison.png")

print("7. overall_comparison.png")

print("\nAll graphs saved in:")

print("Comparison_Graphs/")

# =====================================================
# COMBINED RESULT GRAPHS
# =====================================================

import matplotlib.pyplot as plt

time_axis = results_df["Time"]

graphs = [

    (
        "Connectivity_Ratio",
        "Connectivity Ratio Over Time",
        "Connectivity Ratio",
        "connectivity_ratio.png"
    ),

    (
        "Runnerup_Miners",
        "Runner-Up Miners Over Time",
        "Runner-Up Miners",
        "runnerup_miners.png"
    ),

    (
        "Average_Connected_Servers",
        "Average Connected Servers Over Time",
        "Connected Servers",
        "average_connected_servers.png"
    ),

    (
        "Average_Priority",
        "Average Priority Score Over Time",
        "Priority Score",
        "priority_score.png"
    ),

    (
        "Average_Final_Score",
        "Average Final Score Over Time",
        "Final Score",
        "final_score.png"
    ),

    (
        "Success_Rate",
        "Allocation Success Rate Over Time",
        "Success Rate (%)",
        "success_rate.png"
    )

]

for column, title, ylabel, filename in graphs:

    plt.figure(figsize=(12,6))

    plt.plot(
        time_axis,
        results_df[column],
        marker='o',
        linewidth=2
    )

    plt.title(title)
    plt.xlabel("Time (sec)")
    plt.ylabel(ylabel)

    plt.grid(
        True,
        linestyle='--',
        alpha=0.7
    )

    plt.tight_layout()

    plt.savefig(
        f"Comparison_Graphs/{filename}",
        dpi=300
    )

    plt.show()

    plt.close()

print(
    "\nAdditional Result Graphs Generated Successfully"
)