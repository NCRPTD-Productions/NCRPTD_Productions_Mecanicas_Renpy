init python:
    async def prueba():
        await renpy.pause(3)
        
        renpy.call_in_new_context("endDecryption")

label doneCheck:
    if CheckKeyCompletion() != len(inputkey):
        if isfailingintutorial:
            show carlos 2ndpose at characters_half_size_placed_at_center
            Carlos "¡No puedo creer que me haya equivocado!"
            Carlos "¡Es todo culpa de Justo! ¡Me está contagiando su dislexia!"
        else:

            show carlos surprised at characters_half_size_placed_at_center
            Carlos "..."
            Carlos "No puede ser... ¿¡Qué me pasa?!"
            # Pause for 3 seconds
            pause(3)
            jump end_decryption_abruptly

        jump showSlots

    
    else:
        jump endDecryption

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
