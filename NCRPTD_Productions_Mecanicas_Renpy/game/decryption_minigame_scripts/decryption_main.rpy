define keyOrder = {}
define inputkey = {}
define symbolText = []
define inputsText = []

define messageSections = []
define inputsTextSections = []
define messageText = ""

init:
    transform decryption_desk:
        zoom 0.9

label decryption(newMessage):


    $ messageText = newMessage

    python:
        keyOrder = DetermineKeyOrder(messageText)
        inputkey = {index : "  " for index in keyOrder.values()}
        symbolText = NumStringFromMessage(messageText)
        inputsText = SetEmptyArray(symbolText)
        messageSections = SliceMessage(symbolText, 17)

    scene bg escritorio at decryption_desk
    show carlos thoughtful at characters_half_size_placed_at_left
    Carlos "Hay que ser ordenado como siempre. Las letras van en la hoja izquierda, al lado de cada símbolo..."
    Carlos "Y en el criptograma, en la hoja derecha, arriba de cada símbolo."
    show screen Escritorio

    #"\'[messageText]\'"
    #"\'symbol text = [symbolText]\'"
    #"\'[len(inputsText)] = [inputsText]\'"
    #"\'text in nums = [messageSections]\'"
    #"key order = [keyOrder!q]"
    #"Input key = [inputkey!q]"
    jump showSlots

# Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua