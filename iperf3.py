import subprocess
import sys
import math

# SET THIS VALUE TO TRUE IF YOU WANT TO TEST UDP MODE
udp = False

def avg(values):
    return sum(values) / len(values)

def std(values):
    average = avg(values)
    return math.sqrt(sum([((value - average) ** 2) for value in values]) / (len(values) - 1))

def help():
    print("Usage:")
    print(f"python3 {sys.argv[0]} <IP_iperf3_server>")

if len(sys.argv) != 2:
    help()
    exit()

host = sys.argv[1]

bit_rates = []
misses = []

for i in range(10):
    if udp:
        cmd = ["iperf3", "-c", host, "-u", "-b", "50M"]
    else:
        cmd = ["iperf3", "-c", host]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    start_idx = 0
    for idx, line in enumerate(output):
        if line.startswith('- - - - - - - - - - - - - - - - - - - - - - - - -'):
            start_idx = idx + 2
            break

    sender_line = output[start_idx].strip()
    receiver_line = output[start_idx + 1].strip()

    print(sender_line)
    print(receiver_line)

    s = receiver_line.split()
    start_time, end_time = s[2].split("-")
    transfer_bytes = s[4]
    bit_rate = float(s[6])
    
    if udp:
        miss = float(eval(s[10]) * 100)
        misses.append(round(miss, 2))

    print(f"bit rate: {bit_rate}")
    bit_rates.append(bit_rate)

if udp:
    max_misses = max(misses)
    min_misses = min(misses)
    mean_misses = avg(misses)
    std_misses = std(misses)
    print(misses)
    print(f"max misses: {max_misses:.2f}%")
    print(f"min misses: {min_misses:.2f}%")
    print(f"mean misses: {mean_misses:.2f}%")
    print(f"std misses: {std_misses:.2f}%")

max_br = max(bit_rates)
min_br = min(bit_rates)
mean_br = avg(bit_rates)
std_br = std(bit_rates)
print(bit_rates)
print(f"max bit rate: {max_br}")
print(f"min bit rate: {min_br}")
print(f"mean bit rate: {mean_br:.2f}")
print(f"std bit rate: {std_br:.2f}")
