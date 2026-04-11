from collections import deque

class MyStack:
    def __init__(self):
        self.__queue = deque()

    def push(self, x: int) -> None:
        self.__queue.append(x)
        for i in range(len(self.__queue) - 1):
            first = self.__queue.popleft()
            self.__queue.append(first)

    def pop(self) -> int:
        return  self.__queue.popleft()

    def top(self) -> int:
        return  self.__queue[0]

    def empty(self) -> bool:
        return len(self.__queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()