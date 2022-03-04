import responses as resp


def getResponse(action):
    family = ['Cave dad', 'Cave mom', 'Cave baby']
    for i in family:
        print(i + ": " + resp.randomResponse(action))


while True:
    getResponse(input("\nDo you guys wanna: "))
