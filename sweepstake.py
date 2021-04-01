import user_interface
from contestant import Contestant
import random


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestants = []

    # Original method:
    # This method is NOT a dependency injection design pattern
    def register_contestant_non_hd_lc(self, first_name, last_name, email):
        registration_number = len(self.contestants)+1
        self.contestants.append(Contestant(first_name, last_name, email, registration_number))

    # Method that uses Dependency Injection
    # Contestant object will have been already created
    def register_contestant(self, contestant_obj):
        try:
            self.contestants.append(contestant_obj)
        except AttributeError as error:
            user_interface.output_text("Contest doesn't have a notify method - not added")
            user_interface.output_text(error)  # TODO: Change this to output to a logging module.

    def next_available_registration_number(self):
        return len(self.contestants) + 1

    def print_sweepstake_status(self):
        user_interface.output_text(f'\nSweepstake {self.name} currently has {len(self.contestants)} contestants.')

    def pick_winner(self):
        winner_index = random.randint(0, len(self.contestants) - 1)
        winner = self.contestants[winner_index]
        winner.winner_status = True
        user_interface.output_text(f'The winner for {self.name} is '
                                   f'{winner.first_name} {winner.last_name}')
        return winner  # contestant

    def print_contestants(self):
        user_interface.output_text('\n\t\t***Contestant List ***')
        for contestant in self.contestants:
            user_interface.output_text(f'Name: {contestant.first_name} {contestant.last_name} '
                                       f'Email: {contestant.email} '
                                       f'Registration Number: {contestant.registration_number} ')
        return

    def notify_all_contestants(self, winning_contestant):
        for contestant in self.contestants:
            if contestant == winning_contestant:
                contestant.notify(True)
            else:
                contestant.notify(False)
