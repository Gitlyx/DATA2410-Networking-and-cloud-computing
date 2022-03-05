import random

isGreeting = ['hello', 'hey', 'sup', 'hi']


def replyGreeting():
    greeting = [
        'What sup!',
        'Yooo!',
        'Oh you\'re here!',
        'Look who showed up!']
    response = random.choice(greeting)
    return response


isFarewell = ['bye', 'goodbye', 'farewell', 'cya']


def replyFarewell():
    farewell = [
        'Ahh you\'re leaving already?',
        'See you another time bud!',
        'Cya!',
        'Good seeing you', ]
    response = random.choice(farewell)
    return response
