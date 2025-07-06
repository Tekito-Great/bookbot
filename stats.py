def count_word(t_string):
    num = []
    num = t_string.split()
    return len(num)

def count_character(t_string):
    i = 0
    output_dict ={}
    for c in t_string:
        lowered = c.lower()
        if lowered in output_dict:
            output_dict[lowered] += 1
        else:
            output_dict[lowered] = 1
    return output_dict

def sort_dict(t_dict):
    new_dict = {}
    new_dict = sorted(t_dict.items(), key=lambda x:x[1], reverse=True)
    return new_dict