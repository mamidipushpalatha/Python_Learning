from typing import List


class ConcatenationOfArray:
    def getConcatenation1(self, nums: List[int]) -> List[int]:
        return nums+nums

    def getConcatenation2(self, nums: List[int]) -> List[int]:
        return nums *2



print(ConcatenationOfArray().getConcatenation1([1,2,3]))
print(ConcatenationOfArray().getConcatenation2([1,2,4]))



