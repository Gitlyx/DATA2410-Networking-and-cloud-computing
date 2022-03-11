import random


action_list = [
    'cook', 'eat', 'sleep', 'play', 'game', 'work', 'study',
    'fight', 'run', 'swim', 'drive', 'walk', 'exercize', 'jogg'
]


def positive(word):
    positive_responses = [
        f'Wow, {word}? My palms are sweaty ..',
        f'I can\'t handle {word}ing, my knees are weak and arms are heavy.',
        f'Finally someone who likes {word}ing, just let me grab my moms spaghetti.',
        f'I haven\'t tried {word}ing before, but I promise I\'ll remain calm and ready. ',
    ]

    response = random.choice(positive_responses)
    return response


def negative():
    negative_response = [
        f'I dont know what that is!😒',
        f'Haha, what planet are you from? 😂😂',
        f'What a strange request.🤨',
        f'Never heard of it!😐',
        f'Oh no .. hes speaking gibrish again.! 😖',
        f'Come again? 😳',
        f'You wanna do what? 😊',
        f'Hmm .. Whats that? 🤔',
        f'Strange request. 🤨',
        f'Whaaa 🤔',

    ]

    response = random.choice(negative_response)
    return response
