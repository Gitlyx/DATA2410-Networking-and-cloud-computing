import random

# Responses was refactored to unclutter and separate logic from trivial code.


action_list = [
    'cook', 'eat', 'sleep', 'play', 'game', 'work', 'study',
    'fight', 'run', 'swim', 'drive', 'walk', 'exercize', 'jogg'
]


def positive(word):
    positive_responses = [
        f'Wow, {word}? With burning passion! 🔥🔥🔥',
        f'{word}? Affirmative, ninja moving out! 🥷🥷🥷',
        f'Order recieved! Decepticons ready to {word}. 🤖🤖🤖',
        f'Hold up, {word}ing? Please let me bring my pet rock. 🪨🪨🪨',
        f'Finally someone who likes {word}ing, let me finish my spaghetto. 🍝🍝🍝',
        f'{word.upper()}!!! Lets goooo!! 🤯🤯🤯',
        f'It\'s a party! Bro, lets go {word}ing now! 🎉🎉🎉',
        f'{word.upper()}!!{word.upper()}!!{word.upper()}!!😎😎😎',
    ]
    return random.choice(positive_responses)

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
    return random.choice(negative_response)