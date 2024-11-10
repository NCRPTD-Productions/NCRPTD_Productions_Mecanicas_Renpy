label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        Carlos "¡No puedo creer que me haya equivocado!"
        Carlos "¡Es todo culpa de Justo! ¡Me está contagiando su dislexia!"
        
        jump showSlots
    
    else:
        jump tutorial_end