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


people = ['Ulrik', 'Johan', 'Mohammed', 'Ahsan', 'Charlie', 'Adrian']


def oneReply(): return random.choice(people)


def manyReplies():
    randomPeople = people.copy()
    random.shuffle(randomPeople)
    return randomPeople[:random.randrange(5)+1]


def allReplies(): return people


def allGoodbye():
    print("\nThe host is leaving, everyone say goodbye!\n")
    byeAll = manyReplies()
    for i in byeAll:
        print(i, ": ", replyFarewell(), "\n")


allGoodbye()
