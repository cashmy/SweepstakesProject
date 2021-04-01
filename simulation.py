import user_interface
from marketing_firm_creator import MarketingFirmCreator



class Simulation:
    def __init__(self):
        self.new_marketing_firm = None

    def run_simulation(self):
        check = user_interface.display_welcome()
        if check:
            new_marketing_firm_manager = MarketingFirmCreator()
            self.new_marketing_firm = new_marketing_firm_manager.choose_manager()
            self.simulation_menu()
        else:
            return

    def simulation_menu(self):
        """The central method called in main.py."""
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                self.new_marketing_firm.create_sweepstakes()
            elif user_option == 2:
                sweepstake = self.new_marketing_firm.sweepstakes.rtv_sweepstakes()
                # sweepstake = self.new_marketing_firm.rtv_current_sweepstake()
                sweepstake.print_sweepstake_status()
            elif user_option == 3:
                pass
            elif user_option == 4:
                sweepstake = self.new_marketing_firm.sweepstakes.get_sweepstakes()
                user_interface.output_text(f'\nSweepstake {sweepstake.name} has been removed.')
            elif user_option == 5:
                user_interface.output_text('Goodbye.')
                return
            else:
                will_proceed = False
