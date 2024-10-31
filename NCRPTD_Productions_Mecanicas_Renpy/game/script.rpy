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

transform characters_zoomed_placed_at_right: 
    zoom 0.7
    pos (300, 400)

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
            pos(75, 845)
            idle "pac_edgar_idle.png"
            hover "pac_edgar_hover.png"
            action [Hide("displayTextScreen"), Jump("edgar_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A fish")
            unhovered Hide("displayTextScreen")

        imagebutton:
            pos(645, 545)
            idle "pac_biblioteca_izquierda_idle.png"
            hover "pac_biblioteca_izquierda_hover.png"
            action [Hide("displayTextScreen"), Jump("left_library_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A book?")
            unhovered Hide("displayTextScreen")
            
        imagebutton:
            pos(1725, 545)
            idle "pac_biblioteca_derecha_idle.png"
            hover "pac_biblioteca_derecha_hover.png"
            action [Hide("displayTextScreen"), Jump("right_library_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "A book?")
            unhovered Hide("displayTextScreen")
            
        imagebutton:
            pos(2110, 1085)
            idle "pac_cama_carlos_idle.png"
            hover "pac_cama_carlos_hover.png"
            action [Hide("displayTextScreen"), Jump("bed_action_pac")]
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

#scene management

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

#point and click action end scenes

label edgar_action_pac:
    Edgar "Glup."
    show carlos smirk at characters_half_size_placed_at_right
    "??" "Tú lo has dicho, amigo."
    call start_point_and_click

label bed_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_right
    "??" "No estoy cansado aún."
    call start_point_and_click

#Left library

label left_library_action_pac:
    scene bg biblioteca izquierda detalle at carlos_bedroom_background_size
    menu:
        "Figura del EVA-01.":
            jump left_library_option_EVA_01
        "El Escarabajo de oro.":
            jump left_library_option_Golden_Beetle
        "El Psicoanalista.":
            jump left_library_option_The_Psychoanalyst
        "Volver.":
            jump library_option_Go_Back

label left_library_option_EVA_01:
    show carlos annoyed at characters_zoomed_placed_at_right
    "??" "¡Súbete al maldito EVA, Shinji!"
    call left_library_action_pac

label left_library_option_Golden_Beetle:
    show carlos thoughtful at characters_zoomed_placed_at_right
    "??" "Lo que me llevó a la criptografía."
    call left_library_action_pac

label left_library_option_The_Psychoanalyst:
    show carlos 2ndpose at characters_zoomed_placed_at_right
    "??" "Las secuelas nunca existieron."
    call left_library_action_pac

label library_option_Go_Back:
    call start_point_and_click

#Right library

label right_library_action_pac:
    scene bg biblioteca derecha detalle at carlos_bedroom_background_size
    menu:
        "Death Note.":
            jump right_library_option_Death_Note
        "Figura de Ryuk.":
            jump right_library_option_Ryuk_Figure
        "El Psicoanalista.":
            jump right_library_option_The_Psychoanalyst
        "Volver.":
            jump library_option_Go_Back

label right_library_option_Death_Note:
    show carlos smirk at characters_zoomed_placed_at_right
    "??" "Kira tenía razón."
    call right_library_action_pac

label right_library_option_Ryuk_Figure:
    show carlos sigh at characters_zoomed_placed_at_right
    "??" "Me saliste caro."
    call right_library_action_pac

label right_library_option_The_Psychoanalyst:
    show carlos 2ndpose at characters_zoomed_placed_at_right
    "??" "Las secuelas nunca existieron."
    call right_library_action_pac

#
#