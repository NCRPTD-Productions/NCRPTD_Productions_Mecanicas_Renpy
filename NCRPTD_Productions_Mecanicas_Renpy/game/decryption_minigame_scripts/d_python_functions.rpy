init python:
    # Slice the text into lines for display
    def SliceMessage(text, lineLength):
        slicedMessage = []
        part = []
        index = 0

        # Cycle through each symbol in the given array (text)
        for i in text:
            part.append(i) # Create a sub-array with the characters we've already cycled through
            index += 1

            if index == len(text): # Has this part reached the end of the text?
                
                # Append the last part if there's any remaining text
                if part:
                    slicedMessage.append(part)

            elif len(part) == lineLength: # Has the length of this part reached it's maxumim possible length?
                foundSpace = False
                partIndex = -1

                # Search backwards for a space character
                while not foundSpace and abs(partIndex) <= len(part):
                    # Check for two consecutive spaces
                    if part[partIndex] == " ":
                        foundSpace = True
                    else:
                        partIndex -= 1
                
                if foundSpace:
                    # Append the sliced part, preserving it as a list
                    slicedMessage.append(part[:partIndex])  # include the space in the slice
                    part = part[partIndex:]  # Keep text after the found spaces
                else:
                    # If no space was found, just add the entire part
                    slicedMessage.append(part)
                    part = []  # Reset part

        
        return slicedMessage

    def DetermineKeyOrder(text):
        seen = dict()
        order_map = {char: index for index, char in enumerate(KEY)}
        keyOrder = dict()
        
        for char in text:
            letter = char.upper()
            if (letter not in seen) and (char != " "):
                seen[letter] = KEY.index(letter)
                keyOrder[letter] = KEY.index(letter)

        sortedKeyOrder = dict(sorted(keyOrder.items(), key=lambda item: order_map.get(item[0], len(KEY))))
        return sortedKeyOrder
    
    def SetEmptyArray(key):
        newArray = []
        
        for letter in range(len(key)):
            newArray.append("  ")

        return newArray

    def NumStringFromMessage(text):
        numString = []
        
        for letter in text: # Cycles through every letter in the message
            if letter == " ":
                numString.append(" ")
            else:
                for index in range(len(KEY)): # Cycles through KEY to compare current letter
                    if letter.upper() == KEY[index]:
                        if index < 10:
                            numString.append("0" + str(index))
                        else:
                            numString.append(str(index))
        
        return numString

    def noSeAyuda(inputletter):
        for i in range(len(symbolText)):
            if symbolText[i] != ' ':
                symbolNum = int(symbolText[i])
                inputsText[i] = inputkey[symbolNum]
            else:
                inputsText[i] = ''

    def KeyCompleted():
        completedKey = 0

        for char in inputkey.values():
            if char != "  ":
                completedKey += 1
        
        return completedKey

    def CheckKeyCompletion():
        correctInputs = 0

        for i in inputkey.keys():
            originalKeyValue = list(keyOrder.keys())[list(keyOrder.values()).index(i)]
            if inputkey[i] == originalKeyValue:
                correctInputs += 1
        
        return correctInputs