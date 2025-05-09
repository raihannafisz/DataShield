# Simulasi kanal komunikasi dan serangan penyadap
import random

def apply_noise(qubits, error_rate=0.05):
    noisy_qubits = []
    for bit, base in qubits:
        if random.random() < error_rate:
            bit = 1 - bit  # flip bit
        noisy_qubits.append((bit, base))
    return noisy_qubits

def simulate_eavesdropping(qubits):
    # Eve menyadap dengan basis acak, lalu kirim ulang
    intercepted = []
    for bit, base in qubits:
        eve_basis = random.choice(['Z', 'X'])
        eve_bit = bit if base == eve_basis else random.randint(0, 1)
        intercepted.append((eve_bit, eve_basis))
    return intercepted
