def update_stats(stats, changes):
    """Keeps track of player stats and updates player stats after a choice is made in story.
    Args:
        stats (dict[str, int]): stat name and current value.
        changes (dict[str, int]): stat names and amounts to add or subtract.
    Returns:
        dict[str, int]: updated stats.
    Side Effects:
        Changes the stat dictionary.
    """
    for stat, amount in changes.items():
        value = stats[stat] + amount
        
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
            
        stats[stat] = value
    
    return stats

"""Mock:"""
stats = {"health": 80, "hunger": 95}
changes = {"health": -20, "hunger": 10}

print(update_stats(stats, changes))