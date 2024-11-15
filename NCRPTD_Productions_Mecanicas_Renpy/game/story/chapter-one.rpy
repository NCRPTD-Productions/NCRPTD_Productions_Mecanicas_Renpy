label opening_sequence_and_intro:
    show opening_sequence_video at video_formatter
    pause(14.3)
    jump carlos_closed_eyes_scene
    return

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
    return

label carlos_bedroom_ceiling_sequence:
    scene bg techo habitacion carlos right at carlos_corner_bedroom_background_size
    with fade
    play sound "images/sfx_short_sigh.mp3"
    "???" "Que calvario..."
    "???" "Cada vez estoy más cerca de descubrir a ese asesino."
    "???" "Solo espero que ese rarito y el lerdo no me molesten."
    play sound "sfx_bed_sheets.mp3"
    jump carlos_bedroom_scene
    return

label carlos_bedroom_scene:
    # call show_ui_button
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
    return


label start_point_and_click:
    scene bg habitacion carlos at carlos_bedroom_background_size
    "{i}Explora la habitación o ve al escritorio.{/i}"
    call screen intro_pac

label topdown_view_desk_scene:

    call screen carlos_desktop_pac
    return

    #desk point and click action sequences


label tutorial_start:
    $ isintutorial = True
    
    play sound "sfx_paper_tearing.mp3"
    pause(0.5)
    play sound "sfx_scissors.mp3"
    call decryption("a") from _call_decryption
    return

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
    return

label guillermo_call:
    play sound "sfx_phone_vibrating.mp3"
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    hide carlos annoyed
    Carlos "¿Y ahora qué?"
    show phone receiving guillermo call at phone_placed_at_left_shake
    show carlos telefono furioso at characters_half_size_placed_at_right_no_transition
    Carlos "¡No puede ser! ¡A falta de uno, el otro!"
    play sound "sfx_phone_vibrating.mp3"
    Carlos "¿Vale la pena que le conteste, Edgar?"
    hide carlos telefono furioso
    show edgar toc at edgar_placed_at_right
    Edgar "Glup."
    hide edgar toc
    play sound "sfx_short_sigh.mp3"
    show carlos telefono neutral at characters_half_size_placed_at_right_no_transition
    Carlos "Solo porque tú lo dijiste, Edgar."
    hide phone receiving guillermo call
    show phone guillermo active call at phone_placed_at_left_jump
    show carlos telefono furioso at characters_half_size_placed_at_right_no_transition
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
    return
    
label act_I_choice_stay_home:
    # TODO: Poner sprite gritando AL TELÉFONO
    Carlos "No, no y un millón de veces no. ¡La última vez que me dijiste algo así, estuviste dos horas hablándome sobre la tierra plana!"
    show phone guillermo active call at phone_placed_at_left_jump
    Guillermo "¡Vamos, amigo! ¡Sabes que es verdad!"
    # TODO: Poner sprite gritando AL TELÉFONO
    Carlos "¡NO!"
    show phone guillermo active call at phone_placed_at_left_jump
    show carlos telefono neutral at characters_half_size_placed_at_right_no_transition
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
    play sound "sfx_short_sigh.mp3"
    show carlos sigh at characters_half_size_placed_at_right
    Carlos "Bueno, a seguir con los criptogramas..."
    jump start_impossible_cryptogram
    return

label start_impossible_cryptogram:

    play sound "sfx_paper_tearing.mp3"
    pause(0.5)
    play sound "sfx_scissors.mp3"
    call decryption("sda") from _call_decryption_1
    return

label act_I_choice_go:
    play sound "sfx_short_sigh.mp3"
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "Está bien... Iré... "
    show carlos annoyed at characters_half_size_placed_at_right_no_transition
    Guillermo "¡SEEEEEEEHHHHHHH!"
    Guillermo "¡Ven cuanto antes! ¿Aún tienes mi dirección?"
    show carlos telefono neutral at characters_half_size_placed_at_right_no_transition
    Carlos "Creo que sí. En fin, te veré en un rato."
    Guillermo "¡GENIAL! ¡Justo, adivina! Carlos dijo que-{nw=0.75}"
    play sound "sfx_hang_up_call.mp3"
    hide phone guillermo active call
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    Carlos "¿En qué me metí, Edgar?"
    hide carlos sigh
    show edgar toc at edgar_placed_at_left
    Edgar "Glup."
    hide edgar toc
    show carlos annoyedspeech at characters_half_size_placed_at_right_no_transition
    Carlos "Lo sé, lo sé. Yo acepté."
    Carlos "Si llega a ser como la última vez, lo mato."
    show carlos thoughtful at characters_half_size_placed_at_right_no_transition
    Carlos "{i}Tal vez en mi teléfono aún tenga guardada la dirección de la casa de Guillermo.{i}"
    hide carlos thoughtful
    jump carlos_bedroom_navigation_gui
    return
    # call handle_carlos_phone_ui_button
    # Carlos "asjdlasjdlkasjldk"
    # $ renpy.quit()

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
    return

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
    Carlos "Ahora muéstrate. ¡Muéstrate!"
    jump ringing_bell_carlos_house
    return

