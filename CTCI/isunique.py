def is_unique(str):
    seen_char = {}
    for char in str:
        if char in seen_char:
            return False
        else:
            seen_char[char] = True
    return True
