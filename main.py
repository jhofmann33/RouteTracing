'''
This is the main launcher file. Running this file will call all the pieces in the correct order.
(AKA only run this one)

You can comment out the generateNewRoutes() function from main to reuse a previously generated one to save time.
Generally that will be for debugging.

'''

#-------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------
from traceRoute import main as traceRoute
from IPs_To_Locations import main as IPs_To_Locations
from animation import main as animation


#-------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for sublist in data:
            line = ', '.join(map(str, sublist)) + '\n'
            file.write(line)

def read_from_file(filename):
    master_list = []
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

def generateNewRoutes():
    destinationIPs = [ "8.8.8.8", #Google
                        "1.1.1.1", #Cloudflare
                        #"208.67.222.222", #OpenDNS (slow)
                        "9.9.9.9", #Quad9
                        "4.2.2.1", #CenturyLink
                        #"amazon.com", #Amazon (slow)
                        "apple.com", #Apple
                        #"chase.com", #Chase (slow)
                        #"LinkedIn.com", #LinkedIn (slow)
                        "Instagram.com", #Instagram
                        "Wikipedia.org", #Wikipedia
                        "X.com" #X
    ]
    locationsList = []
    for IP in destinationIPs:
    #destinationIP = "8.8.8.8"
        hops = traceRoute(IP)
        #print(hops)
        locations = IPs_To_Locations(hops)
        #print(locations)
        locationsList.append(locations)
        #print(locationsList)
    save_to_file(locationsList, "RouteTracing/locationList.txt") 


#-------------------------------------------------------------------
# Main
#-------------------------------------------------------------------
def main():
    generateNewRoutes()
    coordinates_from_file = read_from_file("RouteTracing/locationList.txt")
    animation(coordinates_from_file)
    


# Will init main  (dont touch)  
if __name__ == "__main__":
  main()



