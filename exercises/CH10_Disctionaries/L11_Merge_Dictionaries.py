def merge(dict1, dict2):
    merged_dictionaries = {}

    for item in dict1:
        merged_dictionaries[item] = dict1[item]
        
    for item in dict2:
        merged_dictionaries[item] = dict2[item]
    return merged_dictionaries
