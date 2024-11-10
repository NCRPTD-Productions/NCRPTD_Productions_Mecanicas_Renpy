label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        Carlos "¡No puedo creer que me haya equivocado!"
        Carlos "¡Es todo culpa de Justo! ¡Me está contagiando su dislexia!"
        
        hide screen SlotButtons
        hide screen SlotLetters
        hide screen ShowInputsText
        hide screen ShowMessage
        hide screen DoneButton
        hide screen Escritorio

        jump showSlots
    
    else:
        jump tutorial_end