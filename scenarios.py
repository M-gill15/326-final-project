def progression(scenario, player_choices, player_stats):
    """ Scenarios occur every turn until reaching 10 total scenarios
    
    Args:
        scenario (str): Presents an event to the player
        player_choices(str): The players selected choice (Good/Neutral/Bad)
        player_stats(dict): The players current stats
    
    Returns:
        dict[str, int]: Updates stats
    
    Side effects:
    Progresses towards finale destination
    """
    
    # 1. Event
    scenario = "\n[EVENT]\nA unicorn blocks your path on the bridge!"
    print(f"{scenario}")
    print("\n(1) Squeeze past quietly \n(2) Bribe it with food \n(3) Scare it off\n")
    player_choices = input("\n[CHOICE]\n Select your choice: ").strip
    
    # 2. Player choices  
    # Bad Choice
    if player_choices == "1":
        print("\n[OUTCOME]\n The boards beneath creak. You get kicked in the neck!\n(-20 Health)\n")
        player_stats["health"] -= 20
    # Neutral Choice
    elif player_choices == "2":
        print("\n[OUTCOME]\n The unicorn sniffs your pocket and eats your snacks. It lets you pass.\n(-5 Hunger)\n")
        player_stats["hunger"] -= 5
    # Good Choice
    elif player_choices == "3":
        print("\n[OUTCOME]\n The unicorn jumps off the bridge entirely. Watching it run into the clouds inspires you.\n(+10 to all stats)")
        player_stats["health"] += 10
        player_stats["hunger"] += 10
        player_stats["water"] += 10

    
    # 3. Turn added to travel log
    # travel_log.append(1)
    # return player_stats 