import user_interface
# from sweepstake import Sweepstake
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        if self.manager == 'stack':
            self.sweepstakes = SweepstakesStackManager()
        elif self.manager == 'queue':
            self.sweepstakes = SweepstakesQueueManager()
        else:
            self.sweepstakes = None

    def create_sweepstakes(self):
        name = user_interface.enter_sweepstake_name()
        self.sweepstakes.insert_sweepstakes(
            name)  # This should work for both types of stack as the function name is the same
        user_interface.output_text(f'Sweepstake {name} created')
