# Sinkronisasi kunci hasil QKD

def synchronize_keys(alice_key, bob_key):
    min_len = min(len(alice_key), len(bob_key))
    return alice_key[:min_len], bob_key[:min_len]
