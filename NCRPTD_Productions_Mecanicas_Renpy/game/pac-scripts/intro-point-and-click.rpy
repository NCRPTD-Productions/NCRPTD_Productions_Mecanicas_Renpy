init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

    transform pac_intro_left_library:
        zoom .7
        align (.216, .625)        # pos(645, 545)

    transform pac_intro_right_library:
        zoom .7
        align (.782, .66)        # pos(645, 545)

    transform pac_intro_edgar:
        zoom .35
        align (.013, .63)        # pos(645, 545)

    transform pac_intro_desk:
        zoom .7
        align (.496, .89)        # pos(645, 545)

    transform pac_intro_bed:
        zoom .83
        align (1.075, 1.34)        # pos(645, 545)

#Image buttons
screen intro_pac:

    imagebutton:
        auto "point_and_click/intro_carlos_bedroom/pac_biblioteca_izquierda_%s.png"
        # hover "point_and_click/intro_carlos_bedroom/pac_biblioteca_izquierda_hover.png"
        action [Hide("displayTextScreen"), Jump("left_library_action_pac")]
        at pac_intro_left_library
        hovered Show("displayTextScreen", displayText = "¿Leer?")
        unhovered Hide("displayTextScreen")
            
    imagebutton:
        pos(75, 845)
        auto "point_and_click/intro_carlos_bedroom/pac_edgar_%s.png"
        # hover "point_and_click/intro_carlos_bedroom/pac_edgar_hover.png"
        action [Hide("displayTextScreen"), Jump("edgar_action_pac")]
        at pac_intro_edgar
        hovered Show("displayTextScreen", displayText = "¿Hablar con Edgar?")
        unhovered Hide("displayTextScreen")

    imagebutton:
        pos(1020, 860)
        auto "point_and_click/intro_carlos_bedroom/pac_escritorio_%s.png"
        # hover "point_and_click/intro_carlos_bedroom/pac_escritorio_hover.png"
        action [Hide("displayTextScreen"), Jump("desk_action_pac")]
        at pac_intro_desk
        hovered Show("displayTextScreen", displayText = "Manos a la obra.")
        unhovered Hide("displayTextScreen")
            
    imagebutton:
        pos(1725, 545)
        auto "point_and_click/intro_carlos_bedroom/pac_biblioteca_derecha_%s.png"
        # hover "point_and_click/intro_carlos_bedroom/pac_biblioteca_derecha_hover.png"
        action [Hide("displayTextScreen"), Jump("right_library_action_pac")]
        at pac_intro_right_library
        hovered Show("displayTextScreen", displayText = "¿Leer?")
        unhovered Hide("displayTextScreen")
            
    imagebutton:
        pos(2110, 1085)
        auto "point_and_click/intro_carlos_bedroom/pac_cama_carlos_%s.png"
        # hover "point_and_click/intro_carlos_bedroom/pac_cama_carlos_hover.png"
        action [Hide("displayTextScreen"), Jump("bed_action_pac")]
        at pac_intro_bed
        hovered Show("displayTextScreen", displayText = "¿Dormir?")
        unhovered Hide("displayTextScreen")



#Point and click action end scenes

#Left library

label left_library_action_pac:
    scene bg biblioteca izquierda detalle at carlos_bedroom_left_library
    menu:
        "Figura del EVA-01.":
            jump left_library_option_EVA_01
        "El Escarabajo de oro.":
            jump left_library_option_Golden_Beetle
        "Volver.":
            jump library_option_Go_Back
    return

label left_library_option_EVA_01:
    show carlos annoyedspeech at characters_zoomed_placed_at_right
    "???" "Que te subas al maldito EVA, Shinji."
    jump left_library_action_pac
    return

label left_library_option_Golden_Beetle:
    show carlos thoughtful at characters_zoomed_placed_at_right
    "???" "Lo que me llevó a la criptografía..."
    jump left_library_action_pac
    return

label library_option_Go_Back:
    jump start_point_and_click
    return

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
    return

label right_library_option_Death_Note:
    show carlos smirk at characters_zoomed_placed_at_right
    "???" "Kira tenía razón."
    jump right_library_action_pac
    return

label right_library_option_Ryuk_Figure:
    show carlos sigh at characters_zoomed_placed_at_right
    "???" "Me saliste caro."
    jump right_library_action_pac
    return

label right_library_option_The_Psychoanalyst:
    show carlos 2ndpose at characters_zoomed_placed_at_right
    "???" "¡Las secuelas nunca existieron!."
    jump right_library_action_pac
    return

#

label edgar_action_pac:
    show edgar toc at edgar_placed_at_left
    Edgar "Glup."
    hide edgar toc
    show carlos smirk at characters_half_size_placed_at_right
    "???" "Tú lo has dicho, amigo."
    jump start_point_and_click
    return

label bed_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_right
    "???" "No estoy cansado aún."
    jump start_point_and_click
    return

label desk_action_pac:
    stop music fadeout 1.0
    play sound "sfx_phone_notification.mp3"
    "¡TIN!"
    show carlos puzzled at characters_half_size_placed_at_right_no_transition
    "???" "..."
    play sound "sfx_short_sigh.mp3"
    show carlos sigh at characters_half_size_placed_at_right_no_transition
    "???" "Te juro por Dios, si llega a ser Justo..."
    
    show carlos telefono neutral at characters_half_size_placed_at_right_no_transition
    nvl_narrator "1 mensaje nuevo"
    justo_phone_nvl "Carlos, hola, junto a Guillermo demos hescubierto algo increíble, ¿Quieres a la casa de Guillermo venir?."
    show carlos telefono furioso at characters_half_size_placed_at_right_no_transition
    Carlos "¡NO! ¡ESTE RETARDADO NO!"
    hide carlos telefono furioso with dissolve
    show edgar hiding at edgar_placed_at_right
    Edgar "Glup."
    hide edgar hiding
    show carlos telefono neutral at characters_half_size_placed_at_center
    Carlos "Ni me voy a molestar. Lo voy a bloquear."
    nvl_narrator "Bloqueaste a este contacto."
    show carlos sigh at characters_half_size_placed_at_center
    Carlos "¿Cómo puede ser que escriba tan mal?"
    # scene bg habitacion carlos at carlos_bedroom_background_size with fade
    show carlos annoyed at characters_half_size_placed_at_center_no_transition
    with Shake((0, 0, 0, 0), .5, dist=30)
    Carlos "¡No se puede ser tan idiota!"
    scene pac_desk_desk_objects at carlos_bedroom_background_size
    with fade
    Carlos "Por fin. A trabajar..."
    jump topdown_view_desk_scene
    return
