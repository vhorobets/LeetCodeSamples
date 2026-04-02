class Solution(object):
    def flipAndInvertImage(self, image):
        def reverseRow(row):
            l = 0
            r = len(row) - 1
            while l < r:
                row[l], row[r] = (row[r], row[l])
                l += 1
                r -= 1
    
        for row in image:
            reverseRow(row)
            for i in range(len(row)):
                row[i] = 1 - row[i]

        return image
        