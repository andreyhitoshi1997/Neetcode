def binary_search(nums, target):
    low = 0 
    hi = len(nums)
    steps = 0

    while lo < hi:
        steps += 1
        mid = int((lo+hi) /2)

        if nums[mid] == target:
            print("step: ", steps)
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            hi = mid
    return -1