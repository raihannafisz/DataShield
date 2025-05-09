import os
from datetime import datetime

LOG_DIR = "simulation_data"

def save_simulation_logs(sender_bases, receiver_bases, final_key, eavesdropped, mismatch_count):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Log channel (hasil QKD)
    with open(os.path.join(LOG_DIR, "channel_log.txt"), "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Alice Bases:     {sender_bases}\n")
        f.write(f"Bob Bases:       {receiver_bases}\n")
        f.write(f"Final Key:       {final_key}\n")
        f.write(f"Mismatch Count:  {mismatch_count}\n")

    # Log eavesdropping simulation
    with open(os.path.join(LOG_DIR, "attack_simulation.txt"), "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Eavesdropping Detected: {'Yes' if eavesdropped else 'No'}\n")
        f.write(f"Mismatch Ratio: {mismatch_count / len(sender_bases):.2f}\n")

def save_encryption_log(original_msg, encrypted_msg):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(LOG_DIR, "encryption_log.txt")
    
    with open(log_path, "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Original Message: {original_msg}\n")
        f.write(f"Encrypted Result: {encrypted_msg}\n")


def save_decryption_log(encrypted_msg, decrypted_msg):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_path = os.path.join(LOG_DIR, "decryption_log.txt")
    
    with open(log_path, "a") as f:
        f.write(f"\n[{timestamp}]\n")
        f.write(f"Encrypted Message: {encrypted_msg}\n")
        f.write(f"Decrypted Result: {decrypted_msg}\n")
