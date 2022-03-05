import re
import responses as resp

# Logic for detecting words in a sentence. This allows the bots to respond without having an exact word count.


def messageScanner(userMessage, wordPool, singleResponse=False, requiredWords=[]):
    wordsDetected = 0
    hasRequiredWords = True

    # Word counter for detected words in the entire sentence.
    for word in userMessage:
        if word in wordPool:
            wordsDetected += 1
    # Calculates the match rate compared to the words detected.
    matchRate = float(wordsDetected) / float(len(wordPool))

    # Checks if any of the words are in the required word list.
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break

    # Return function triggers only if the sentence has required words or a single word.
    if hasRequiredWords or singleResponse:
        return int(matchRate * 100)
    else:
        return 0

# Logic for triggering a response based on detected word in a list.


def responseTrigger(userMessage):
    matchRateList = {}

    # A helper to easier bind arguments to multiple the functions.
    def reply(botResponse, wordPool, singleResponse=False, requiredWords=[]):
        nonlocal matchRateList
        matchRateList[botResponse] = messageScanner(
            userMessage, wordPool, singleResponse, requiredWords)

    # Any words detected in wordPool will give botResponse.
    reply(resp.replyGreeting(), resp.triggerGreeting, singleResponse=True)
    reply(resp.replyFarewell(), resp.triggerFarewell, singleResponse=True)
    reply(resp.replyFarewell(), resp.triggerFarewell, singleResponse=True)
    reply(resp.replyExit(), resp.triggerExit,
          singleResponse=True, requiredWords=[])
    reply(resp.replyHelp(), resp.triggerHelp,
          singleResponse=True, requiredWords=['--help', '-h'])

    # Takes input and compares with the best match rate.
    bestMatch = max(matchRateList, key=matchRateList.get)

    return resp.unknownReply(userMessage) if matchRateList[bestMatch] < 1 else bestMatch


def getResponse(userMessage):
    splitMessage = re.split(r'\s+|[,;?!.]\s*', userMessage.lower())
    response = responseTrigger(splitMessage)
    return response


while True:
    print(resp.oneReply(), ": ", getResponse(input('\nYou: ')))
