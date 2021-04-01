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
                self.current_sweepstake = self.new_marketing_firm.sweepstakes.rtv_sweepstakes()
            elif user_option == 2:
                if self.current_sweepstake is not None:
                    contestant = self.standard_contestant(self.current_sweepstake)
                    self.current_sweepstake.register_contestant(contestant)
                    self.current_sweepstake.print_sweepstake_status()
                else:
                    user_interface.output_text('You must create a sweepstake first.')
            elif user_option == 3:
                if self.current_sweepstake is not None:
                    # Pick a winner and notify contestants
                    contestant = self.current_sweepstake.pick_winner()
                    user_interface.output_text(f'The winner for {self.current_sweepstake.name} is '
                                               f'{contestant.first_name} {contestant.last_name}')
                else:
                    user_interface.output_text('You must create a sweepstake first.')
            elif user_option == 4:
                sweepstake = self.new_marketing_firm.sweepstakes.get_sweepstakes()
                user_interface.output_text(f'\nSweepstake {sweepstake.name} has been removed.')
                # Now update with next available sweepstake
                if len(self.new_marketing_firm.sweepstakes) > 0:
                    self.current_sweepstake = self.new_marketing_firm.sweepstakes.rtv_sweepstakes()
            elif user_option == 5:
                user_interface.output_text('Goodbye.')
                return
            else:
                will_proceed = False

    @staticmethod
    def standard_contestant(sweepstake):
        registration_number = sweepstake.next_available_registration_number()
        first_name, last_name, email = user_interface.get_contestant_info()
        return Contestant(first_name, last_name, email, registration_number)
