from stack import Stack


class SweepstakesStackManager:

    def __init__(self):
        self.sweepstake_stack = Stack()

    def __len__(self):
        return len(self.sweepstake_stack)

    def insert_sweepstakes(self, sweepstake):
        self.sweepstake_stack.push(sweepstake)

    def get_sweepstakes(self):
        return self.sweepstake_stack.pop()

    def rtv_sweepstakes(self):
        sweepstake = self.sweepstake_stack.pop()
        self.sweepstake_stack.push(sweepstake)
        return sweepstake