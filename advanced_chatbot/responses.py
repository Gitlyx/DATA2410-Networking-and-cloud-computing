import random

people = ['Ulrik', 'Johan', 'Mohammed', 'Ahsan', 'Charlie', 'Adrian']
triggerGreeting = ['hello', 'hey', 'sup', 'hi', 'hei', 'skjera']
triggerFarewell = ['bye', 'goodbye', 'farewell', 'cya']
triggerExit = ['exit']
triggerHelp = ['help', 'h', '--help', '-h']


def replyGreeting():
    greeting = [
        'What sup!',
        'Yooo!',
        'Oh you\'re here!',
        'Look who showed up!']
    response = random.choice(greeting)
    return response


def replyFarewell():
    farewell = [
        'Oh you\'re leaving already?',
        'Dont leave without me!',
        'Cya next friday!',
        'Sayonara my guy',
        'Good bye!',
    ]
    response = random.choice(farewell)
    return response


def replyExit():
    for person in people:
        print(person + ": " + replyFarewell())
    return "*waves*"


def replyHelp():
    alt1 = '/'.join(triggerGreeting)
    alt2 = '/'.join(triggerFarewell)

    return ('To be able to communicate with us, you can try one of the following: [' + alt1 + '] or [' + alt2 + '].')


def unknownReply():
    unknown = [
        'Not sure what you mean ...',
        'Please, I\'m not the right guy for this',
        'I don\'t think I understand.'
    ]
    return random.choice(unknown)


def oneReply(): return random.choice(people)
