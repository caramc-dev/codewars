# Binary search problem

a = [-3, -1, 0, 1, 4, 7]

# O(n) searching
if -1 in a:
    print(True)


# Traditional binary search - Look up if a number is in an array
# Time: O(log n)
# Space: O(1)


def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        # m = (left + right) // 2
        m = left + ((right - left) // 2)

        if arr[m] == target:
            return True
        elif target < arr[m]:
            right = m - 1
        else:
            left = m + 1

    return False


print(binary_search(a, 7))

