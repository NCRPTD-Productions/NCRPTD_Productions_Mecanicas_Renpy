init python:
    iskeyspickedup = False
    isGuillermoShoutOnce = False

init:
    transform hall_door:
        zoom 1.43
        align(.5, .42)
        # align(0.5, 0.95)

    transform hall_door_eye_view:
        zoom 2
        align(0.5, 0.5)
        # align(0.5, 0.95)

    transform hall_door_keys:
        zoom 1
        
        # align(0.9, 0.8)      
        align(.58, .38)
        # align(0.5, 0.95)

screen hall_door_pac:
    imagebutton:
        auto "pac_hallway_carlos_door_%s.png"
        action [Hide("displayTextScreen"), Jump("hall_door_action_pac")]
        at hall_door
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")

        
label hall_door_action_pac:
    scene door view at hall_door_eye_view with fade
    Guillermo "CHARLY, CHARLY, ¿¡ESTÁS AHÍ!?"
    jump wait_until_open_door
    return

screen hall_door_calling_continuously_pac:
    imagebutton:
        auto "pac_hallway_carlos_door_%s.png"
        action [Hide("displayTextScreen"), Jump("hall_door_continuously_calling_action_pac")]
        at hall_door
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")
        
    imagebutton:
        idle "door keys idle.png"
        hover "door keys hover.png"
        action [Hide("displayTextScreen"), Jump("grab_keys")]
        at hall_door_keys
        # hovered Show("displayTextScreen", displayText = "¿Abrir?")
        # unhovered Hide("displayTextScreen")

        
label hall_door_continuously_calling_action_pac:
    
    
    if isGuillermoShoutOnce:
        play sound "sfx_knocking_on_door_desperately.mp3"
        jump check_key_picked_up
    else:
        play sound "sfx_knocking_on_door_desperately.mp3"
        Guillermo "¡CARLOOOOOOOOOOOOOOOOOOOOS!"
        $ isGuillermoShoutOnce = True
        call screen hall_door_calling_continuously_pac

label check_key_picked_up:
    if iskeyspickedup:
        
        jump sidewalk_scene_act_II
    else :
        play sound "sfx_knocking_on_door_desperately.mp3"
        Carlos "¡Las llaves, las llaves!"
        Carlos "¡DEJEN DE TOCAR EL TIMBRE!"
        call screen hall_door_calling_continuously_pac

label grab_keys:
    $ iskeyspickedup = True
    play sound "sfx_pick_up_keys.mp3"
    pause(1)
    play sound "sfx_knocking_on_door_desperately.mp3"
    call screen hall_door_calling_continuously_pac
    return
