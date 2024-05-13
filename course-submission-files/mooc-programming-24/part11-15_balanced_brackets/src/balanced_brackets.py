
def balanced_brackets(my_string: str, is_filtered: bool = False):
    if not is_filtered:
        brackets = "([])"
        filtered = ""
        for char in my_string:
            filtered += char if char in brackets else ""
    else: 
        filtered = my_string

    if len(filtered) == 0:
        return True
    
    open_round = filtered[0] == '('
    closed_round = filtered[-1] == ")"
    open_square = filtered[0] == "["
    closed_square = filtered[-1] == "]"
    
    if not (open_round and closed_round) and not (open_square and closed_square):
        return False        
    
    return balanced_brackets(filtered[1:-1], is_filtered=True)