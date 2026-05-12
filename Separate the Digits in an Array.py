class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            # Convert number to string to iterate through each digit
            for digit in str(num):
                answer.append(int(digit))
        return answer