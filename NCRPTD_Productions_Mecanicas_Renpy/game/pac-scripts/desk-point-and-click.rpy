init:
    transform pac_desk_plant:
        zoom 0.8
        align(.065, 0.05)

    transform pac_desk_lamp:
        zoom .8
        align (1.055, 0.05)

    transform pac_desk_laptop:
        zoom 1.2
        align (0.53,0.15)

    transform pac_desk_pencil_holder:
        zoom .5
        align(0.835, 0.02)

#Point and click image buttons
screen carlos_desktop_pac:
    #Image button planta
        add "point_and_click/top_down_desk/pac_desk_desk_empty.jpg" at carlos_bedroom_background_size
        imagebutton:
            auto "point_and_click/top_down_desk/pac_desk_plant_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_plant_action_pac")]
            at pac_desk_plant
            hovered Show("displayTextScreen", displayText = "¿Regar?")
            unhovered Hide("displayTextScreen")

    #Image button lámpara
        imagebutton:
            auto "point_and_click/top_down_desk/pac_desk_lamp_%s.png"
            # hover "pac_biblioteca_izquierda_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_lamp_action_pac")]
            at pac_desk_lamp
            hovered Show("displayTextScreen", displayText = "¿Encender?")
            unhovered Hide("displayTextScreen")
              
    #Image button laptop
        imagebutton:
            auto "point_and_click/top_down_desk/pac_desk_laptop_%s.png"
            # hover "pac_escritorio_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_laptop_action_pac")]
            at pac_desk_laptop
            hovered Show("displayTextScreen", displayText = "¿Usar?")
            unhovered Hide("displayTextScreen")

    #Image button pencil holder
        imagebutton:
            idle "point_and_click/top_down_desk/pac_desk_pencil_holder_idle.png"
            at pac_desk_pencil_holder
            # hover "pac_escritorio_hover.png"
            # action [Hide("displayTextScreen"), Jump("desk_laptop_action_pac")]
            # hovered Show("displayTextScreen", displayText = "¿Usar?")
            # unhovered Hide("displayTextScreen")
#


#Point and click action end scenes

label desk_plant_action_pac:
    show carlos normal at characters_half_size_placed_at_left
    Carlos "No. Se riega cada diez días, y aún faltan dos."
    jump topdown_view_desk_scene
    return

label desk_lamp_action_pac:
    show carlos puzzled at characters_half_size_placed_at_left
    Carlos "Aún no es de noche."
    jump topdown_view_desk_scene
    return

label desk_laptop_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_left
    Carlos "Ah, sí, la laptop. Un aparato con miles de páginas y programas para desencriptar textos..."
    hide carlos thoughtful
    show edgar normal at edgar_placed_at_right
    Edgar "Glup."
    hide edgar normal
    play sound "sfx_slam_desk.mp3"
    show carlos smirk at characters_half_size_placed_at_left_no_transition
    with Shake((0, 0, 0, 0), .5, dist=30)
    Carlos "¡Y aún así nadie pudo descifrar la identidad del Asesino del Zodíaco!"
    show edgar hiding at edgar_placed_at_right
    Edgar "..."
    show carlos annoyedspeech at characters_half_size_placed_at_left_no_transition
    Carlos "¡Porque son ineptos, y sus mentes dependen de una máquina!"
    hide edgar hiding
    Carlos "¡Por eso, Edgar, yo lo hago a la vieja usanza: Con lápiz y papel!"
    hide carlos smirk
    jump tutorial_start
    return

#