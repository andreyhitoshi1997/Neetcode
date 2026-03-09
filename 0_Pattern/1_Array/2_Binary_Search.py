#Tem que ser items ordenados

def binary_search(nums, target):
    low = 0
    high = len(nums)

    steps =0
    while low < high:
        steps += 1
        mid = int((low + high)/2)
        if nums[mid] == target:
            print(steps)
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid