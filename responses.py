import random

people = ['Ulrik', 'Johan', 'Mohammed', 'Ahsan', 'Charlie', 'Adrian']
triggerGreeintg = ['hello', 'hey', 'sup', 'hi', 'hei', 'skjera?']
triggerFarewell = ['bye', 'goodbye', 'farewell', 'cya']
triggerHelp = ['--help', '-h', 'help']


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
        'Oh nei ikke stikk',
        'Snakkes bro',
        'HEY! Du skylder meg en kebab!',
        'Brur kom hvor skal du?!',
        'Ææælig, kom her',
        'Venta brur',
    ]
    response = random.choice(farewell)
    return response


def oneReply(): return random.choice(people)


def manyReplies():
    randomPeople = people.copy()
    random.shuffle(randomPeople)
    return randomPeople[:random.randrange(len(people))+1]


def allReplies(): return people


def allGoodbye():
    byeAll = allReplies()
    for i in byeAll:
        print(i, ": \t", replyFarewell())
    print("\n")
