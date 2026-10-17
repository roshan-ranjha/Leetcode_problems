
def digit_sum(number):
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def minimum_swaps(nums):
    # Step 1: Sort by digit sum, then by number
    sorted_nums = sorted(nums, key=lambda number: (digit_sum(number), number))

    # Step 2: Store each number's correct index
    correct_index = {}

    for index in range(len(sorted_nums)):
        correct_index[sorted_nums[index]] = index

    # Step 3: Track visited positions
    visited = [False] * len(nums)
    swaps = 0

    # Step 4: Find cycles and count minimum swaps
    for i in range(len(nums)):

        # Skip positions already visited or already correct
        if visited[i] or correct_index[nums[i]] == i:
            continue

        cycle_size = 0
        current = i

        while not visited[current]:
            visited[current] = True
            current = correct_index[nums[current]]
            cycle_size += 1

        # A cycle of k elements needs k - 1 swaps
        swaps += cycle_size - 1

    return swaps


if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

    result = minimum_swaps(nums)

    print("Minimum swaps required:", result)
