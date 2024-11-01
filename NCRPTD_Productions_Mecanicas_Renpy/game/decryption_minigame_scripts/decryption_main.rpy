define keyOrder = {}
define inputkey = {}
define symbolText = []
define inputsText = []

define messageSections = []
define inputsTextSections = []
define messageText = ""

label decryption(newMessage):
    $ messageText = newMessage

    python:
        keyOrder = DetermineKeyOrder(messageText)
        inputkey = {index : "  " for index in keyOrder.values()}
        symbolText = NumStringFromMessage(messageText)
        inputsText = SetEmptyArray(symbolText)
        messageSections = SliceMessage(symbolText, 17)

    show screen Escritorio

    #"\'[messageText]\'"
    #"\'symbol text = [symbolText]\'"
    #"\'[len(inputsText)] = [inputsText]\'"
    #"\'text in nums = [messageSections]\'"
    #"key order = [keyOrder!q]"
    #"Input key = [inputkey!q]"
    jump showSlots

# Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua