#https://leetcode.com/problems/implement-stack-using-queues/
#
#두 개의 대기열만 사용하여 LIFO(후입선출) 스택을 구현합니다. push구현된 스택은 일반 스택( , top, pop및 ) 의 모든 기능을 지원해야 합니다 empty.
# 클래스를 구현합니다 MyStack.
#
# void push(int x)요소 x를 스택의 맨 위로 푸시합니다.
# int pop()스택 맨 위에 있는 요소를 제거하고 반환합니다.
# int top()스택의 맨 위에 있는 요소를 반환합니다.
# boolean empty()true스택이 비어 있으면 반환하고 , false그렇지 않으면 반환합니다.
#
# 노트:
# 대기열의 표준 작업 만 사용해야 합니다 . 즉 push to back, peek/pop from front, size및 is empty작업만 유효합니다.
# 언어에 따라 대기열이 기본적으로 지원되지 않을 수 있습니다. 대기열의 표준 작업만 사용하는 한 목록 또는 deque(양단 대기열)를 사용하여 대기열을 시뮬레이션할 수 있습니다.
#
#
# 예시 1:
# 입력
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# 산출
# [널, 널, 널, 2, 2, 거짓]
#
# 설명
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // 2를 반환
# myStack.pop(); // 2를 반환
# myStack.empty(); // 거짓을 반환
#
#
# 제약:
# 1 <= x <= 9
# 대부분의 호출은 , , 및 100으로 이루어집니다 .pushpoptopempty
# pop및 에 대한 모든 호출이 top유효합니다.
#
#
# 후속 조치: 하나의 대기열만 사용하여 스택을 구현할 수 있습니까?

class MyStack:
    def __init__(self):
        self.q = []

    # x를 q의 맨 앞으로 push
    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

    # q의 맨 앞 요소를 제거 하고 반환
    def pop(self) -> int:
        return self.q.pop(0)

    # q의 맨 앞 요소를 제거 하지 않고 반환
    def top(self) -> int:
        return self.q[0]

    # q가 비어 있으면 true, 아닐 경우 false
    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()