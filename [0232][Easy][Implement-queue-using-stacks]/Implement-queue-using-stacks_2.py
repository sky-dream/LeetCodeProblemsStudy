class MyQueue:

    def __init__(self):
        self.input, self.output = [], []

    def push(self, x: int):
        """
        Push element x to the back of queue.
        """
        while self.output:
            self.input.append(self.output.pop())
        self.input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self):
        """
        Get the front element.
        """
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        while self.input:
            self.output.append(self.input.pop())
        return not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
