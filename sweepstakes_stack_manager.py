from stack import Stack


class SweepstakesStackManager:

    def __init__(self):
        self.sweepstake_stack = Stack()
        pass

    def insert_sweepstakes(self, sweepstakes):
        self.sweepstake_stack.push(sweepstakes)
        pass

    def get_sweepstakes(self):
        return self.sweepstake_stack.pop()
