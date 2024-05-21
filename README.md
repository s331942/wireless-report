# Network Performance Measurement Tool

This Python script measures the network performance by running multiple tests with `iperf3`. The tests can be configured to use either TCP or UDP protocol.

## Prerequisites

- Python 3.x
- `iperf3` installed on your system

## Usage

To run the script, use the following command:

```sh
python3 <script_name.py> <IP_iperf3_server>
```
Replace <script_name.py> with the name of your script file and <IP_iperf3_server> with the IP address of the iperf3 server you want to test against.

## Configuration
The script has a configuration option to choose between TCP and UDP modes. By default, it is set to TCP. To use UDP, change the udp variable to True.

```py
# SET THIS VALUE TO TRUE IF YOU WANT TO TEST UDP MODE
udp = False
```

## Test Execution
It runs the iperf3 test 10 times.

If udp is True, it runs iperf3 with UDP settings (-u -b 50M).
If udp is False, it runs iperf3 with the default TCP settings.
It captures the output and parses the bit rate and, if in UDP mode, the packet loss information.
Result Calculation and Display
For both TCP and UDP, it calculates and prints the maximum, minimum, mean, and standard deviation of the bit rates.
In UDP mode, it also calculates and prints the maximum, minimum, mean, and standard deviation of the packet loss percentages.

## Conclusion
This script provides a simple way to measure network performance using iperf3. By switching the udp variable, you can test both TCP and UDP protocols, allowing for versatile network performance evaluation.
