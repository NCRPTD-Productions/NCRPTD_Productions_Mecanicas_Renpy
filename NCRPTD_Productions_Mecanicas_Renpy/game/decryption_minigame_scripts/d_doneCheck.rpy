init python:
    async def prueba():
        await renpy.pause(3)
        
        renpy.call_in_new_context("endDecryption")

label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        if not isintutorial:
            Carlos "..."
            Carlos "No puede ser... ¿¡Qué me pasa?!"
            # Pause for 3 seconds
            pause(3)
            jump end_decryption_abruptly
        jump showSlots
    else:
        if isintutorial:
            jump endDecryption
        else:
            pause(3)
            jump end_decryption_abruptly

label end_decryption_abruptly:
    
        hide screen Escritorio
        hide screen SlotButtons
        hide screen SlotLetters
        hide screen ShowMessage
        hide screen ShowInputsText
        hide screen DoneButton
        # hide screen End
        scene black
        jump carlos_stops_cryptogram_abruptly

label endDecryption:
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
