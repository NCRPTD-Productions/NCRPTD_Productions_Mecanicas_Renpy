screen Escritorio:
    
    add "escritorio/bg desk_decryption.png" at decryption_desk

screen SlotButtons:
    vbox:
        xalign 0.158
        ypos 0.19
        spacing 10
        
        for i in inputkey:

            hbox:
                spacing 5
                
                if (i < 10):
                    add "escritorio/simbolos/0[i].png" zoom 1.1
                else:
                    add "escritorio/simbolos/[i].png" zoom 1.1

                text "{color=#666} = {/color}"

                imagebutton:
                    
                    idle "escritorio/escritorio_textspace_idle.png"
                    hover "escritorio/escritorio_textspace_hover.png"
                    action Call("inputLetter", i)


screen SlotLetters:

    vbox:
        xalign 0.2
        ypos 0.19
        spacing 10

        for i in inputkey:

            text "{color=#666}[inputkey[i]!u]{/color}":
                xalign 0.5
            

screen ShowMessage(text):

    vbox:
        xalign 0.8
        ypos 0.4
        spacing 40

        for line in range(len(text)): # va a iterar por cada dato dentro del array (cada linea del texto)
            $ text_line = text[line]

            hbox:
                spacing 10
                xalign 0.5
                
                for char in range(len(text_line)):
                    if (text_line[char] != " "):
                        add "escritorio/simbolos/[text_line[char]!u].png" zoom 1.1
                    else:
                        text "{color=#000} [text_line[char]!u]{/color}"

screen ShowInputsText:
    
    vbox:
        xalign 0.8
        ypos 0.36
        spacing 40

        $ index = 0

        for line in range(len(messageSections)): # va a iterar por cada dato dentro del array (cada linea del texto)
            $ text_line = messageSections[line]
            $ increment = 0
            
            hbox:
                xalign 0.5
                spacing 25

                for char in range(len(text_line)):
                    text "{color=#f00}[inputsText[index]!u]{/color}"
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
    