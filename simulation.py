import user_interface


class Simulation:
    def __init__(self):
        pass

    @staticmethod
    def run_simulation():
        """The central method called in main.py."""
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                pass
            elif user_option == 2:
                pass
            elif user_option == 3:
                pass
            else:
                will_proceed = False
