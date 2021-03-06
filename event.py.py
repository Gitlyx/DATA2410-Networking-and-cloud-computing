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
    '๐งจ', 'โจ', '๐', '๐ช', '๐จ', 'โ๏ธ', 'โ๏ธ',
    '๐ช', '๐ก๏ธ', 'โ๏ธ', '๐ช', '๐น', '๐ฃ',
]


def positive_response(word):
    repsonse_list = [
        f'Thats right my Lord! Today is the day of {word}!! ๐ฅ๐ฅ๐ฅ',
        f'{word}? Proposal accepted! ๐จ๐จ๐จ',
        f'Your order is my command, my Lord! {word} is all I wish for us to do. ๐โโ๏ธ๐โโ๏ธ๐โโ๏ธ',
        f'Wait a minute sire, {word}? I cannot believe this day has come. ๐๐๐',
        f'If {word} is what my king says, then {word} is what his loyal men will do. โ๏ธโ๏ธโ๏ธ',
        f'{word.upper()}!!! Lets goooo!! ๐คฏ๐คฏ๐คฏ',
        f'It\'s a party! Everyone, lets go its time for {word}! ๐๐๐',
        f'{word.upper()}!!{word.upper()}!!{word.upper()}!!๐โโ๏ธ๐โโ๏ธ๐',
    ]
    return random.choice(repsonse_list)


def negative_response():
    repsonse_list = [
        f'I dont know what that is!๐',
        f'Please my lord, may you reconsider this? ๐ฃ',
        f'I believe we could do better.๐คจ',
        f'Not to be rude, but I had other thoughts!๐',
        f'Oh please no! I have to get back to my wife and kids! ๐',
        f'Pardon me Lord? ๐ณ',
        f'I heed your call, but please allow to to say my farewells? ๐',
        f'Hmm .. That might not be too wise .. ๐ค',
        f'Request unhead of! ๐คจ',
        f'... ๐ค',
    ]
    return random.choice(repsonse_list)


def random_botname():
    return random.choice(name_list)


def get_event():
    event_list = [
        f"{random.choice(name_list)}: There is a sudden attack from the north! Their tactic this time seem to be {random.choice(icon_list)} {random.choice(action_list)}ing while {random.choice(icon_list)} {random.choice(action_list)}ing! What do you want us to do? Our best options are either 1๏ธโฃ  {random.choice(action_list)}ing or 2๏ธโฃ  {random.choice(action_list)}ing the invaders. Choose quickly!",
        f"{random.choice(name_list)}: My Lord! We are about to get raided, the attackers are {random.choice(icon_list)} {random.choice(action_list)}ing outside waiting for us to {random.choice(icon_list)} {random.choice(action_list)} on the inside. Best course of action should be to retaliate by  1๏ธโฃ  {random.choice(action_list)}ing, we could also 2๏ธโฃ  {random.choice(action_list)} the enemy, the choice is yours!",
        f"{random.choice(name_list)}: Not again! We're all out of food because {random.choice(name_list)} chose to {random.choice(action_list)} all day! We should punish the lazy by a forceful 1๏ธโฃ  {random.choice(action_list)}ing or 2๏ธโฃ  {random.choice(action_list)}ing session. What will it be?",
        f"{random.choice(name_list)}: We caught this thief {random.choice(icon_list)} {random.choice(action_list)}ing around the streets, which is not allowed by your rules my Lord! We should sentence him to eternal 1๏ธโฃ  {random.choice(action_list)}ing or 2๏ธโฃ  {random.choice(action_list)}ing. What will it be?",
        f"[SPECIAL EVENT] Horseriding is coming up ๐๐๐. How should we sabotage their horses? Choose one: 1๏ธโฃ  {random.choice(action_list)}, 2๏ธโฃ  {random.choice(action_list)}, 3๏ธโฃ  {random.choice(action_list)} or 4๏ธโฃ  {random.choice(action_list)} the horses.",
        f"[SPECIAL EVENT] The army is recruiting specialists to fight on the battlefield โ๏ธโ๏ธโ๏ธ. What does your team specialize in? Choose one: 1๏ธโฃ  {random.choice(action_list)}, 2๏ธโฃ  {random.choice(action_list)}, 3๏ธโฃ  {random.choice(action_list)}, 4๏ธโฃ  {random.choice(action_list)}",
    ]
    print(f'\n---------- [New Event] ----------')
    print(random.choice(event_list))
