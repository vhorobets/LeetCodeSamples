from collections import deque

class MyQueue:

    def __init__(self):
        self.__queue = deque()

    def push(self, x: int) -> None:
        self.__queue.append(x)

    def pop(self) -> int:
        return self.__queue.popleft()

    def peek(self) -> int:
        return self.__queue[0]

    def empty(self) -> bool:
        return len(self.__queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()