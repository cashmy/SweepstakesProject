from contestant import Contestant
import random


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestants = []

    def register_contestant(self, first_name, last_name, email):
        registration_number = len(self.contestants)+1
        self.contestants.append(Contestant(first_name, last_name, email, registration_number))
        pass

    def pick_winner(self):

        winner_index = random.randint(0, len(self.contestants) - 1)
        winner = self.contestants[winner_index]
        winner.winner_status = True
        # TODO: call notify contestants
        return winner  # contestant

    def print_contestant_info(self, contestant):
        # TODO: make a call user_interface
        return
