import random


def profoundResponse(noun):
    alt1 = ['ARRGHH! ', 'Hmpf.. ', '... ', 'Grr.. ']
    return (random.choice(alt1) + "Me no like {}".format(noun+'ing!'))


def smartResponse(noun):
    alt1 = ['{}?, let me see .. ',
            '{} is a bit .. ',
            '{}ing you say? ',
            'I see you like to {}, '
            ]
    return(random.choice(alt1).format(noun) + 'I can do {}'.format(noun+'ing.'))


def lazyResponse(noun):
    alt1 = ['weak', 'slow', 'tired', 'hungry']
    alt2=['sleep', 'rest', 'eat']
    return('I am too {} to {}, '.format(random.choice(alt1), noun) + 'I rather go {}.'.format(random.choice(alt2)))


def randomResponse(noun):
    responses = [profoundResponse, smartResponse, lazyResponse]
    return random.choice(responses)(noun)
