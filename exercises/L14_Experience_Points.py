def calculate_experience_points(level):
    xp_so_far = 0
    for i in range(0, level):
        xp_for_next_level = (level - 1) * 5
        xp_so_far += xp_for_next_level
    
    return xp_so_far // 2
