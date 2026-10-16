class MyQueue:
    def __init__(self):
        self.s_in = []
        self.s_out = []

    def push(self, x: int) -> None:
        self.s_in.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s_out.pop()

    def peek(self) -> int:
        if not self.s_out:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
        return self.s_out[-1]

    def empty(self) -> bool:
        return not self.s_in and not self.s_out

   