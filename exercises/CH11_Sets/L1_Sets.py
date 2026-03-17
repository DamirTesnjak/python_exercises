def remove_duplicates(spells):
    learned_spells = set()

    for spell in spells:
        learned_spells.add(spell)
    return list(learned_spells)
