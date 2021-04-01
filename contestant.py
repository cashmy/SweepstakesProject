import user_interface


class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number

    def notify(self, is_winner):
        if is_winner:
            text = 'You are the WINNER!'
        else:
            text = 'Unfortunately you did not win this time. Please register for our next sweepstakes.'
        user_interface.output_text(f'\n{self.first_name}, we wanted to let you know!')
        user_interface.output_text(text)
        pass
