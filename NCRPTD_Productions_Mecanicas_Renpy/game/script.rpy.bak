#Characters

define Carlos = Character('Carlos', color= "#e2b520")
define Edgar = Character('Edgar', color= "#14d1d1")
define Justo= Character('Justo', color= "#bd4acc")
define Guillermo= Character('Guillermo', color= "#db4141")
define AlZodiak= Character('Al Zodiak', color= "#47b947")

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
        xpos 900
        ypos 350
        # pos (900, 350)
        linear .25 xalign .6

    transform characters_half_size_placed_at_right_no_transition: 
        zoom 0.5
        xalign .6
        ypos 350

    transform characters_half_size_placed_at_left_no_transition: 
        zoom 0.5
        xalign .3
        ypos 350
        # pos (-10, 350) # pos (300, 500)

    transform characters_half_size_placed_at_center_no_transition: 
        zoom 0.5
        ypos 350
        xalign .5
        
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
        
    transform phone_placed_at_left:
        zoom 1
        pos (-10, 125) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3 

#

init python: 
    
    import random
    import time
    
    # Camera Shake using Ren'Py's built-in Shake transition
    # def camera_shake(intensity=10, duration=0.5):
    #     """
    #     Apply a shake effect to the screen using the built-in Shake transition.

    #     intensity: How intense the shake is (higher value = more movement).
    #     duration: How long the shake lasts (in seconds).
    #     """
    #     # Apply the shake effect to the screen
    #     shake = Shake(intensity, duration)
    #     renpy.pause(duration, hard=True)
    #     return shake
    # def eyewarp(x):
    #     return x**3
    # black_image = Solid("#000")
    # white_image = Solid("#ffffff00")

    #Camera Shake
    #
    
    #Point and click text display hover
screen displayTextScreen:  
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
    #    

#

#scene management

label start:
    play music "audio/bgm_opening_sequence.mp3"
    show bg ncrptd productions opening title at opening_image_size
    #TODO: Cambiar texto de sprite a "De la mano de"
    with fadeHold
    show bg members at opening_image_size
    with fadeHold
    show bg game logo at opening_image_size
    with fadeHoldGameLogo
    # show pruebadiosqueande
    # "this video has ended"
    stop music fadeout 1.0
    jump carlos_closed_eyes_scene
    
label carlos_closed_eyes_scene:
    
    scene black
    play sound "sfx_alarm.mp3"
    "BEEP *BEEP"
    #TODO: Meter audio de golpe seco
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
    jump carlos_bedroom_ceiling_sequence

label carlos_bedroom_ceiling_sequence:
    scene bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with fade
    #TODO: Meter audio de suspiro corto
    play sound "sfx_short_sigh.mp3"
    "???" "Que calvario..."
    "???" "Cada vez estoy más cerca de descubrir a ese asesino."
    "???" "Solo espero que ese rarito y el disléxico de mierda no me molesten."
    play sound "sfx_bed_sheets.mp3"
    #TODO: Meter audio de correr sábanas
    jump carlos_bedroom_scene

label carlos_bedroom_scene:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos normal  at characters_half_size_placed_at_left
    show edgar normal  at edgar_placed_at_right
    with fade
    play music "audio/bgm_carlos_bedroom.mp3"
    "???" "Hola, Edgar. ¿Cómo amaneciste?"
    Edgar "Glup."
    show carlos smirk  at characters_half_size_placed_at_left
    "???" "Por supuesto que bien. Si te cambié el agua y di de comer."
    show edgar hiding at edgar_placed_at_right
    Edgar "..."
    "???" "No digas nada más, mi querido Edgar. Tengo trabajo que hacer."
    jump start_point_and_click


label start_point_and_click:
    scene bg habitacion carlos at carlos_bedroom_background_size
    "{i}Explora la habitación o ve al escritorio.{/i}"
    call screen intro_pac

label topdown_view_desk_scene:

    scene bg habitacion carlos at carlos_bedroom_background_size
    Carlos "Por fin. A trabajar..."
    call screen carlos_desktop_pac

    #desk point and click action sequences

label tutorial_start:
    call decryption("holanda")

label tutorial_end:
    
    #TODO: Agregar sonido teléfono vibrando
    # scene black
    # with fade
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos annoyed at characters_half_size_placed_at_left
    Carlos "¿Qué?"
    Carlos "¿Tres tristes tigres? ¿El trabalenguas?"
    #TODO: Poner sonido de smirk
    show carlos smirk at characters_half_size_placed_at_left_no_transition
    Carlos "No es de extrañar. Al Asesino le gusta jugar con los detectives."
    jump guillermo_call

label guillermo_call:
    #TODO: Poner sonido vibración llamada
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    hide carlos annoyed
    Carlos "¿Y ahora qué?"
    show phone guillermo active call at phone_placed_at_left
    show carlos telefono furioso at characters_half_size_placed_at_right
    Carlos "¡No puede ser! ¡A falta de uno, el otro!"
    Carlos "¿Vale la pena que le conteste, Edgar?"
    hide carlos telefono furioso
    show edgar toc at edgar_placed_at_right
    Edgar "Glup."
    hide edgar toc
    play sound "sfx_short_sigh.mp3"
    show carlos telefono neutral at characters_half_size_placed_at_right
    Carlos "Solo porque tú lo dijiste, Edgar."
    hide phone guillermo active call
    show phone guillermo active call at phone_placed_at_left 
    show carlos telefono furioso at characters_half_size_placed_at_right
    Guillermo "¡HOLA, CARLITOOOOOOOS! ¿¡CÓMO ESTÁS!?"
    Carlos "..."
    Guillermo "¿Hola? ¿Estás ahí?"
    Carlos "Sí, aquí estoy. ¿Qué quieres?"
    Guillermo "Estoy en mi casa con Justo, y encontramos algo \"de otro mundo\"."
    Guillermo "Es el desafío perfecto para ti, Rey de los Criptogramas. ¿Vienes?"
    menu:
        "Quedarme en casa.":
            jump act_I_choice_stay_home
        "Ir.":
            jump act_I_choice_go
    jump end_game
    
label act_I_choice_stay_home:
    Carlos "No, no y un millón de veces no. ¡La última vez que me dijiste algo así, estuviste dos horas hablándome sobre la tierra plana!"
    Guillermo "¡Vamos, amigo! ¡Sabes que es verdad!"
    Carlos "¡NO!"
    Guillermo "Te arrepentirás si no vienes, ¡créeme!"
    Carlos "Tengo cosas que hacer. No me llames."
    hide phone guillermo active call
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "Qué calvario..."
    show carlos normal at characters_half_size_placed_at_right_no_transition
    Carlos "Edgar, ¿por qué siempre que estoy por trabajar viene un idiota a robarme tiempo?"
    hide carlos normal
    show edgar toc at edgar_placed_at_right
    Edgar "Glup."
    hide edgar toc
    show carlos sigh at characters_half_size_placed_at_right
    Carlos "Bueno, a seguir con los criptogramas..."
    jump end_game

label act_I_choice_go:
    Carlos "Esto es lo que sucede si Carlos acepta ir con los pibardox."
    $ renpy.quit()
label end_game:
    scene black
    # hide screen End
    "Thank you for playing!"
    $ renpy.quit()