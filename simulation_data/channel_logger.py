import datetime

CHANNEL_LOG = "simulation_data/channel_log.txt"
ATTACK_LOG = "simulation_data/attack_simulation.txt"

def log_channel(original_qubits, measured_bits):
    with open(CHANNEL_LOG, 'a') as f:
        f.write("--- Kanal Transmisi ---\n")
        for i, ((bit, basis), meas) in enumerate(zip(original_qubits, measured_bits)):
            f.write(f"Qubit {i}: Bit={bit}, Basis={basis} => Diterima={meas}\n")
        f.write("\n")

def log_attack(eavesdropped_qubits):
    with open(ATTACK_LOG, 'a') as f:
        f.write("--- Simulasi Penyadapan ---\n")
        for i, (bit, basis) in enumerate(eavesdropped_qubits):
            f.write(f"Qubit {i}: Eve menyadap dengan Basis={basis}, Bit={bit}\n")
        f.write("\n")
