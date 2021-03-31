import user_interface
from marketing_firm import MarketingFirm


class MarketingFirmCreator:

    def __init__(self):
        pass

    @staticmethod
    def choose_manager():
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:  # Create a stack
                manager_type = 'stack'
            elif user_option == 2:  # Create a Queue
                manager_type = 'queue'
            elif user_option == 3:
                return
            will_proceed = False
        else:
            pass
        marketing_firm = MarketingFirm(manager_type)
        return marketing_firm
