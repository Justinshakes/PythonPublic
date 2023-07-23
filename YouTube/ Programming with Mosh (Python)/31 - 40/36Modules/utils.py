def find_max(nums):
    maximum = nums[0]

    for number in nums:
        if number > maximum:
            maximum = number
    return maximum
