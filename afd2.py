stateList = input()
afd = {}
for state in stateList.split(' '):
    afd[state] = {}
symbolList = input()
index = int(input())
for i in range(index):
    temp = input()
    temp = temp.split(' ')
    if(temp[1] not in afd[temp[0]]):
        afd[temp[0]][temp[1]] = temp[2]
initialState = input()
finalState = input()
words = input()
words = words.split(' ')
for word in words:
    currentState = initialState
    errorState = 0
    for char in word:
        try:
            currentState = afd[currentState][char]
        except KeyError:
            errorState = 1
            break
    if(errorState == 1 or currentState not in finalState):
        print('N')
    else:
        print('S')