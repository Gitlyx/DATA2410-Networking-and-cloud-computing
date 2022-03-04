import random


def profoundResponse(noun, noun2=None):
    alt1 = ['ARRGHH! ', 'Hmpf.. ', '... ', 'Grr.. ']
    return (random.choice(alt1) + "Me no like {}".format(noun+'ing!'))


def smartResponse(noun, noun2=None):
    alt1 = ['{}?, let me see .. ',
            '{} is a bit .. ',
            '{}ing you say? ',
            'I see you like to {}, '
            ]
    return(random.choice(alt1).format(noun) + 'I can do {}'.format(noun+'ing.'))


def lazyResponse(noun, noun2=['sleep', 'rest', 'eat']):
    alt1 = ['weak', 'slow', 'tired', 'hungry']
    return('I am too {} to {}, '.format(random.choice(alt1), noun) + 'I rather go {}.'.format(random.choice(noun2)))
