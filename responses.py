import random

members = []


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if p_message == '?roll':
        return members[random.randint(0, len(members)-1)]

    if p_message == '?help':
        with open('help.txt', 'r') as file:
            text = file.read()
        return text
