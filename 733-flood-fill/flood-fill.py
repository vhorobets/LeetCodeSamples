class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] != color:
            self.__fill_internal(image, sr, sc, color, image[sr][sc])

        return image

    def __fill_internal(self, image: List[List[int]], sr: int, sc: int, color: int, original: int):
        if sr < 0 or sr >= len(image):
            return

        if sc < 0 or sc >= len(image[sr]):
            return

        if image[sr][sc] != original:
            return

        image[sr][sc] = color

        self.__fill_internal(image, sr + 1, sc, color, original)
        self.__fill_internal(image, sr - 1, sc, color, original)
        self.__fill_internal(image, sr, sc + 1, color, original)
        self.__fill_internal(image, sr, sc - 1, color, original)