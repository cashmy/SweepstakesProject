import user_interface
from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        self.sweepstakes = None


    def create_sweepstakes(self):
        name = user_interface.enter_sweepstake_name()
        new_sweepstake = Sweepstake(name)
        # This call below should work for both types of sweepstakes as the function name is the same
        self.sweepstakes.insert_sweepstakes(new_sweepstake)
        user_interface.output_text(f'Sweepstake {name} created')

    def rtv_current_sweepstake(self):
        return self.sweepstakes.rtv_sweepstakes()
