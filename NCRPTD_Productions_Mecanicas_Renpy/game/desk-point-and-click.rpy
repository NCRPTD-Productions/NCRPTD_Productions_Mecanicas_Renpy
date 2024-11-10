
#Point and click image buttons
screen carlos_desktop_pac:
    #Image button planta
        imagebutton:
            pos(75, 845)
            idle "pac_edgar_idle.png"
            hover "pac_edgar_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_plant_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "¿Regar?")
            unhovered Hide("displayTextScreen")
    #Image button lámpara
        imagebutton:
            pos(645, 545)
            idle "pac_biblioteca_izquierda_idle.png"
            hover "pac_biblioteca_izquierda_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_lamp_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "¿Encender?")
            unhovered Hide("displayTextScreen")
              
    #Image button laptop
        imagebutton:
            pos(1020, 860)
            idle "pac_escritorio_idle.png"
            hover "pac_escritorio_hover.png"
            action [Hide("displayTextScreen"), Jump("desk_laptop_action_pac")]
            at pac_custom_library_zoom
            hovered Show("displayTextScreen", displayText = "¿Usar?")
            unhovered Hide("displayTextScreen")
#


#Point and click action end scenes

label desk_plant_action_pac:
    show carlos normal at characters_half_size_placed_at_left
    Carlos "No. Se riega cada diez días, y faltan dos."
    call start_point_and_click from _call_start_point_and_click_2

label desk_lamp_action_pac:
    show carlos puzzled at characters_half_size_placed_at_left
    Carlos "Aún no es de noche."

label desk_laptop_action_pac:
    show carlos thoughtful at characters_half_size_placed_at_left
    Carlos "Ah, sí, la laptop. Un aparato con miles de páginas y programas para desencriptar textos..."
    hide carlos thoughtful
    show edgar neutral at edgar_placed_at_right
    Edgar "Glup."
    #TODO: Sfx golpe mesa
    hide edgar neutral
    show carlos smirk at characters_half_size_placed_at_left
    Carlos "¡Y aún así nadie pudo descifrar la identidad del Asesino del Zodiaco!"
    show edgar hiding at edgar_placed_at_right
    Edgar "..."
    Carlos "¡Porque son ineptos, y sus mentes dependen de una máquina!"
    hide edgar hiding
    Carlos "¡Por eso, Edgar, yo lo hago a la vieja usanza: con lápiz y papel!"
    hide carlos smirk
    jump tutorial_start

#