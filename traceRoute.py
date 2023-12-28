'''
This module will take a given destination IP and enact the traceroute command to it. 
After completetion the output will be a list of IP addresses along the route.


'''
#-------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------
import subprocess
import re

#-------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------
def get_hops(command):
    """Gets the hops from the traceroute output."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    hops = []
    for line in output.decode("utf-8").splitlines():
        line = line.strip()
        if line.startswith("  "):
            match = re.search(r"(\d+\.\d+) \((\w\-)+(?: ([\w\-]+) ms)?\)", line)
            if match:
                hops.append((match.group(1), match.group(2), match.group(3)))
        else:
            if line != "* * *":
                hops.append(line)
    return hops


#-------------------------------------------------------------------
# Main
#-------------------------------------------------------------------
def main(destinationIP):
    command = ["traceroute", str(destinationIP)]
    hops = get_hops(command)
    return(hops)
