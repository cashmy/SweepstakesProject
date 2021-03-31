from sweep_queue import Queue


class SweepstakesQueueManager:

    def __init__(self):
        self.sweepstake_queue = Queue()
        pass

    def insert_sweepstakes(self, sweepstakes):
        self.sweepstake_queue.enqueue(sweepstakes)
        pass

    def get_sweepstakes(self):
        return self.sweepstake_queue.dequeue()
