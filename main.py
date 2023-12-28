
import time

from traceRoute import main as traceRoute
from IPs_To_Locations import main as IPs_To_Locations
from animation import main as animation
'''
import geoip2.webservice
import geoip2.database
import pygeoip

import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import geopandas as gpd
from gmplot import gmplot



#test = subprocess.Popen(["ping","-W","2","-c", "1", "192.186.1.254"], stdout=subprocess.PIPE)
#output = test.communicate()[0]
#print(output)

def get_average_ping_speed(hops):
    """Calculates the average ping speed for the hops."""
    total_ping_time = 0
    number_of_hops = len(hops)
    for hop in hops:
        total_ping_time += float(hop[0])
    average_ping_speed = total_ping_time / number_of_hops
    return average_ping_speed


'''
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for sublist in data:
            line = ', '.join(map(str, sublist)) + '\n'
            file.write(line)

def read_from_file(filename):
    master_list = []

    # Assuming 'file.txt' is your text file
    with open(filename, 'r') as file:
        for line in file:
            # Remove newline characters
            line = line.strip()
        
            # Split the line into tuples
            tuples = line.split('), ')
        
            # Initialize an empty list for this line
            line_list = []
        
            for t in tuples:
                # Remove parentheses
                t = t.replace('(', '').replace(')', '')
            
                # Split the tuple into two parts
                parts = t.split(', ')
            
                # Convert parts to floats and add to line_list
                line_list.append((float(parts[0]), float(parts[1])))
        
            # Add line_list to master_list
            master_list.append(line_list)

    return master_list








def main():
    destinationIPs = [ "8.8.8.8", #Google
                      # "1.1.1.1", #Cloudflare
                       #"208.67.222.222", #OpenDNS
                       "9.9.9.9", #Quad9
                     #  "4.2.2.1", #CenturyLink
                       #"amazon.com", #Amazon
                     #  "apple.com", #Apple
                       #"chase.com", #Chase
                       #"LinkedIn.com", #LinkedIn
                     #  "Instagram.com", #Instagram
                       #"Wikipedia.org", #Wikipedia
                     # "X.com" #X
    ]
    locationsList = []
    
    for IP in destinationIPs:
    #destinationIP = "8.8.8.8"
        hops = traceRoute(IP)
        #print(hops)
        locations = IPs_To_Locations(hops)
        print(locations)
        locationsList.append(locations)
        print(locationsList)
    #save_to_file(locationsList, "RouteTracing/locationList.txt") 
    '''
    '''
    #print(locations)
    #locations = [(40.64505, -111.28162), (38.89037, -77.03196), (38.89037, -77.03196), (38.89037, -77.03196), (38.89037, -77.03196), (34.05357, -118.24545), (37.4224, -122.08421), (37.4224, -122.08421)]
    #print(read_from_file("locationList.txt"))
    #coordinates_from_file = read_from_file("RouteTracing/locationList.txt")
    #print(coordinates_from_file)
    #animation(coordinates_from_file)
    animation(locationsList)
    
 #70, -168
    #23, -61


    
if __name__ == "__main__":
  main()


#'latitude': '38.84275', 'longitude': '-77.43924'
#'ip': '192.168.1.254', 'continent_code': 'NA', 'continent_name': 'North America', 'country_code2': 'US', 'country_code3': 'USA', 'country_name': 'United States', 'country_capital': 'Washington, D.C.',
#'state_prov': 'Virginia', 'state_code': 'US-VA', 'district': '', 'city': 'Centreville', 'zipcode': '20120', 


##b' 1  dsldevice (192.168.1.254)  24.108 ms  2.739 ms  3.110 ms\n
##2  108-250-208-1.lightspeed.milwwi.sbcglobal.net (108.250.208.1)  16.648 ms  4.067 ms  4.355 ms\n
##3  76.207.192.34 (76.207.192.34)  7.993 ms  5.054 ms  4.862 ms\n 4  * * *\n
##5  32.130.91.19 (32.130.91.19)  23.896 ms  7.803 ms  6.881 ms\n
##6  12.255.10.44 (12.255.10.44)  11.521 ms\n    12.255.10.54 (12.255.10.54)  13.971 ms\n
##12.255.10.56 (12.255.10.56)  12.827 ms\n 7  * * *\n 8  dns.google (8.8.8.8)  19.954 ms  8.769 ms  8.468 ms\n
##'
##b'PING 192.186.1.254 (192.186.1.254): 56 data bytes\n\n--- 192.186.1.254 ping statistics ---\n
##1 packets transmitted, 0 packets received, 100.0% packet loss\nw'





















