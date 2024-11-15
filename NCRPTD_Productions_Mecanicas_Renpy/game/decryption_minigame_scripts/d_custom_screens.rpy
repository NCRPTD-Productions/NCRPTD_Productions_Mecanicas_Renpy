screen Escritorio:
    
    add "escritorio/bg desk_decryption.png" at decryption_desk

screen SlotButtons:
    vbox:
        xalign 0.1
        yalign 0.65
        spacing 10
        
        for i in inputkey:

            hbox:
                spacing 5
                if i < 10:
                    text "{color=#000}0[i] = {/color}"
                else:
                    text "{color=#000}[i] = {/color}"

                imagebutton:
                    
                    idle "escritorio/escritorio_textspace_idle.png"
                    hover "escritorio/escritorio_textspace_hover.png"
                    action Call("inputLetter", i)


screen SlotLetters:

    vbox:
        xalign 0.16
        yalign 0.65
        spacing 12

        for i in inputkey:

            text "{color=#f00}[inputkey[i]!u]{/color}":
                xalign 0.5
            

screen ShowMessage(text):

    vbox:
        xalign 0.75
        yalign 0.5
        spacing 40

        for line in range(len(text)): # va a iterar por cada dato dentro del array (cada linea del texto)
            $ text_line = text[line]

            hbox:
                spacing 7
                xalign 0.5
                
                for char in range(len(text_line)):
                    text "{color=#f00}[text_line[char]!u]{/color}"

screen ShowInputsText:
    
    vbox:
        xalign 0.75
        yalign 0.46
        spacing 40

        $ index = 0

        for line in range(len(messageSections)): # va a iterar por cada dato dentro del array (cada linea del texto)
            $ text_line = messageSections[line]
            $ increment = 0
            
            hbox:
                xalign 0.5
                spacing 35

                for char in range(len(text_line)):
                    text "{color=#00f}[inputsText[index]!u]{/color}"
                    $ index += 1

screen DoneButton:
    
    imagebutton:
        xalign 0.8
        yalign 0.2
        idle "escritorio/escritorio_textspace_idle.png"
        hover "escritorio/escritorio_textspace_hover.png"
        action Call("doneCheck")

    text "{color=#000}Done{/color}":
        xalign 0.8
        yalign 0.2

screen End:
    text "FIN":
        xalign 0.5
        yalign 0.5
    