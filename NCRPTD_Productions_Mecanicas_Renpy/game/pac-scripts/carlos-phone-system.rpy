init python:

    isCameraEnabled = False
    phone_navigation_gui_carlos_home_enabled = True
    phone_navigation_gui_guillermo_home_enabled = True
    phone_navigation_gui_gas_station_enabled = True
    phone_navigation_gui_risky_gas_station_enabled = True
    phone_navigation_gui_al_zodiak_enabled = True

init:
    transform phone:
        zoom 0.7
        xalign 0.5
        ypos 2500
        # Move the character across the screen (to the right)
        linear .5 yalign 0.42
    transform phone_map_background:
        zoom 1.15
        xalign 0.5
        ypos 2500
        # Move the character across the screen (to the right)
        linear .5 yalign 0.42
    transform phone_map_carlos_home:
        zoom .9
        xalign 0.45
        ypos 2500
        linear .5 yalign 0.6
    transform phone_map_guillermo_home:
        zoom 1.0
        xalign 0.55
        ypos 2500
        linear .5 yalign 0.6
    transform phone_map_gas_station:
        zoom .9
        xalign 0.5
        ypos 2500
        linear .5 yalign 0.45
    transform phone_map_risky_gas_station:
        zoom .5
        xalign 0.45
        ypos 2500
        linear .5 yalign 0.3
    transform phone_map_al_zodiak:
        zoom .6
        xalign 0.55
        ypos 2500
        linear .5 yalign 0.3

#armo el teléfono con los sprites e imagebuttons
screen carlos_phone_system:
    imagebutton:
        idle "phone_map_background.png" at phone_map_background
    imagebutton:
        idle "phone_foreground.png" at phone
    if phone_navigation_gui_carlos_home_enabled:
        imagebutton:
            auto "point_and_click/phone_system/phone_map_pac_carlos_home_%s.png"
            action Jump("carlos_home_phone_system_location")
            at phone_map_carlos_home
    if phone_navigation_gui_guillermo_home_enabled:
        imagebutton:
            auto "point_and_click/phone_system/phone_map_pac_guillermo_home_%s.png"
            action Jump("guillermo_home_phone_system_location")
            at phone_map_guillermo_home
    if phone_navigation_gui_gas_station_enabled:
        imagebutton:
            auto "point_and_click/phone_system/phone_map_pac_gas_station_%s.png"
            action Jump("gas_station_phone_system_location")
            at phone_map_gas_station
    if phone_navigation_gui_risky_gas_station_enabled:
        imagebutton:
            auto "point_and_click/phone_system/phone_map_pac_old_gas_station_%s.png"
            action Jump("risky_gas_station_phone_system_location")
            at phone_map_risky_gas_station
    if phone_navigation_gui_al_zodiak_enabled:
        imagebutton:
            auto "point_and_click/phone_system/phone_map_pac_ufo_%s.png"
            action Jump("al_zodiak_phone_system_location")
            at phone_map_al_zodiak

# screen carlos_phone_system_pac:

label carlos_home_phone_system_location:
    scene gas station
    # scene black
    "Casa Carlos"
    # call handle_carlos_phone_ui_button
    return

label guillermo_home_phone_system_location:
    scene nave
    "Casa Guillermo"
    # call handle_carlos_phone_ui_button
    # scene gas station
    return

label gas_station_phone_system_location:
    scene gas station
    "Estación de servicio ok"
    # call handle_carlos_phone_ui_button
    return

label risky_gas_station_phone_system_location:
    scene nave
    "Estación de servicio edgy"
    # call handle_carlos_phone_ui_button
    return

label al_zodiak_phone_system_location:
    scene nave
    "Al Zodiak"
    # call handle_carlos_phone_ui_button
    return