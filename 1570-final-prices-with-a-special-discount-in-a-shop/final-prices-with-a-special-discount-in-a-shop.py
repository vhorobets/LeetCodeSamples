class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        i = 0
        while i < n:
            j = i + 1

            while j < n:
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
                j += 1

            i += 1

        return prices

        