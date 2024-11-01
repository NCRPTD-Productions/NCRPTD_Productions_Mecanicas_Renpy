label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        "Tu clave no está bien. Revisá"
        jump showSlots
    
    else:
        "Esaaaa bien ahi :)"
        "El mensaje era \"[messageText!cl]\""
        "Felicidades :)"

        jump end