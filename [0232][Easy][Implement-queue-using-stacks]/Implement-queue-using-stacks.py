class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []

    def push(self, x: int):
        """
        Push element x to the back of queue.
        """
        self.stackin.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout.pop()

    def peek(self):
        """
        Get the front element.
        """
        if not self.stackout:
            while self.stackin:
                a = self.stackin.pop()
                self.stackout.append(a)
        return self.stackout[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if not self.stackin and not self.stackout:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