label ringing_bell_carlos_house:
    play sound "doorbell.mp3"
    scene bg habitacion carlos at carlos_bedroom_background_size
    with fade
    play sound "doorbell.mp3"
    show carlos furious at characters_half_size_placed_at_left #TODO: Poner sprite carlos gritando (no al telefono)
    Carlos "¡NO, NO, NO!"
    play sound "doorbell.mp3"
    Carlos "¡YA TE ESCUCHÉ!"
    jump pasillo_casa_carlos
    return

label pasillo_casa_carlos:
    play music "doorbell.mp3"
    scene hallway_carlos at custom_hallway_background_size with fade
    Carlos "¿Quién es...?"
    call screen hall_door_pac

label wait_until_open_door:
    scene hallway_carlos at custom_hallway_background_size with fade
    stop music
    Carlos "{i}Si no hago nada, eventualmente se irán...{i}"
    play sound "sfx_short_sigh.mp3"
    Carlos "Por fin..."
    play music "doorbell.mp3"
    play sound "sfx_knocking_on_door_desperately.mp3"
    call screen hall_door_calling_continuously_pac
    return

label sidewalk_scene_act_II:
    stop music
    play music "sfx_door_lock_unlock.mp3"
    play sound "sfx_door_open.mp3"
    pause(.5)
    stop music
    scene sidewalk at sidewalk_size
    show guillermo feliz at characters_half_size_placed_at_center
    show justo feliz at characters_half_size_placed_at_right
    Guillermo "¡Carlitos!"
    Justo "Hola, Calos.{nw=.25}"
    show carlos annoyedspeech at characters_half_size_placed_at_left
    Carlos "¿Qué diablos quieren?"
    show guillermo neutral at characters_half_size_placed_at_center_no_transition
    Guillermo "Lo que te dije por llamada. ¡Ven con nosotros a mi casa! ¡Tenemos algo que te va a encantar!"
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    Carlos "{i}No puedo creerlo. Casi me tiran la puerta, y tocaron mi timbre de esa manera...{i}"
    Carlos "¿Qué debería hacer?"
    jump decision_act_II_sidewalk
    return

label decision_act_II_sidewalk:
    menu:
        "Echarlos.":
            jump response_shove_away_friends_act_II
        "Ceder.":
            jump response_go_with_friends_act_II
    return

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
    return

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
    return

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
    scene black
    jump neutral_ending_endgame_screen
    return

label neutral_ending_endgame_screen:
    play music "audio/bgm_opening_sequence.mp3"
    scene black
    with fade
    show bg neutral ending at opening_image_size
    jump end_game
    return

label response_go_with_friends_act_II:
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    show guillermo roblox face at characters_half_size_placed_at_center_no_transition
    show justo complacido at characters_half_size_placed_at_right_no_transition
    Carlos "Hmmm..."
    show carlos annoyedspeech at characters_half_size_placed_at_left_no_transition 
    Carlos "Está bien, iré. Pero deja de hacer esa cara, Guillermo."
    show guillermo feliz at characters_half_size_placed_at_center_no_transition
    show justo feliz at characters_half_size_placed_at_right_no_transition
    Guillermo "¡SIII!"
    Justo "¡YAY!"
    show justo complacido at characters_half_size_placed_at_right_no_transition
    show guillermo roblox face at characters_half_size_placed_at_center_no_transition
    Guillermo "Pero no te pongas nerviosa, Carlos."
    show carlos furious at characters_half_size_placed_at_left_no_transition
    show justo neutral at characters_half_size_placed_at_right_no_transition
    Carlos "¡BASTA!"
    show guillermo roblox face at characters_half_size_placed_at_center_no_transition
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    show justo feliz at characters_half_size_placed_at_right_no_transition
    Guillermo "Espléndido."
    show guillermo neutral at characters_half_size_placed_at_center_no_transition
    Guillermo "Vamos de una vez, yo los guío. "
    jump chapter_II_guillermo_bedroom_no_pac
    return

label end_game:
    # hide screen End
    "Thank you for playing!"
    $ MainMenu(confirm=False)()
    return