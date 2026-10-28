class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            # Convert number to string to easily access each digit
            for digit in str(num):
                answer.append(int(digit))
        return answer