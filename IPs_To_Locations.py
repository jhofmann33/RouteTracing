'''
This module will take a list of IPs and get the corresponding coordinates to each, then return that new list. 


'''
#-------------------------------------------------------------------
# Imports
#-------------------------------------------------------------------
import requests
from ignored.KeysAndSecrets import main as KeysAndSecrets
#-------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------
def get_coordinates(ip_address):
  """Gets the coordinates of the IP address."""
  url = "https://api.ipgeolocation.io/ipgeo?apiKey=" + KeysAndSecrets(1) + "&ip={}".format(ip_address)
  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    #print(data)
    return float(data["latitude"]), float(data["longitude"])
  else:
    #print("Error getting coordinates: {}".format(response.status_code))
    return None

def remove_nones(input_list):
    return [item for item in input_list if item is not None]

#-------------------------------------------------------------------
# Main
#-------------------------------------------------------------------
def main(IPList):
    coords = []
    for IP in IPList:
       coords.append(get_coordinates(IP))
       cleaned_coords = remove_nones(coords)
    return cleaned_coords    
