def meditate(mana, max_mana, num_potions):
    while num_potions > 0:
        if mana == max_mana:
            break
        mana += 1
        num_potions -= 1
        
    return mana, num_potions
