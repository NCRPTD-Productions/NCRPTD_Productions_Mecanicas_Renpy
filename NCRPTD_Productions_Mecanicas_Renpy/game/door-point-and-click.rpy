init python:
    iskeyspickedup = False
    isGuillermoShoutOnce = False

init:
    transform hall_door:
        zoom 1.43
        xalign .5
        ypos 50
        # align(0.5, 0.95)

    transform hall_door_eye_view:
        zoom 2
        align(0.5, 0.5)
        # align(0.5, 0.95)

    transform hall_door_keys:
        zoom 2.5
        align(.63, .8)
        # align(0.5, 0.95)

screen hall_door_pac:
    imagebutton:
        idle "door idle.png"
        hover "door hover.png"
        action [Hide("displayTextScreen"), Jump("hall_door_action_pac")]
        at hall_door
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")

        
label hall_door_action_pac:
    # TODO: Agregar sonido timbre raro
    scene door view at hall_door_eye_view with fade
    Guillermo "CHARLY, CHARLY, ¿¡ESTÁS AHÍ!?"
    jump wait_until_open_door



screen hall_door_calling_continuously_pac:
    imagebutton:
        idle "door idle.png"
        hover "door hover.png"
        action [Hide("displayTextScreen"), Jump("hall_door_continuously_calling_action_pac")]
        at hall_door
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")
        
    imagebutton:
        align(0.9, 0.8)      
        idle "door keys idle.png"
        hover "door keys hover.png"
        action [Hide("displayTextScreen"), Jump("grab_keys")]
        at hall_door_keys
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")

        
label hall_door_continuously_calling_action_pac:
    
    # TODO: Agregar sonido timbre raro
    if isGuillermoShoutOnce:
        jump check_key_picked_up
    else:
        Guillermo "¡CARLOOOOOOOOOOOOOOOOOOOOS!"
        $ isGuillermoShoutOnce = True

label check_key_picked_up:
    if iskeyspickedup:
        jump sidewalk_scene_act_II
    else :
        Carlos "¡Las llaves, las llaves!"
        # TODO: Poner sonido llaves
        Carlos "¡DEJEN DE TOCAR EL TIMBRE!"
        # TODO: Dejan de sonar golpes y timbre
        call screen hall_door_calling_continuously_pac

label grab_keys:
    $ iskeyspickedup = True
    call screen hall_door_calling_continuously_pac
