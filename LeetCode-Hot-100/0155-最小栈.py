class MinStack:

    def __init__(self):
        self.stack = []
        self.min_heap = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        heapq.heappush(self.min_heap,value)

    def pop(self) -> None:
        x = self.stack.pop()
        self.min_heap.remove(x)
        heapq.heapify(self.min_heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_heap[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
