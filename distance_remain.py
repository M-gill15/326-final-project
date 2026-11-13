def distance_remaining(travel_log, target_distance):
    """
    Calculates the distance remaining until the player reaches their final
    destination.
    
    Args: 
        travel_log (list): A list containing the distances traveled during
        each aprt of the journey.
        target_distance (int/float): The total distance to the player's final
        destination.
        
    Returns:
        int/float: The distance remaining until the player reaches their final
        destination
        
    """
    distance_traveled = 0
    
    for distance in travel_log:
        distance_traveled += distance
        
    distance_remaining = target_distance - distance_traveled
    
    if distance_remaining < 0:
        distance_remaining = 0
    
    return distance_remaining

# test
# travel_log = [8, 12, 5, 10]
# target_distance = 50

# unit can be decided later
# remaining = distance_remaining(travel_log, target_distance)
# print(remaining)