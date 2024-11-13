#Characters

define Carlos = Character('Carlos', color= "#e2b520")
define Edgar = Character('Edgar', color= "#14d1d1")
define Justo= Character('Justo', color= "#bd4acc")
define Guillermo= Character('Guillermo', color= "#db4141")
define AlZodiak= Character('Al Zodiak', color= "#47b947")

#Phone characters and variables
define carlos_phone_nvl = Character("Carlos", kind=nvl, image="nighten", callback=Phone_SendSound)
define justo_phone_nvl = Character("Justo", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Snow shader variables
image splashbg= Color("#FBF0D9")
image snow1 = Fixed(SnowBlossom("gui/dreaming particle 1.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image snow2 = Fixed(SnowBlossom("gui/dreaming particle 2.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image snow3 = Fixed(SnowBlossom("gui/dreaming particle 3.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image rain = Fixed(SnowBlossom("gui/raindrop.png", 50, xspeed=(-600, -1000), yspeed=(1000,1600), start=10))
image rainback:
    "gui/rain1.png"
    pause 0.1
    "gui/rain2.png"
    pause 0.1
    repeat
#

# Videos

image carloswakingupvideo = Movie(play="images/videos/carloswakingup.webm", size=(1920,1080))
image opening_sequence_video = Movie(play="images/videos/opening_sequence.webm", size=(1920,1080))

default day_time = True
default day = 1
default time_of_day = ["morning", "noon", "evening", "night"] # edit this list to rename, add or delete time of days
define end_of_day = "night" # set this as the last time of day before new day begins
#default end_of_day = time_of_day[-1] # this can automatically pick up the last element of time_of_day as above, remove above line if you want to use this.


#Day cicle label
label advance(increment = 1):
    python:
        while increment > 0:
            if time_of_day[0] == end_of_day:
                day += 1
            time_of_day.append(time_of_day.pop(0))
            increment -= 1
    return

init:

#Custom image sizes
    transform video_formatter:
        zoom 1.5
        align((0.0, 0.0))
    transform pac_custom_library_zoom:
        zoom 1.37

    transform opening_image_size: #Opening text size adjustment
        xalign 0.5
        yalign 0.5

    transform characters_half_size_placed_at_left: 
        zoom 0.5
        pos (-10, 350) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3  # Shake right and down again # Move to the right over 2 seconds
        # easeinout 2.0 xalign 0.5  # Optionally ease the character to the center after

    transform characters_half_size_placed_at_center: 
        zoom 0.5
        # xalign .5
        ypos 350
        
        linear .25 xalign .6  # Shake right and down again  # Move to the right over 2 seconds
        # pos (600, 350)

    transform characters_half_size_placed_at_right: 
        zoom 0.5
        xpos 900
        ypos 350
        # pos (900, 350)
        linear .25 xalign .8  # Shake right and down again

    transform characters_half_size_placed_at_right_no_transition: 
        zoom 0.5
        xalign .8
        ypos 350
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again

    transform characters_half_size_placed_at_left_no_transition: 
        zoom 0.5
        xalign .3
        ypos 350
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        # pos (-5, 350) # pos (300, 500)

    transform characters_half_size_placed_at_center_no_transition: 
        zoom 0.5
        ypos 350
        xalign .6
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        
    transform edgar_placed_at_right:
        zoom 0.35
        pos (2350, 370) # pos (1650, 370)
        linear .25 xalign .75

    transform edgar_placed_at_left:
        zoom 0.35
        pos (400, 300)

    transform characters_zoomed_placed_at_right: 
        zoom 0.7
        
        pos (300, 400)

    transform custom_background_size: 
        zoom 2.7
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
        
    transform phone_placed_at_left_shake:
        zoom 1
        pos (-10, 125)  # Initial position of the sprite
        xalign .3
        # Vibrate every 3 seconds (alternating x and y offsets)
        linear 0.090 xoffset -10 yoffset -10  # Shake left and up
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down
        linear 0.090 xoffset -10 yoffset -10  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        pause .5  # Pause for 3 seconds before starting the next shake cycle
        repeat

    transform phone_placed_at_left_jump:
        zoom 1
        ypos 125 # pos (300, 500)
        xalign .3
        # Move the character across the screen (to the right)
        linear 0.090 xoffset -25 yoffset -25  # Shake left and up again
        linear 0.090 xoffset +25 yoffset +25  # Shake right and down again

    transform phone_placed_at_left_no_shake:
        zoom 1
        pos (-10, 125) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3
    
    transform dreaming_background:
        zoom 1.5
        pos(0, 0)
    
    transform cryptogram_symbol: 
        xpos 0
        ypos 100

    transform door_centered:
        zoom 3.2
        align(0.5, 0.8)

    transform day_cicle_bedroom_sizes:
        zoom 1.5
        align((0.0, 0.0))
#

init python: 

    isintutorial = False

    day_cicle_transforms=[
        day_cicle_bedroom_sizes
    ]

    elements_behind=[
        'bedroom_background'
    ]

    def show_day_cycle():
        renpy.scene()
        renpy.show("bg hab carlos w transparency", at_list=day_cicle_transforms, layer='master', what=None, zorder=1, tag="bedroom_background", behind=[])
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg night", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.scene()
        # show bg night at custom_background_size
        # pause (.5)
        # show bg day zorder 1
        # pause (.5)
        # show bg hab carlos w transparency at custom_background_size onlayer screens

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

screen gradient_background():
    # Draw the gradient (we'll use a linear gradient from top to bottom)
    python:
        import pygame
        import renpy
        
        # Get the dimensions of the screen
        width, height = renpy.config.screen_width, renpy.config.screen_height

        # Create a surface for the gradient
        gradient_surface = pygame.Surface((width, height))

        # Get the elapsed time in seconds since the game started
        elapsed_time = renpy.get_time_since_start()  # This gives the time in seconds
        
        # Loop through each pixel and change the color over time
        for y in range(height):
            # Create a gradient based on the current time and position
            t = (y + (elapsed_time * 0.05)) % 255  # Oscillate between 0 and 255
            r = int(255 * t / 255)  # Red channel
            g = int(255 * (255 - t) / 255)  # Green channel
            b = 255  # Blue channel stays constant
            
            # Set the color for the pixel at the current position
            for x in range(width):
                gradient_surface.set_at((x, y), (r, g, b))

        # Draw the surface to the screen
        renpy.display.draw(gradient_surface, (0, 0))

#scene management

label start:
    
    show opening_sequence_video at video_formatter
    pause(14.3)
    jump carlos_closed_eyes_scene
    
label carlos_closed_eyes_scene:
    
    scene black
    play music "sfx_alarm.mp3"
    "BEEP BEEP"
    play sound "sfx_slam_desk.mp3"
    stop music fadeout 1.0
    window hide
    show carloswakingupvideo at video_formatter
    pause(4.3)
    jump carlos_bedroom_ceiling_sequence

label carlos_bedroom_ceiling_sequence:
    scene bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with fade
    play sound "images/sfx_short_sigh.mp3"
    "???" "Que calvario..."
    "???" "Cada vez estoy más cerca de descubrir a ese asesino."
    "???" "Solo espero que ese rarito y el lerdo no me molesten."
    play sound "sfx_bed_sheets.mp3"
    jump carlos_bedroom_scene

label carlos_bedroom_scene:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos normal  at characters_half_size_placed_at_left
    show edgar normal  at edgar_placed_at_right
    with fade
    play music "audio/bgm_carlos_bedroom.mp3"
    "???" "Hola, Edgar. ¿Cómo amaneciste?"
    Edgar "Glup{nw=.25}."
    show carlos smirk  at characters_half_size_placed_at_left_no_transition
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
    $ isintutorial = True
    
    play sound "sfx_paper_tearing.mp3"
    pause(0.5)
    play sound "sfx_scissors.mp3"
    call decryption("a") from _call_decryption

label tutorial_end:
    $ isintutorial = False
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos annoyed at characters_half_size_placed_at_left
    Carlos "¿Qué?"
    Carlos "¿\"Tres tristes tigres\"? ¿El trabalenguas?"
    play sound "smirk.mp3"
    show carlos smirk at characters_half_size_placed_at_left_no_transition
    Carlos "No es de extrañar. Al Asesino le gusta jugar con los detectives."
    jump guillermo_call

label guillermo_call:
    play sound "sfx_phone_vibrating.mp3"
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    hide carlos annoyed
    Carlos "¿Y ahora qué?"
    show phone receiving guillermo call at phone_placed_at_left_shake
    show carlos telefono furioso at characters_half_size_placed_at_right
    Carlos "¡No puede ser! ¡A falta de uno, el otro!"
    play sound "sfx_phone_vibrating.mp3"
    Carlos "¿Vale la pena que le conteste, Edgar?"
    hide carlos telefono furioso
    show edgar toc at edgar_placed_at_right
    Edgar "Glup."
    hide edgar toc
    play sound "sfx_short_sigh.mp3"
    show carlos telefono neutral at characters_half_size_placed_at_right
    Carlos "Solo porque tú lo dijiste, Edgar."
    hide phone receiving guillermo call
    show phone guillermo active call at phone_placed_at_left_jump
    show carlos telefono furioso at characters_half_size_placed_at_right
    Guillermo "¡HOLA, CARLITOOOOOOOS! ¿¡CÓMO ESTÁS!?"
    Carlos "..."
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "¿Hola? ¿Estás ahí?"
    Carlos "Sí, aquí estoy. ¿Qué quieres?"
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "Estoy en mi casa con Justo, y encontramos algo \"de otro mundo\"."
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "Es el desafío perfecto para ti, Rey de los Criptogramas. ¿Vienes?"
    menu:
        "Quedarme en casa.":
            jump act_I_choice_stay_home
        "Ir.":
            jump act_I_choice_go
    jump end_game
    
label act_I_choice_stay_home:
    # TODO: Poner sprite gritando AL TELÉFONO
    Carlos "No, no y un millón de veces no. ¡La última vez que me dijiste algo así, estuviste dos horas hablándome sobre la tierra plana!"
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "¡Vamos, amigo! ¡Sabes que es verdad!"
    # TODO: Poner sprite gritando AL TELÉFONO
    Carlos "¡NO!"
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "Te arrepentirás si no vienes, ¡Créeme!"
    show carlos telefono furioso at characters_half_size_placed_at_right_no_transition
    Carlos "Tengo cosas que hacer. No me llames."
    hide phone guillermo active call
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "Qué calvario..."
    show carlos normal at characters_half_size_placed_at_right_no_transition
    Carlos "Edgar, ¿Por qué siempre que estoy por trabajar viene un idiota a robarme tiempo?"
    hide carlos normal
    show edgar toc at edgar_placed_at_right
    Edgar "Glup."
    hide edgar toc
    show carlos sigh at characters_half_size_placed_at_right
    Carlos "Bueno, a seguir con los criptogramas..."

label start_impossible_cryptogram:

    play sound "sfx_paper_tearing.mp3"
    pause(0.5)
    play sound "sfx_scissors.mp3"
    call decryption("sda") from _call_decryption_1

label act_I_choice_go:
    Carlos "Esto es lo que sucede si Carlos acepta ir con los pibardox."
    $ renpy.quit()

label carlos_stops_cryptogram_abruptly:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos annoyed at characters_half_size_placed_at_left
    Carlos "..."
    hide carlos annoyed
    show edgar normal at edgar_placed_at_right
    Edgar "Glup."
    show carlos annoyedspeech at characters_half_size_placed_at_left
    Carlos "No, Edgar. Yo jamás."
    Carlos "JAMÁS pediría ayuda. Solo... Necesito descansar. Hablar con Guillermo me agotó mentalmente."
    jump carlos_dream

label carlos_dream:
    scene bg dreaming at dreaming_background
    with dissolve
    show snow1
    show snow2
    show snow3
    # TODO: Agregar array de sprites de simbolos
    Carlos "Sí... Sí, eso es."
    Carlos "Te voy a encontrar. Voy a saber quién eres. Solo yo. Nadie más."
    Carlos "Así me haré famoso y podré vivir lejos. Lejos de esos infelices."
    play sound "doorbell.mp3"
    Carlos "Ahora muéstrate. ¡Muéstrate, mierda!"
    jump ringing_bell_carlos_house

label ringing_bell_carlos_house:
    play sound "doorbell.mp3"
    scene bg habitacion carlos at carlos_bedroom_background_size
    with fade
    play sound "doorbell.mp3"
    show carlos furious at characters_half_size_placed_at_left #TODO: Poner sprite carlos gritando (no al telefono)
    Carlos "¡NO, NO, NO!"
    play sound "doorbell.mp3"
    Carlos "¡YA TE ESCUCHÉ, MIERDA!"
    jump pasillo_casa_carlos

label pasillo_casa_carlos:
    play music "doorbell.mp3"
    scene bg pasillo at custom_background_size with fade
    Carlos "¿Quién es...?"
    call screen hall_door_pac

label wait_until_open_door:
    Carlos "{i}Si no hago nada, eventualmente se irán...{i}"
    scene bg pasillo at custom_background_size with fade
    stop music
    play sound "sfx_short_sigh.mp3"
    Carlos "Por fin..."
    play music "doorbell.mp3"
    play sound "sfx_knocking_on_door_desperately.mp3"
    call screen hall_door_calling_continuously_pac

label sidewalk_scene_act_II:
    stop music
    play music "sfx_door_lock_unlock.mp3"
    play sound "sfx_door_open.mp3"
    pause(.5)
    stop music
    scene sidewalk at custom_background_size with fade
    show guillermo feliz at characters_half_size_placed_at_center
    show justo feliz at characters_half_size_placed_at_right
    Guillermo "¡Carlitos!"
    Justo "Hola, Calos.{nw=.25}"
    show carlos annoyedspeech at characters_half_size_placed_at_left
    Carlos "¿Qué carajos quieren?"
    show guillermo neutral at characters_half_size_placed_at_center_no_transition
    Guillermo "Lo que te dije por llamada. ¡Ven con nosotros a mi casa! ¡Tenemos algo que te va a encantar!"
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    Carlos "{i}No puedo creerlo. Casi me tiran la puerta, y tocaron mi timbre de esa manera...{i}"
    Carlos "¿Qué debería hacer?"
    jump decision_act_II_sidewalk

label decision_act_II_sidewalk:
    menu:
        "Echarlos.":
            jump response_shove_away_friends_act_II
        "Ceder.":
            jump response_go_with_friends_act_II

label response_shove_away_friends_act_II:
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    Carlos "¿Qué te hace pensar que me interesa ir?"
    Carlos "¡Ni siquiera me explicaron qué es eso que encontraron! Dios santo, ¡¿Tienen alguna foto, siquiera!?"
    show guillermo triste at characters_half_size_placed_at_center_no_transition
    Guillermo "Bueno, no, pero..."
    show justo pensativo at characters_half_size_placed_at_right_no_transition
    Justo "Tampoco es que nos hayas pedido una foto en su momento."
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    Carlos "¿Qué dijiste?"
    show justo nervioso at characters_half_size_placed_at_right_no_transition
    Justo "Me lefiero a que si bien no oculió se nos... Digo... A que si bien no se nos ocurrió... Tú tampoco lo suge-sugeriste..."
    show justo confundido at characters_half_size_placed_at_right_no_transition
    Justo "Y esto algo es que tiene que ver con los... Cli-clipto... Gramas..."
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    Carlos "Se dice \"Criptogramas\"."
    show justo triste at characters_half_size_placed_at_right_no_transition # TODO: Poner esto en el guión
    Carlos "Ni para decir la R sirves..."
    show guillermo angry at characters_half_size_placed_at_center_no_transition
    Guillermo "¡Bueno, es suficiente!"
    Guillermo "¡¿Cuál es tu problema con nosotros, Carlos!?"
    show carlos puzzled at characters_half_size_placed_at_left_no_transition
    Carlos "¿Mi problema? ¿En serio?"
    # TODO: Reemplazar sprite carlos gritando
    show carlos furious at characters_half_size_placed_at_left_no_transition
    Carlos "¡USTEDES SON LOS IMBÉCILES QUE INVADEN MI CASA, A PESAR DE QUE LES DIJE MÁS DE UNA VEZ QUE NO VINIERAN!"
    Carlos "¡¿CUANDO VAN A ENTENDER QUE NO ME INTERESA JUNTARME CON RARITOS!?"
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    Carlos "¡Son tan inútiles! ¡Uno cree que la Tierra es plana, y el otro no puede pronunciar la R!"
    show carlos furious at characters_half_size_placed_at_left_no_transition
    Carlos "¡Y ENTRE LOS DOS NO PUEDEN PENSAR EN UNA PUTA FORMA CORRECTA DE DECIR LAS COSAS!"
    show guillermo sorprendido at characters_half_size_placed_at_center_no_transition
    Guillermo "Oh, habló el rey de Roma."
    show guillermo preocupado at characters_half_size_placed_at_center_no_transition
    Guillermo "Entiendo que puedas enojarte por las cosas en las que creo, pero..."
    Guillermo "¿Acaso crees que Justo habla así porque quiere, Carlos?"
    show guillermo triste at characters_half_size_placed_at_center_no_transition
    Guillermo "Para ser alguien que se dedica a los criptogramas, no puedes darte cuenta del esfuerzo que hace por hablarte."
    show guillermo preocupado at characters_half_size_placed_at_center_no_transition
    Guillermo "El esfuerzo que hacemos ambos, mejor dicho."
    show guillermo angry at characters_half_size_placed_at_center_no_transition
    Guillermo "Porque podremos ser raritos, pero tú eres de lejos el sujeto más arrogante, desagradable y soberbio que jamás conocí."
    Guillermo "¡Ni siquiera nos importa lo que descubrimos, solo queríamos una excusa para hablar con nuestro \"amigo\"!"
    show carlos surprised at characters_half_size_placed_at_left_no_transition
    Guillermo "¡Pero diablos, es una gran ironía llamarte así, porque no lo mereces!"
    show guillermo triste at characters_half_size_placed_at_center_no_transition
    Guillermo "Vámonos, Justo."
    hide guillermo triste
    hide justo triste
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    Carlos "..."
    show carlos furious at characters_half_size_placed_at_left_no_transition
    Carlos "¡BIEN! Después de todo ¡NO LOS NECESITO!"
    play audio "sfx_door_slam.mp3"
    jump carlos_bedroom_endgame

label carlos_bedroom_endgame:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show carlos sigh at characters_half_size_placed_at_right
    Carlos "..."
    show carlos furious at characters_half_size_placed_at_right_no_transition
    Carlos "¡NO PUEDO CREER QUE ESTOS DOS INEPTOS NO ME TOMEN ENSERIO! ¡ME TIENEN HARTO!"
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    Carlos "Primero ese maldito disléxico que no sabe conjugar dos palabras bien ni pronunciar debidamente la letra \"R\"."
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    Carlos "Luego el \"Señor melodrama\", tomando la postura de héroe que defiende a sus amigos, como si fuera la persona más correcta del planeta..."
    show carlos furious at characters_half_size_placed_at_right_no_transition
    Carlos "¡PLANETA EL CUAL CREE ROTUNDAMENTE QUE ES PLANO! ¿¡QUÉ CLASE DE SIMIO CREE TAN FERVIENTEMENTE EN TAN ABSURDAS PATRAÑAS!?"
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    Carlos "¡Lamento desde lo más profundo de mi corazón haberlos conocido! ¡Son el par más molesto e incompetente que vi en toda mi vida!"
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    Carlos "..."
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "Bueno, volvamos a lo que respecta..."
    jump act_II_final_scene

label act_II_final_scene:
    $ show_day_cycle()
    scene bg habitacion carlos at carlos_bedroom_background_size
    with fade
    play sound "sfx_phone_notification.mp3"
    "¡TIN!"
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    Carlos "..."
    play sound "sfx_short_sigh.mp3"
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "Te juro por Dios, si llega a ser ese par..."
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    Carlos "..."
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    Carlos "¿Una noticia internacional?"
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    Carlos "\"Dos adolescentes encuentran una nave espacial y ganan fama mundial...\""
    show carlos surprised at characters_half_size_placed_at_right_no_transition
    Carlos "No... No... No..."
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    show phone newspaper at phone_placed_at_left_no_shake
    Carlos "¡No puede ser! ¡¿Por qué no les creí?! ¡Soy un idiota!"
    show carlos annoyed at characters_half_size_placed_at_right_no_transition
    Carlos "Mi mayor sueño... Volverme famoso... Arrebatado por ese par de inadaptados mentales..."
    show carlos 2ndpose at characters_half_size_placed_at_right_no_transition
    Carlos "Si tan solo hubiera ido con ellos... Si tan solo..."
    show carlos sigh at characters_half_size_placed_at_right_no_transition #TODO: Poner sonido inspiración (De respirar)
    Carlos "..."
    play sound "sfx_rage_scream.mp3"
    with Shake((0, 0, 0, 0), .5, dist=30)
    # TODO: Poner sonido grito de furia
    show carlos furious at characters_half_size_placed_at_right_no_transition
    Carlos "¡MALDICIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOON!"
    jump neutral_ending_endgame_screen

label neutral_ending_endgame_screen:
    play music "audio/bgm_opening_sequence.mp3"
    scene black
    with fade
    show bg neutral ending at opening_image_size
    jump end_game

label response_go_with_friends_act_II:
    Carlos "Bueno pibes son lo más nunca cambien saludos ;)"
    jump end_game
label end_game:
    # hide screen End
    "Thank you for playing!"
    $ MainMenu(confirm=False)()