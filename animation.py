from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import geopandas as gpd
import numpy as np
import time
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")



def interpolate_points(point1, point2, num_points):
    #print(f"point1 type: {type(point1)}, point2 type: {type(point2)}")
    lon_values = np.linspace(point1[0], point2[0], num_points)
    lat_values = np.linspace(point1[1], point2[1], num_points)
    return list(zip(lon_values, lat_values))

def update_dot(num, coordinates, dot, paths):
    if num < len(coordinates):
        lon, lat = coordinates[num]
        dot.set_data(lon, lat)
    elif paths:
        # Pause for 3 seconds at the end of a path
        plt.pause(3)
        # Reset the dot to the start of the next path
        next_path = paths.pop(0)
        coordinates.extend(next_path)
    else:
        # No more paths, stop the animation
        plt.close()
        exit
    return dot,



def main(coordinateLists):
    # Load a world map using geopandas
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    north_america = world[world['continent'] == 'North America']

    # Create a figure and axis with the world map
    fig, ax = plt.subplots()
    world.plot(ax=ax)
    #north_america.plot(ax=ax)

    # Interpolate points for all paths
    paths = []
    for coordinateList in coordinateLists:
        path = []
        for i in range(len(coordinateList) - 1):
            path.extend(interpolate_points(coordinateList[i], coordinateList[i+1], 100))
        paths.append(path)

    # Start with the first path
    coordinates = paths.pop(0)

    # Create a dot at the initial position
    initial_lon, initial_lat = coordinates[0]
    dot, = ax.plot(initial_lon, initial_lat, 'ro')  # 'ro' means red color, round marker

    # Create the animation
    ani = FuncAnimation(fig, update_dot, fargs=(coordinates, dot, paths), frames=sum(len(path) for path in [coordinates] + paths), interval=25, blit=True, repeat=False)

    plt.show()

    # Check if all paths have been traversed
    #if not paths:
        #return "done"

# Example usage:
#coordinates1 = [(-111.28162, 40.64505), (-77.03196, 38.89037), (-118.24545, 34.05357), (-122.08421, 37.4224)]
#coordinates2 = [(-80.84313, 35.22709), (-87.65005, 41.85003), (-73.56725, 45.50169), (-79.38318, 43.65323)]
#print(main([coordinates1, coordinates2]))
