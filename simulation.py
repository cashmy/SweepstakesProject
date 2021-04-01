import user_interface
from marketing_firm_creator import MarketingFirmCreator
from contestant import Contestant


class Simulation:
    def __init__(self):
        self.new_marketing_firm = None
        self.current_sweepstake = None

    def run_simulation(self):
        check = user_interface.display_welcome()
        if check:
            firm_creator = MarketingFirmCreator()
            self.new_marketing_firm = firm_creator.create_firm_menu()
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
                self.current_sweepstake = self.new_marketing_firm.sweepstakes.rtv_sweepstakes()
            elif user_option == 2:
                if self.current_sweepstake is None:
                    user_interface.require_sweepstakes_error()
                else:
                    # Add a contestant - This separation of "Adding" and "Registering"
                    #     allows for Dependency Injection
                    contestant = self.standard_contestant(self.current_sweepstake)
                    # Now register a contestant -
                    self.current_sweepstake.register_contestant(contestant)
                    self.current_sweepstake.print_sweepstake_status()
            elif user_option == 3:
                if self.current_sweepstake is None:
                    user_interface.require_sweepstakes_error()
                else:
                    self.current_sweepstake.print_contestants()
            elif user_option == 4:
                if self.current_sweepstake is None:
                    user_interface.require_sweepstakes_error()
                else:
                    # Pick a winner and notify contestants
                    contestant = self.current_sweepstake.pick_winner()
                    self.current_sweepstake.notify_all_contestants(contestant)
            elif user_option == 5:
                if len(self.new_marketing_firm.sweepstakes) > 0:
                    sweepstake = self.new_marketing_firm.sweepstakes.get_sweepstakes()
                    user_interface.output_text(f'\nSweepstake {sweepstake.name} has been removed.')
                else:
                    user_interface.output_text('Nothing to remove')
                # Now update with next available sweepstake
                if len(self.new_marketing_firm.sweepstakes) > 0:
                    self.current_sweepstake = self.new_marketing_firm.sweepstakes.rtv_sweepstakes()
            elif user_option == 6:
                user_interface.output_text('Goodbye.')
                return
            else:
                will_proceed = False

    @staticmethod
    def standard_contestant(sweepstake):
        registration_number = sweepstake.next_available_registration_number()
        first_name, last_name, email = user_interface.get_contestant_info()
        return Contestant(first_name, last_name, email, registration_number)
