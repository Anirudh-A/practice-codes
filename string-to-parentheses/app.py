def stringToParentheses(inputString):
    if not(bool(inputString)):
        return 'Invalid input'

    uniqueCharacters = dict()

    # determine unique characters
    for character in inputString:
        if character in uniqueCharacters:
            uniqueCharacters.update({character: 0})
            continue
        uniqueCharacters.update({character: 1})

    outputString = ""
    # buil output string
    for character in inputString:
        if bool(uniqueCharacters[character]):
            outputString += ')'
            continue
        outputString += '('

    return outputString


inputString = input('Enter string to be converted to parentheses : ')
outputString = stringToParentheses(inputString)
print('After conversion: ' + outputString)
