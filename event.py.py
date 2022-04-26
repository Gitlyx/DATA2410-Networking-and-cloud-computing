import random

# Responses was refactored to unclutter and separate logic from trivial code.

name_list = [
    'Arya', 'Sansa', 'Jamie', 'Robb', 'Cersi', 'Jon', 'Tyrion', 'Bronn',
    'Eddard', 'Danny', 'Robert', 'Theon', 'Joff', 'Khal', 'Marg', 'Ramsey'
]

action_list = [
    'brew', 'eat', 'sleep', 'play', 'feast', 'hunt', 'read',
    'fight', 'brawl', 'swim', 'ride', 'stroll', 'hide', 'conquer',
    'drink', 'torture', 'slaughter',
]

icon_list = [
    '🧨', '✨', '🏏', '🪓', '🔨', '⚒️', '⛏️',
    '🪚', '🗡️', '⚔️', '🔪', '🏹', '💣',
]


def positive_response(word):
    repsonse_list = [
        f'Thats right my Lord! Today is the day of {word}!! 🔥🔥🔥',
        f'{word}? Proposal accepted! 🔨🔨🔨',
        f'Your order is my command, my Lord! {word} is all I wish for us to do. 🙇‍♂️🙇‍♂️🙇‍♂️',
        f'Wait a minute sire, {word}? I cannot believe this day has come. 🐎🐎🐎',
        f'If {word} is what my king says, then {word} is what his loyal men will do. ⚔️⚔️⚔️',
        f'{word.upper()}!!! Lets goooo!! 🤯🤯🤯',
        f'It\'s a party! Everyone, lets go its time for {word}! 🎉🎉🎉',
        f'{word.upper()}!!{word.upper()}!!{word.upper()}!!🙋‍♀️🙋‍♂️🙋',
    ]
    return random.choice(repsonse_list)


def negative_response():
    repsonse_list = [
        f'I dont know what that is!😒',
        f'Please my lord, may you reconsider this? 😣',
        f'I believe we could do better.🤨',
        f'Not to be rude, but I had other thoughts!😐',
        f'Oh please no! I have to get back to my wife and kids! 😖',
        f'Pardon me Lord? 😳',
        f'I heed your call, but please allow to to say my farewells? 😊',
        f'Hmm .. That might not be too wise .. 🤔',
        f'Request unhead of! 🤨',
        f'... 🤔',
    ]
    return random.choice(repsonse_list)


def random_botname():
    return random.choice(name_list)


def get_event():
    event_list = [
        f"{random.choice(name_list)}: There is a sudden attack from the north! Their tactic this time seem to be {random.choice(icon_list)} {random.choice(action_list)}ing while {random.choice(icon_list)} {random.choice(action_list)}ing! What do you want us to do? Our best options are either 1️⃣  {random.choice(action_list)}ing or 2️⃣  {random.choice(action_list)}ing the invaders. Choose quickly!",
        f"{random.choice(name_list)}: My Lord! We are about to get raided, the attackers are {random.choice(icon_list)} {random.choice(action_list)}ing outside waiting for us to {random.choice(icon_list)} {random.choice(action_list)} on the inside. Best course of action should be to retaliate by  1️⃣  {random.choice(action_list)}ing, we could also 2️⃣  {random.choice(action_list)} the enemy, the choice is yours!",
        f"{random.choice(name_list)}: Not again! We're all out of food because {random.choice(name_list)} chose to {random.choice(action_list)} all day! We should punish the lazy by a forceful 1️⃣  {random.choice(action_list)}ing or 2️⃣  {random.choice(action_list)}ing session. What will it be?",
        f"{random.choice(name_list)}: We caught this thief {random.choice(icon_list)} {random.choice(action_list)}ing around the streets, which is not allowed by your rules my Lord! We should sentence him to eternal 1️⃣  {random.choice(action_list)}ing or 2️⃣  {random.choice(action_list)}ing. What will it be?",
        f"[SPECIAL EVENT] Horseriding is coming up 🐎🐎🐎. How should we sabotage their horses? Choose one: 1️⃣  {random.choice(action_list)}, 2️⃣  {random.choice(action_list)}, 3️⃣  {random.choice(action_list)} or 4️⃣  {random.choice(action_list)} the horses.",
        f"[SPECIAL EVENT] The army is recruiting specialists to fight on the battlefield ⚔️⚔️⚔️. What does your team specialize in? Choose one: 1️⃣  {random.choice(action_list)}, 2️⃣  {random.choice(action_list)}, 3️⃣  {random.choice(action_list)}, 4️⃣  {random.choice(action_list)}",
    ]
    print(f'\n---------- [New Event] ----------')
    print(random.choice(event_list))
