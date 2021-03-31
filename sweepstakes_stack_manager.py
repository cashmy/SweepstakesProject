from stack import Stack


class SweepstakesStackManager:

    def __init__(self):
        self.sweepstake_stack = Stack()
        pass

    def insert_sweepstakes(self, sweepstake):
        self.sweepstake_stack.push(sweepstake)
        pass

    def get_sweepstakes(self):
        return self.sweepstake_stack.pop()
