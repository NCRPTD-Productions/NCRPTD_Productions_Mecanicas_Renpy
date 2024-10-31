#Characters

define Carlos = Character('Carlos', color= "#E03b8b")
define Edgar = Character('Edgar', color= "#24dddd")
#

define fadeHold = Fade(.5, .75, 3, color="#000")
define fadeHoldGameLogo = Fade(.5, 1, 4, color="#000")
init:
    transform pac_custom_library_zoom:
        zoom 1.37

init python:
    def StopSound(soundEffect):
        if(renpy.sound.is_playing("sfx_alarm.mp3")):
            renpy.sound.StopSound("sfx_alarm.mp3")

    isPlaying =False
    
    def eyewarp(x):
        return x**3
    eye_open = ImageDissolve("eye.png", .75, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("eye.png", .75, ramplen=128, reverse=True, time_warp=eyewarp)
    black_image = Solid("#000")
    white_image = Solid("#FFF")

#Custom image sizes
transform opening_image_size: #Opening text size adjustment
    xalign 0.5
    yalign 0.5

transform characters_half_size_placed_at_right: 
    zoom 0.5
    pos (300, 500)

transform characters_half_size_placed_at_center: 
    zoom 0.5
    pos (600, 500)

transform characters_half_size_placed_at_left: 
    zoom 0.5
    pos (900, 500)

transform custom_background_size: 
    zoom 2
    pos (0,0)
transform carlos_bedroom_background_size: 
    zoom .75
    pos (0,0)
transform carlos_corner_bedroom_background_size: 
    zoom 2
    pos (0,0)
#

#Point and click image buttons
screen test_pac:
        imagebutton:
            pos(645, 545)
            idle "pac_biblioteca_izquierda_idle.png"
            hover "pac_biblioteca_izquierda_hover.png"
            action [Hide("displayTextScreen"), Jump("end_point_and_click")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A book?")
            unhovered Hide("displayTextScreen")

        imagebutton:
            pos(75, 845)
            idle "pac_edgar_idle.png"
            hover "pac_edgar_hover.png"
            action [Hide("displayTextScreen"), Jump("end_point_and_click")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A fish")
            unhovered Hide("displayTextScreen")
            
        imagebutton:
            pos(2110, 1085)
            idle "pac_cama_carlos_idle.png"
            hover "pac_cama_carlos_hover.png"
            action [Hide("displayTextScreen"), Jump("end_point_and_click")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A fish")
            unhovered Hide("displayTextScreen")

screen displayTextScreen:  
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
        

#
label start:
    show bg ncrptd productions opening title at opening_image_size
    with fadeHold
    show bg members at opening_image_size
    with fadeHold
    show bg game logo at opening_image_size
    with fadeHoldGameLogo
    
label carlos_closed_eyes_scene:
    
    scene bg blank at custom_background_size
    # play sound "sfx_alarm.mp3" loop
    "*BEEP* *BEEP"
    #TODO: Meter audio de alarma
    scene white
    with eye_open
    scene black
    with eye_shut
    scene white
    with eye_open
    scene black
    with eye_shut
    scene white
    with eye_open
    scene black
    with eye_shut

label carlos_bedroom_ceiling_sequence:
    scene bg techo habitacion carlos at carlos_corner_bedroom_background_size
    with fade
    "??" "Que calvario..."
    #TODO: Meter audio de suspiro corto
    "??" "Cada vez estoy más cerca de descubrir a ese asesino."
    "??" "Solo espero que ese rarito y el disléxico de mierda no me molesten."
    #TODO: Meter audio de correr sábanas


    

label carlos_bedroom_scene:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos normal  at characters_half_size_placed_at_right
    show edgar neutral  at characters_half_size_placed_at_left
    with fade
    "??" "Hola, Edgar. ¿Cómo amaneciste?"
    Edgar "Glup."
    "??" "Por supuesto que bien. Si te cambié el agua y di de comer."
    Edgar "..."
    "??" "No digas nada más, mi querido Edgar. Tengo trabajo que hacer."

label start_point_and_click:
    scene bg habitacion carlos at carlos_bedroom_background_size
    "{i}Explora la habitación o ve al escritorio.{/i}"


    call screen test_pac

label end_point_and_click:
    "??" "Buenas"
    return