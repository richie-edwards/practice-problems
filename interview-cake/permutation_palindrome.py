# Time: O(n), where n is the number of characters in the string
# Space: O(1) since set will hold some unique number, j, of ascii/unicode


def is_perm_palindrome(str):
    """
    check if permutation of string is a palindrome
    """
    no_pair_chars = set()
    tracker = 0
    for c in str:
        if c in no_pair_chars:
            no_pair_chars.remove(c)
            tracker -= 1
        else:
            no_pair_chars.add(c)
            tracker += 1
    return (tracker == 0 or tracker == 1)


tests = ['civic', 'ivicc', 'civil', 'livci', '', ' ', 'a', ' a']

for t in tests:
    print(is_perm_palindrome(t))
