# Simulasi pembangkitan kunci kuantum (BB84)
import random
from .config import BB84_BASES, KEY_LENGTH
import os
from datetime import datetime
from .log_writer import save_simulation_logs

def simulate_qkd():
    alice_bits = generate_random_bits(KEY_LENGTH)
    alice_bases = generate_random_bases(KEY_LENGTH)
    qubits = encode_qubits(alice_bits, alice_bases)

    bob_bases = generate_random_bases(KEY_LENGTH)
    bob_results = measure_qubits(qubits, bob_bases)

    key = sift_keys(alice_bases, bob_bases, bob_results)

    # Simulasi deteksi penyadapan
    mismatches = sum(1 for a, b in zip(alice_bases, bob_bases) if a != b)
    eavesdropped = mismatches > (len(alice_bases) * 0.2)

    # Simpan log
    save_simulation_logs(alice_bases, bob_bases, key, eavesdropped, mismatches)

    return key


def save_simulation_logs(alice_bases, bob_bases, sifted_key, eavesdropped=False, mismatches=0):
    log_dir = "simulation_data"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Channel log
    with open(os.path.join(log_dir, "channel_log.txt"), "w") as f:
        f.write("=== Quantum Channel Log ===\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Bit Length: {len(alice_bases)}\n")
        f.write(f"Alice Bases: {' '.join(alice_bases)}\n")
        f.write(f"Bob Bases:   {' '.join(bob_bases)}\n")
        f.write(f"Sifted Key:  {' '.join(str(b) for b in sifted_key)}\n")
        f.write(f"Key Agreement Success Rate: {int(100 * len(sifted_key)/len(alice_bases))}%\n")
        f.write(f"Noise Detected: {'Yes' if eavesdropped else 'Low'}\n")
        f.write(f"Status: {'Not Secure' if eavesdropped else 'Secure'}\n")

    # Attack simulation log
    with open(os.path.join(log_dir, "attack_simulation.txt"), "w") as f:
        f.write("=== Attack Simulation Log ===\n")
        f.write(f"Timestamp: {timestamp}\n")
        f.write(f"Type: Intercept-Resend Attack\n")
        f.write(f"Attacker: Eve\n")
        f.write(f"Qubits Intercepted: {len(alice_bases)}\n")
        f.write(f"Detected mismatches in basis: {mismatches}\n")
        f.write(f"Key mismatch rate: {int(100 * mismatches / len(alice_bases))}%\n")
        f.write(f"Conclusion: {'Key exchange was not secure due to presence of eavesdropping.' if eavesdropped else 'Key exchange appears secure.'}\n")


def generate_random_bits(length):
    return [random.randint(0, 1) for _ in range(length)]

def generate_random_bases(length):
    return [random.choice(BB84_BASES) for _ in range(length)]

def encode_qubits(bits, bases):
    return list(zip(bits, bases))  # Representasi qubit sederhana

def measure_qubits(qubits, measurement_bases):
    return [bit if base == meas else random.randint(0, 1)
            for (bit, base), meas in zip(qubits, measurement_bases)]

def sift_keys(sender_bases, receiver_bases, bits):
    return [bit for b1, b2, bit in zip(sender_bases, receiver_bases, bits) if b1 == b2]



def simulate_qkd():
    alice_bits = generate_random_bits(KEY_LENGTH)
    alice_bases = generate_random_bases(KEY_LENGTH)
    qubits = encode_qubits(alice_bits, alice_bases)

    bob_bases = generate_random_bases(KEY_LENGTH)
    bob_results = measure_qubits(qubits, bob_bases)

    key = sift_keys(alice_bases, bob_bases, bob_results)

    # Simulasi eavesdropping (acak, 30% basis mismatch)
    mismatches = sum([1 for a, b in zip(alice_bases, bob_bases) if a != b])
    eavesdropped = mismatches > (len(alice_bases) * 0.2)

    # Simpan log
    save_simulation_logs(alice_bases, bob_bases, key, eavesdropped, mismatches)

    return key

