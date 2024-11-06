﻿#Characters

define Carlos = Character('Carlos', color= "#E03b8b")
define Edgar = Character('Edgar', color= "#24dddd")
define Justo= Character('Justo Pianelo', color= "#b209c9")

# NVL characters are used for the phone texting
define carlos_phone_nvl = Character("Carlos", kind=nvl, image="nighten", callback=Phone_SendSound)
define justo_phone_nvl = Character("Justo", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#

# Videos

image pruebadiosqueande = Movie(play="prueba.mkv", size=(1920,1080), loop=False)

#

define fadeHold = Fade(.5, .75, 3, color="#000")
define fadeHoldGameLogo = Fade(.5, 1, 4, color="#000")

define eyeopen = ImageDissolve("eye.png", 1.5, 100)
define eyeclose = ImageDissolve("eye.png", 1.5, 100, reverse=True)

init:

#Custom image sizes
    transform pac_custom_library_zoom:
        zoom 1.37

    transform opening_image_size: #Opening text size adjustment
        xalign 0.5
        yalign 0.5

    transform characters_half_size_placed_at_left: 
        zoom 0.5
        pos (-10, 350) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3  # Move to the right over 2 seconds
        # easeinout 2.0 xalign 0.5  # Optionally ease the character to the center after

    transform characters_half_size_placed_at_center: 
        zoom 0.5
        # xalign .5
        ypos 350
        
        linear .25 xalign .5  # Move to the right over 2 seconds
        # pos (600, 350)

    transform characters_half_size_placed_at_right: 
        zoom 0.5
        pos (900, 350)
        linear .25 xalign .5

    transform characters_half_size_placed_at_right_no_transition: 
        zoom 0.5
        pos (900, 350)

    transform characters_half_size_placed_at_left_no_transition: 
        zoom 0.5
        xalign .3
        ypos 350
        # pos (-10, 350) # pos (300, 500)

    transform characters_half_size_placed_at_center_no_transition: 
        zoom 0.5
        
        pos (600, 350)
        
    transform edgar_placed_at_right:
        zoom 0.35
        pos (2350, 370) # pos (1650, 370)
        linear .25 xalign .75

    transform edgar_placed_at_left:
        zoom 0.35
        pos (400, 370)

    transform characters_zoomed_placed_at_right: 
        zoom 0.7
        
        pos (300, 400)

    transform custom_background_size: 
        zoom 2
        pos (0,0)
    transform carlos_bedroom_background_size: 
        zoom .75
        pos (0,0)
        
    transform carlos_bedroom_left_library: 
        zoom .75
        pos (0,0)
        
    transform carlos_bedroom_right_library: 
        zoom .75
        pos (0,-150)
        
    transform carlos_corner_bedroom_background_size: 
        zoom 1.5
        pos (0,0)

    transform menu_position:
        pos(0,0)
#

init python:
    def StopSound(soundEffect):
        if(renpy.sound.is_playing("sfx_alarm.mp3")):
            renpy.sound.StopSound("sfx_alarm.mp3")

    isPlaying =False
    
    def eyewarp(x):
        return x**3
    black_image = Solid("#000")
    white_image = Solid("#ffffff00")

#Point and click image buttons
screen intro_pac:
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
            pos(1020, 860)
            idle "pac_escritorio_idle.png"
            hover "pac_escritorio_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "Manos a la obra.")
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
    play music "audio/bgm_opening_sequence.mp3"
    show bg ncrptd productions opening title at opening_image_size
    with fadeHold
    show bg members at opening_image_size
    with fadeHold
    show bg game logo at opening_image_size
    with fadeHoldGameLogo
    # show pruebadiosqueande
    # "this video has ended"
    stop music fadeout 1.0
    
label carlos_closed_eyes_scene:
    
    scene black
    play sound "sfx_alarm.mp3"
    "*BEEP* *BEEP"
    #TODO: Meter audio de alarma
    show bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeopen
    hide bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeclose
    show bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeopen
    hide bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeclose
    show bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeopen
    hide bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with eyeclose

label carlos_bedroom_ceiling_sequence:
    scene bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with fade
    #TODO: Meter audio de suspiro corto
    play sound "sfx_short_sigh.mp3"
    "??" "Que calvario..."
    "??" "Cada vez estoy más cerca de descubrir a ese asesino."
    "??" "Solo espero que ese rarito y el disléxico de mierda no me molesten."
    play sound "sfx_bed_sheets.mp3"
    #TODO: Meter audio de correr sábanas

label carlos_bedroom_scene:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos normal  at characters_half_size_placed_at_left
    show edgar normal  at edgar_placed_at_right
    with fade
    "??" "Hola, Edgar. ¿Cómo amaneciste?"
    Edgar "Glup."
    "??" "Por supuesto que bien. Si te cambié el agua y di de comer."
    Edgar "..."
    "??" "No digas nada más, mi querido Edgar. Tengo trabajo que hacer."

label start_point_and_click:
    scene bg habitacion carlos at carlos_bedroom_background_size
    play music "audio/bgm_carlos_bedroom.mp3"
    "{i}Explora la habitación o ve al escritorio.{/i}"

    call screen intro_pac

#point and click action end scenes

#Left library

label left_library_action_pac:
    scene bg biblioteca izquierda detalle at carlos_bedroom_left_library
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
    scene bg biblioteca derecha detalle at carlos_bedroom_right_library
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
    "??" "¡Las secuelas nunca existieron!."
    call right_library_action_pac

#

label edgar_action_pac:
    Edgar "Glup."
    show carlos smirk at characters_half_size_placed_at_right
    "??" "Tú lo has dicho, amigo."
    call start_point_and_click

label bed_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_right
    "??" "No estoy cansado aún."
    call start_point_and_click

label desk_action_pac:
    stop music fadeout 1.0
    "??" "Manos a la obra"
    #TODO: Sonido campana notificación
    play sound "sfx_phone_notification.mp3"
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    "¡TIN!"
    #TODO: Sonido Suspiro corto
    play sound "sfx_short_sigh.mp3"
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    "??" "Te juro por Dios, si llega a ser Justo..."
    
    show carlos telefono neutral at characters_half_size_placed_at_right_no_transition
    nvl_narrator "1 mensaje nuevo"
    justo_phone_nvl "Carlos, hola, junto a Guillermo demos hescubierto algo increíble, ¿Quieres a la casa de Guillermo venir?."

    #Muestro teléfono, mensaje de Justo :D
    # Justo "Carlos, hola, junto a Guillermo demos hescubierto algo increíble, ¿Quieres a la casa de Guillermo venir?."
    show carlos telefono furioso at characters_half_size_placed_at_right_no_transition
    play sound "sfx_carlos_frustrated.mp3"
    Carlos "¡NO! ¡ESTE RETARDADO NO!"
    hide carlos telefono furioso with dissolve
    show edgar hiding at edgar_placed_at_right
    Edgar "Glup."
    hide edgar hiding
    show carlos telefono neutral at characters_half_size_placed_at_center
    Carlos "Ni me voy a molestar. Lo voy a bloquear."
    nvl_narrator "Bloqueaste a este contacto."
    show carlos sigh at characters_half_size_placed_at_center
    Carlos "..."
    scene bg habitacion carlos at carlos_bedroom_background_size with fade
    show carlos annoyed at characters_half_size_placed_at_center_no_transition
    Carlos "¡No se puede ser tan idiota!"

# label tutorial:
#     scene black
#     with fade
#     call decryption("tres tristes tigres comen trigo en un trigal")
#     return
    
label end:
    
    #Phone conversation start
    # e_nvl "who's this?"
    # carlos_phone_nvl e2m1_b "haha, silly you"
    # carlos_phone_nvl e1m2_b "We talked about showing off the phone the other day, remember?"
    # e_nvl "it's today? {image=emoji/fear.png}"
    # e_nvl "oops sorry night', I forgot {image=emoji/sweat.png}"
    # carlos_phone_nvl "No problem, you must be quite busy!"
    # carlos_phone_nvl e2m2_b "congrat on showing the emoji tho {image=emoji/clap.png}"
    # e_nvl "Nothing magical, it's just a {a=https://www.renpy.org/doc/html/text.html#text-tag-image}image tag{/a} :)"
    # carlos_phone_nvl e1m2 "But since we use regular renpy, we can use the same principle to send pictures!"
    # e_nvl "Right! Let me take a selfie {image=emoji/camera.png}"
    # show nighten e1m2_b
    # e_nvl "{image=EileenSelfieSmall.png}"
    # carlos_phone_nvl e2m1_b "awww, you look fantastic!"
    # show nighten e2m2_b
    # e_nvl "A bit low res but hey, the pic has to fit the screen somehow"
    
    # carlos_phone_nvl "Thank you Eileen for doing this demo with me!"
    # e_nvl "no problem, I hope people will make good use of it!"
    # e_nvl "byyee {image=emoji/wave.png}"


    # show nighten:
    #     ease 0.5 xalign 0.5 

    # n e1m2 "That's it for the demo!"
    # n normal e1m2 "Do you have any question?"

    return

#