from typing import List


class ShuffleArrayPrb:
    # Example
    # Input: nums = [1, 1, 2, 2], n = 2
    # Output: [1, 2, 1, 2]

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result=[]
        for i in range(n):
            # result.append(nums[i])
            # result.append((nums[i+n]))
            result.extend([nums[i], nums[i+n]])
        return result

    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        return [nums[i + (j % 2) * n] for i in range(n) for j in range(2)]

    def understandTheFormula(self, n: int):
        for i in range(n):
            for j in range(2):
                print(f" when i = {i} and j= {j} then {i} + ({j} % 2) * {n} => {i + (j % 2) * n}")


print(ShuffleArrayPrb().shuffle([1,1,2,2],2))
print(ShuffleArrayPrb().shuffle([2,5,1,3,4,7],3))
print(ShuffleArrayPrb().shuffle2([1,1,2,2],2))






