# Time: O(log(n)) where n is number of words in list;
# we compare words using <> so O(l * log(n)) where l is length of word
# Space: O(1) to store some needed variables


def get_rotation_point(words):
    list_length = len(words)
    if list_length < 2:
        return ValueError("no pivot point")

    start_index = 0
    end_index = list_length - 1

    while (end_index - start_index) > 1:
        mid_index = (start_index + end_index) // 2
        start_word = words[start_index]
        mid_word = words[mid_index]
        end_word = words[end_index]
        min_word = min(start_word, mid_word, end_word)

        if min_word == end_word:
            start_index = mid_index
        elif min_word == start_word:
            end_index = mid_index
        elif min_word == mid_word:
            if words[mid_index - 1] < words[mid_index + 1]:
                end_index = mid_index
            else:
                start_index = mid_index

    if words[start_index] < words[end_index]:
        return start_index
    else:
        return end_index
