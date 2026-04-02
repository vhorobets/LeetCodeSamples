class Solution(object):
    def flipAndInvertImage(self, image):
        def reverseRow(row):
            l = 0
            r = len(row) - 1
            while l <= r:
                row[l], row[r] = (1 - row[r], 1 - row[l])
                l += 1
                r -= 1
    
        for row in image:
            reverseRow(row)

        return image
        