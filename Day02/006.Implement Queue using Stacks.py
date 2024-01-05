#https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []

    # x를 stack 대기열 뒤쪽 으로 푸쉬
    def push(self, x: int) -> None:
        self.stack.append(x)

    # stack의 앞부분 요소를 제거 하고 반환
    def pop(self) -> int:
        if len(self.stack) == 1:
            return self.stack.pop()

        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.pop(0))

            return self.stack.pop()

    # stack의 맨 앞 요소를 제거 하지 않고 반환
    def peek(self) -> int:
        return self.stack[0]

    # stack이 비어있으면 true, 그렇지 않으면 false
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()