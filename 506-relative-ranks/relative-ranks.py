class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = [(index, value) for index, value in enumerate(score)]

        arr.sort(key=lambda x: x[1], reverse=True)

        n = len(arr)

        result = [0] * n

        for i in range(n):
            index = arr[i][0]

            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)

        return result