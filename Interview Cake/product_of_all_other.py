# Time: O(n) stemming from O(2n); Space: O(n)
def product_of_all_other(nums):
    """
    A method that takes a list of integers and
    returns a list where each original index holds
    the product of all numbers in the list except for the
    number at the corresponding index.
    Ex: input: [3, 7, 1, 4], output: [28, 12, 84, 21]
    """
    result = [None] * len(nums)
    curr_prod = 1
    for i in range(len(nums)):
        result[i] = curr_prod
        curr_prod *= nums[i]

    curr_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= curr_prod
        curr_prod *= nums[i]

    return result


test = [5, 3, 1, 7]
expected = [21, 35, 105, 15]
print(product_of_all_other(test), f"expected: {expected}")
