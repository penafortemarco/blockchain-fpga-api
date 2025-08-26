#!/bin/bash

echo "Starting virtual ports with socat ---------------------------------------"

# Running Socat
exec 3< <(socat -d -d pty,raw,echo=0 pty,raw,echo=0 2>&1)
SOCAT_PID=$!

sleep 1
PORTS=($(grep -oPm2 '/dev/pts/\d+' <&3))

# Check if the array contains exactly two ports
if [ "${#PORTS[@]}" -ne 2 ]; then
    echo "Error: Could not determine socat port names. Exiting..."
    kill $SOC_PID &>/dev/null
    exit 1
fi

# Assign ports from the array
PORT1=${PORTS[0]}
PORT2=${PORTS[1]}

echo "Virtual ports created: $PORT1 <--> $PORT2"
echo ""

# Running Test
echo "Starting Mock FPGA in the background ------------------------------------"
python3 -m src.mock_test "$PORT1"
FPGA_PID=$!

#echo "Running Main Test Program -----------------------------------------------"
#python3 main.py "$PORT2"

# Exiting
echo "Test finished. Cleaning up background processes. ------------------------"
kill $FPGA_PID
kill $SOCAT_PID

echo "Done!"