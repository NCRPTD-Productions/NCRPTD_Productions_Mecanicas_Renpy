init:
    transform guillermo_house_outside:
        zoom 1.5
        align((0.5, 0.5))
    transform guillermo_bedroom:
        zoom .68
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
    play sound "sfx_pasos.mp3"
    play music "bgm_cueva_de_guillermo.mp3"
    scene bg habitacion guillermo desordenada vacia at guillermo_bedroom
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
    scene bg habitacion guillermo desordenada vacia at guillermo_bedroom
    play sound "sfx_pasos.mp3"
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
    play sound "sfx_pasos.mp3"
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
    call artifact_pac(1)
    # jump end_game
    return

label act_II_images_rendered_in_artifact:
    Guillermo "¡Allí está! ¡¿Ves!? ¡Te dije que habíamos encontrado algo: ese QR es algo de otro mundo!"
    Carlos "No. Eso no es un QR. Es un {i}MaxiCode{/i}, un tipo de código de barras."
    Carlos "Imagino que el Artefacto lo conseguiste de {i}4chan{/i}, ¿verdad?"
    Guillermo "¿Qué me habrá delatado?"
    Guillermo "Sí. Un usuario anónimo lo publicó en un foro de conspiracionismo."
    Guillermo "Dijo que se podía obtener señales alienígenas con él. ¡¿No es genial?!"
    Carlos "Podrás haberme impresionado con el Artefacto, pero no por ello creeré en los alienígenas, Guillermo."
    Guillermo "¡Oh, vamos!"
    Carlos "Y aún así no preguntaste por ahí qué clase de código es este. Ni siquiera investigaste."
    Guillermo "Blah, blah, blah."
    jump show_phone_ui_scanner
    return

label show_phone_ui_scanner:
    jump end_game
    return
    