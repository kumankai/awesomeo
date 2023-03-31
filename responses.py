import random

members = []


def handle_response(message) -> str:
    msg = message.lower()

    if msg == 'hello':
        return 'oh hey'

    if msg == '?roll':
        return members[random.randint(0, len(members)-1)]

    if msg == '?help':
        with open('help.txt', 'r') as file:
            text = file.read()
        return text

    if 'fatass' in msg:
        return "dont call me fat you fucking jew"
