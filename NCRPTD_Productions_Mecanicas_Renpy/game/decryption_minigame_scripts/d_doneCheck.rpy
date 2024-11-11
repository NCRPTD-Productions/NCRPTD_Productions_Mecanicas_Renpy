label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        Carlos "¡No puedo creer que me haya equivocado!"
        Carlos "¡Es todo culpa de Justo! ¡Me está contagiando su dislexia!"
        
        jump showSlots
    
    else:
        hide screen Escritorio
        hide screen SlotButtons
        hide screen SlotLetters
        hide screen ShowMessage
        hide screen ShowInputsText
        hide screen DoneButton
        # hide screen End
        scene black
        jump tutorial_end
        # hide screen SlotButtons
        # hide screen SlotLetters
        # hide screen ShowInputsText
        # hide screen ShowMessage
        # hide screen DoneButton
        # hide screen Escritorio
        # jump tutorial_end