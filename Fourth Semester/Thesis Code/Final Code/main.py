# =========================================================
# PROOF OF WORK (PoW) CONSENSUS
# FOR CDAM & MDAM
# =========================================================

import hashlib
import time
import numpy as np

# =========================================================
# BLOCK CLASS
# =========================================================

class Block:

    def __init__(

        self,
        index,
        timestamp,
        data,
        previous_hash

    ):

        self.index = index

        self.timestamp = timestamp

        self.data = data

        self.previous_hash = previous_hash

        self.nonce = 0

        self.hash = self.calculate_hash()

    # =====================================================
    # HASH FUNCTION
    # =====================================================

    def calculate_hash(self):

        block_string = (

            str(self.index) +

            str(self.timestamp) +

            str(self.data) +

            str(self.previous_hash) +

            str(self.nonce)

        )

        return hashlib.sha256(

            block_string.encode()

        ).hexdigest()

# =========================================================
# PROOF OF WORK FUNCTION
# =========================================================

def proof_of_work(

    block,
    difficulty

):

    target = "0" * difficulty

    start_time = time.time()

    while (

        block.hash[:difficulty] != target

    ):

        block.nonce += 1

        block.hash = block.calculate_hash()

    mining_time = (

        time.time() - start_time

    )

    return (

        block.hash,
        block.nonce,
        mining_time

    )

# =========================================================
# BLOCKCHAIN
# =========================================================

blockchain = []

# =========================================================
# GENESIS BLOCK
# =========================================================

genesis_block = Block(

    0,
    time.time(),
    "Genesis Block",
    "0"

)

blockchain.append(genesis_block)

# =========================================================
# PoW PARAMETERS
# =========================================================

difficulty = 4

# =========================================================
# STORE PoW RESULTS
# =========================================================

pow_mining_time_history = []

pow_nonce_history = []

pow_hashrate_history = []

pow_success_history = []

# =========================================================
# START PoW CONSENSUS
# =========================================================

print("\n====================================")
print("STARTING PoW CONSENSUS")
print("====================================")

for round_num in range(TOTAL_ROUNDS):

    current_time = (
        round_num + 1
    ) * UPDATE_INTERVAL

    print("\n====================================")
    print(f"TIME STEP: {current_time} sec")
    print("====================================")

    # =====================================================
    # PREVIOUS BLOCK
    # =====================================================

    previous_block = blockchain[-1]

    # =====================================================
    # CREATE NEW BLOCK
    # =====================================================

    block_data = {

        "Connected_Miners": connected_miners_history[round_num],

        "CDAM_Winners": cdam_winner_history[round_num],

        "MDAM_Winners": mdam_winner_history[round_num],

        "CDAM_Social_Welfare":

            cdam_social_welfare_history[round_num],

        "MDAM_Social_Welfare":

            mdam_social_welfare_history[round_num]

    }

    new_block = Block(

        round_num + 1,

        time.time(),

        block_data,

        previous_block.hash

    )

    # =====================================================
    # RUN PoW
    # =====================================================

    (
        mined_hash,
        nonce,
        mining_time

    ) = proof_of_work(

        new_block,
        difficulty

    )

    # =====================================================
    # ADD BLOCK TO BLOCKCHAIN
    # =====================================================

    blockchain.append(new_block)

    # =====================================================
    # HASHRATE
    # =====================================================

    hashrate = nonce / (

        mining_time + 0.0001

    )

    # =====================================================
    # SUCCESS
    # =====================================================

    success = 1

    # =====================================================
    # STORE RESULTS
    # =====================================================

    pow_mining_time_history.append(
        mining_time
    )

    pow_nonce_history.append(
        nonce
    )

    pow_hashrate_history.append(
        hashrate
    )

    pow_success_history.append(
        success
    )

    # =====================================================
    # PRINT RESULTS
    # =====================================================

    print(
        f"Block Index: {new_block.index}"
    )

    print(
        f"Nonce: {nonce}"
    )

    print(
        f"Hash: {mined_hash}"
    )

    print(
        f"Mining Time: {round(mining_time, 4)} sec"
    )

    print(
        f"Hashrate: {round(hashrate, 2)}"
    )

# =========================================================
# SAVE PoW METRICS
# =========================================================

pow_df = pd.DataFrame({

    "Time": time_history,

    "Mining_Time": pow_mining_time_history,

    "Nonce": pow_nonce_history,

    "Hashrate": pow_hashrate_history,

    "Consensus_Success": pow_success_history

})

pow_df.to_csv(

    "pow_metrics.csv",

    index=False

)

# =========================================================
# PoW GRAPH FUNCTION
# =========================================================

def draw_pow_graph(

    y,
    ylabel,
    title,
    filename

):

    plt.figure(figsize=(10, 6))

    plt.plot(

        time_history,
        y,
        marker='o',
        linewidth=2

    )

    plt.xlabel("Time (seconds)")

    plt.ylabel(ylabel)

    plt.title(title)

    plt.grid(True)

    plt.savefig(

        f"Graphs/{filename}"

    )

    plt.close()

# =========================================================
# DRAW PoW GRAPHS
# =========================================================

draw_pow_graph(

    pow_mining_time_history,
    "Mining Time (sec)",
    "PoW Mining Time vs Time",
    "pow_mining_time.png"

)

draw_pow_graph(

    pow_nonce_history,
    "Nonce",
    "PoW Nonce vs Time",
    "pow_nonce.png"

)

draw_pow_graph(

    pow_hashrate_history,
    "Hashrate",
    "PoW Hashrate vs Time",
    "pow_hashrate.png"

)

# =========================================================
# FINAL PoW RESULTS
# =========================================================

print("\n====================================")
print("PoW FINAL RESULTS")
print("====================================")

print(
    "Average Mining Time:",
    round(np.mean(pow_mining_time_history), 4)
)

print(
    "Average Nonce:",
    round(np.mean(pow_nonce_history), 2)
)

print(
    "Average Hashrate:",
    round(np.mean(pow_hashrate_history), 2)
)

print("\n====================================")
print("PoW CONSENSUS COMPLETED")
print("====================================")