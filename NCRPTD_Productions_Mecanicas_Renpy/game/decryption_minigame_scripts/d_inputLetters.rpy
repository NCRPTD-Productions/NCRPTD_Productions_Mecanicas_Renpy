label inputLetter(i):
    #TODO: Agregar sonido lápiz escribiendo
    $ assignedLetter = renpy.input(_("Introducir letra:"), allow="[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]", length=1)
    if assignedLetter == "":
        $ inputkey[i] = "  "
    else:
        $ inputkey[i] = assignedLetter.upper()

    python:
        noSeAyuda(assignedLetter.upper())
    
    if (KeyCompleted() == len(inputkey)):
        show screen DoneButton
    
    #"Input key = [inputkey!q]"
    #"Inputs text = [inputsText]"
    jump showSlots