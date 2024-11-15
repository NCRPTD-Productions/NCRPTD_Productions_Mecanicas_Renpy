init:
    transform guillermo_house_outside:
        zoom 1.5
        align((0.5, 0.5))

label start_chapter_II_guillermo_home:
    scene black
    show bg guillermo house exterior at guillermo_house_outside
    pause(1)
    show guillermo feliz at characters_half_size_placed_at_center
    play sound "sfx_door_slam.mp3"
    Guillermo "¡Carlos!"
    Carlos "{i}Ni siquiera toqué la puerta.{i}"
    Carlos "Hola, Guillermo. ¿Están tus padres?"
    show guillermo serious2 at characters_half_size_placed_at_center_no_transition
    Guillermo "No. Se fueron a comprar. "
    show guillermo hayasmug at characters_half_size_placed_at_center_no_transition
    Guillermo "Ahora, ¡Sube conmigo a la terraza! ¡No perdamos más tiempo!"
    Carlos "{i}¿Cómo diablos puede cambiar de humor tan rápido? Da escalofríos.{i}"
    jump chapter_II_guillermo_bedroom_scene_I

label chapter_II_guillermo_bedroom_scene_I:
    scene guillermo bedroom at guillermo_house_outside
    # TODO: Poner sonido pasos
    # TODO: Poner música cueva guille
    Guillermo "¡Ven a la terraza!"
    show carlos normal at characters_half_size_placed_at_left
    Carlos "Cuánto desorden... Dios."
    hide carlos normal
    Justo "Hola, Calos. ¿Todo bien?"
    show carlos annoyed at characters_half_size_placed_at_left_no_transition
    "{i}Investiga la sala o ve a la terraza.{i}"
    hide carlos annoyed
    jump chapter_II_guillermo_bedroom_pac_handler

label chapter_II_guillermo_bedroom_pac_handler:
    call screen guillermo_bedroom_pac
    return

label chapter_II_guillermo_bedroom_no_pac:
    # TODO: Agregar sonido pasos
    scene guillermo bedroom at guillermo_house_outside
    Guillermo "¡Ven a la terraza!"
    show carlos puzzled at characters_half_size_placed_at_left
    Carlos "¿En serio te pondrás a jugar? ¡Si acabamos de llegar!"
    Justo "Sí, bueno. Me quedó poco por terminal la part- partida. "
    show carlos normal at characters_half_size_placed_at_left_no_transition
    Carlos "Ah."
    Carlos "Esta habitación es un asco."
    Justo "Tú lo has dicho."
    play sound "smirk.mp3"
    show carlos smirk at characters_half_size_placed_at_left_no_transition
    Carlos "Estaré en la terraza."
    # TODO: Agregar sonido pasos
    jump chapter_II_artifact_introducion
    return

label chapter_II_artifact_introducion:
    # scene artifact_off with fade
    # if artifact_is_on:
    #     show artifact_on at artifact_point_and_click_artifact_displacement
    #     "on"
    # else:
    #     show artifact_off at artifact_point_and_click_artifact_displacement
    #     "off"
    call screen artifact_point_and_click
    # jump end_game
    return
    