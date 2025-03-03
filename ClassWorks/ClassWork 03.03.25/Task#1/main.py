def solve(nums: list[int]) -> bool:
    from itertools import permutations

    for perm in permutations(nums):  # Проверяем все возможные порядки чисел
        if _solve(list(perm[1:]), perm[0]):
            return True
    return False


def _solve(nums: list[int], value: int) -> bool:
    if len(nums) == 0:
        return value == 23

    for i in range(len(nums)):
        sub_nums = nums[:i] + nums[i + 1:]

        if _solve(sub_nums, value + nums[i]):
            return True
        if _solve(sub_nums, value - nums[i]):
            return True
        if _solve(sub_nums, value * nums[i]):
            return True

    return False


if __name__ == '__main__':
    with open("input.txt") as f:
        for line in f:
            numbers = [int(x) for x in line.split()]
            if numbers == [0, 0, 0, 0, 0]:
                break
            print("Possible" if solve(numbers) else "Impossible")