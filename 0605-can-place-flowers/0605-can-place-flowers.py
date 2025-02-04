class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # To track the number of flowers we can plant
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:  # If we have planted enough flowers, return True early
                        return True
                
        return count >= n  # Check if we managed to plant `n` flowers
