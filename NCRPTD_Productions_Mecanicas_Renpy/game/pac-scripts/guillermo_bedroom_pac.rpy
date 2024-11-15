init:
    transform guillermo_bed:
        zoom 1.2
        align(1.04, 1.45)

    transform guillermo_karate_kid_poster:
        zoom 0.7
        align(0.8, 0.3)

    transform guillermo_dirty_clothing:
        zoom 1.1
        align(0.985, 1.65)

    transform guillermo_justo_in_computer:
        zoom 1.2
        align(0.33, 0.88)

    transform guillermo_trapdoor:
        zoom 1.43
        align(-0.52, 0.91)


#Point and click image buttons
screen guillermo_bedroom_pac:
    #Image button cama guille

    #Image button justo en computadora
        imagebutton:
            auto "point_and_click/guillermo_bedroom/desorganized/justo_hab_guillermo_%s.png"
            # hover "pac_escritorio_hover.png"
            action Jump("justo_in_computer_action_pac")
            at guillermo_justo_in_computer
            # hovered Show("displayTextScreen", displayText = "Es de Guillermo.")
            # unhovered Hide("displayTextScreen")
            
        # add "point_and_click/guillermo_bedroom/desorganized/habitacion-guillermo-desordenada-vacia.jpg" at guillermo_bedroom
        imagebutton:
            auto "point_and_click/guillermo_bedroom/desorganized/cama_hab_guillermo_%s.png"
            action [Hide("displayTextScreen"), Jump("guillermo_bed_action_pac")]
            at guillermo_bed
            hovered Show("displayTextScreen", displayText = "El horror.")
            unhovered Hide("displayTextScreen")

    #Image button poster karate kid
        imagebutton:
            auto "point_and_click/guillermo_bedroom/desorganized/poster_hab_guillermo_%s.png"
            # hover "pac_biblioteca_izquierda_hover.png"
            action [Hide("displayTextScreen"), Jump("guillermo_poster_karate_kid_action_pac")]
            at guillermo_karate_kid_poster
            hovered Show("displayTextScreen", displayText = "Karate.")
            unhovered Hide("displayTextScreen")
              
    #Image button ropa tirada
        imagebutton:
            auto "point_and_click/guillermo_bedroom/desorganized/ropa_hab_guillermo_%s.png"
            # hover "pac_escritorio_hover.png"
            action [Hide("displayTextScreen"), Jump("guillermo_dirty_clothes_action_pac")]
            at guillermo_dirty_clothing
            hovered Show("displayTextScreen", displayText = "Es de Guillermo.")
            unhovered Hide("displayTextScreen")

    #Image button puerta ventana
        imagebutton:
            auto "point_and_click/guillermo_bedroom/desorganized/ventana_hab_guillermo_%s.png"
            # hover "pac_escritorio_hover.png"
            action Jump("guillermo_trapdoor_action_pac")
            at guillermo_trapdoor
#


#Point and click action end scenes

label guillermo_bed_action_pac:
    show carlos annoyed at characters_half_size_placed_at_left
    Carlos "Ni en sueños toco eso."
    hide carlos annoyed
    jump chapter_II_guillermo_bedroom_pac_handler
    return

label guillermo_poster_karate_kid_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_left
    Carlos "¿Sabrá que en Karate Kid no hacen karate?"
    show carlos normal at characters_half_size_placed_at_left_no_transition
    Justo "Lo dudo. Pelo no... No le aduinemos la ilusión."
    hide carlos normal
    jump chapter_II_guillermo_bedroom_pac_handler
    return

label guillermo_dirty_clothes_action_pac:
    show carlos annoyedspeech at characters_half_size_placed_at_left
    Carlos "¿Por qué?"
    show carlos normal at characters_half_size_placed_at_left_no_transition
    Justo "No lo sé, y te digo que no lo sé, porque sé que no sé que lo... Ehm..."
    show carlos surprised at characters_half_size_placed_at_left_no_transition
    Justo "¡Que no lo quiedes sabel!"
    show carlos 2ndpose at characters_half_size_placed_at_left_no_transition
    pause(0.5)
    hide carlos 2ndpose
    jump chapter_II_guillermo_bedroom_pac_handler
    return

label justo_in_computer_action_pac:
    show carlos normal at characters_half_size_placed_at_left
    Carlos "¿Qué haces?"
    # TODO: Poner sonido tecleo intenso
    Justo "Estoy... Jugando Castle Crashers. ¿Quieres jugar?"
    Carlos "No, gracias."
    hide carlos normal
    jump chapter_II_guillermo_bedroom_pac_handler
    return

label guillermo_trapdoor_action_pac:
    # TODO: Poner sonido pasos
    "Paso a parte del artefacto"
    jump chapter_II_artifact_introducion
    return
#