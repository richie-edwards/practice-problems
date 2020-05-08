def is_string_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_sum = 0
    s2_sum = 0

    for char in s1:
        s1_sum += ord(char)

    for char in s2:
        s2_sum += ord(char)

    return (s1_sum == s2_sum)


result = is_string_permutation("footcall", "ballfoot")
print(result)
