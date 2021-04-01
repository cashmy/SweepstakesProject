import user_interface
from marketing_firm import MarketingFirm
from sweepstakes_stack_manager import SweepstakesStackManager
from sweepstakes_queue_manager import SweepstakesQueueManager


class MarketingFirmCreator:

    def __init__(self):
        pass

    # This menu will allow the user to select a type of sweepstakes manager object: Queue or Stack
    # This in turn, will allow for Dependency Injection in the 'create_firm' method
    def create_firm_menu(self):
        manager = self.assign_manager()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.sweeps_type_menu()
            if user_option == 1:  # Create a stack
                stack_type_obj = SweepstakesStackManager()
                marketing_firm = self.create_firm(manager, stack_type_obj, 'Stack')
            elif user_option == 2:  # Create a Queue
                stack_type_obj = SweepstakesQueueManager()
                marketing_firm = self.create_firm(manager, stack_type_obj, 'Queue')
            elif user_option == 3:
                quit(0)
                return
            will_proceed = False
        else:
            pass
        return marketing_firm

    @staticmethod
    def assign_manager():
        manager = user_interface.get_manager_name()
        return manager

    # This method takes a manager_type_obj variable for Dependency Injection assignment.
    @staticmethod
    def create_firm(manager, manager_type_obj, obj_desc):
        marketing_firm = MarketingFirm(manager)
        marketing_firm.sweepstakes = manager_type_obj
        user_interface.output_text(f'\n {obj_desc} created.')
        return marketing_firm
