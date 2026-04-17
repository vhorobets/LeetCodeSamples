class RecentCounter:

    def __init__(self):
        self.__queue = deque()
        self.__min = -3000

    def ping(self, t: int) -> int:
        self.__queue.append(t)
        self.__min = self.__queue[-1] - 3000

        while self.__queue[0] < self.__min:
            self.__queue.popleft()

        return len(self.__queue)

    
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)