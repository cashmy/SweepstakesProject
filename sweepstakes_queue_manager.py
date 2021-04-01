from sweep_queue import Queue


class SweepstakesQueueManager:

    def __init__(self):
        self.sweepstake_queue = Queue()

    def __len__(self):
        return len(self.sweepstake_queue)

    def insert_sweepstakes(self, sweepstake):
        self.sweepstake_queue.enqueue(sweepstake)

    def get_sweepstakes(self):
        return self.sweepstake_queue.dequeue()

    def rtv_sweepstakes(self):
        sweepstake = self.sweepstake_queue.dequeue()
        self.sweepstake_queue.enqueue(sweepstake)
        return sweepstake
