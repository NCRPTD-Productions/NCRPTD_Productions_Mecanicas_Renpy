init python:
    isalreadyfailed = False
label inputLetter(i):
    $ assignedLetter = renpy.input(_("Introducir letra:"), allow="[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]", length=1)
    if assignedLetter == "":
        $ inputkey[i] = "  "
        if isintutorial and not isalreadyfailed:
            show carlos 2ndpose at characters_half_size_placed_at_center
            play sound "sfx_pencil_erasing.mp3"
            Carlos "¡No puedo creer que me haya equivocado!"
            Carlos "¡Es todo culpa de Justo! ¡Me está contagiando su dislexia!"
            $ isalreadyfailed=True
    else:
        $ inputkey[i] = assignedLetter.upper()
        play audio "sfx_pencil_writting.mp3"

    python:
        noSeAyuda(assignedLetter.upper())
    
    if (KeyCompleted() == len(inputkey)):
        show screen DoneButton
    
    #"Input key = [inputkey!q]"
    #"Inputs text = [inputsText]"
    jump showSlots