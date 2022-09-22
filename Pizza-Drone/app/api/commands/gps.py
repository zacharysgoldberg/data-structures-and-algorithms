from geopy.geocoders import Nominatim
from geopy import distance
import time
import mlrose_hiive as mlrose


# [Getting coordinates from address]
def get_coords_by_address(address: str):
    app = Nominatim(user_agent="pizza-drone")
    time.sleep(1)
    try:
        location = app.geocode(address)
        lon = float(location.longitude)
        lat = float(location.latitude)
        return (lat, lon)

    except:
        return get_coords_by_address(address)

# [Getting distance between two coordinates]


def get_distance_by_coords(coords1, coords2):
    miles = distance.geodesic(coords1, coords2).miles
    return miles

# [Getting distances between all coordinates]


def distances_from_coords(coords):
    Distances = []
    for index, coord in enumerate(coords):
        for x in range(0, len(coords)):
            if index != x:
                if Distances:
                    for d in Distances:
                        NotFound = False
                        if (index < d[0] or index < d[1]) and ((index == d[0] and x != d[0]) or (x == d[1] and index != d[1])):
                            NotFound = True
                            break
                    if NotFound:
                        Distance = distance.distance(
                            (coord[0], coord[1]), (coords[x][0], coords[x][1])).miles
                        Distances.append((index, x, Distance))
                else:
                    Distance = distance.distance(
                        (coord[0], coord[1]), (coords[x][0], coords[x][1])).miles
                    Distances.append((index, x, Distance))
    return Distances

# [ML algo for getting most optimal path between coordinates in miles]


def TSP(GPSS):
    dist_list = distances_from_coords(GPSS)
    print(dist_list)

    fitness_dists = mlrose.TravellingSales(distances=dist_list)
    problem_fit = mlrose.TSPOpt(length=len(
        GPSS), fitness_fn=fitness_dists, maximize=False)
    best_state, best_fitness, _ = mlrose.genetic_alg(
        problem_fit, mutation_prob=0.2, max_attempts=100, random_state=2)
    print('The best state found is: ', best_state)
    print('The fitness at the best state is: ', best_fitness)

    shortest_GPSS = []
    for b in best_state:
        shortest_GPSS.append(GPSS[b])
    # [Returning optimal path in coordinates and sequential order]
    return shortest_GPSS, best_state
