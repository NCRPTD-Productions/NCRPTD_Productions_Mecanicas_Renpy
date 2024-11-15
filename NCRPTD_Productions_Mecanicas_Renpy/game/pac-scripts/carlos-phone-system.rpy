init python:

    isCameraEnabled = False

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
        align((0.45, 0.6))
    transform phone_map_guillermo_home:
        zoom 1.0
        align((0.55, 0.6))
    transform phone_map_gas_station:
        zoom .9
        align((0.5, 0.45))
    transform phone_map_risky_gas_station:
        zoom .5
        align((0.45, 0.3))
    transform phone_map_al_zodiak:
        zoom .6
        align((0.55, 0.3))

label carlos_phone_system:
    show phone_map_background at phone_map_background
    show phone_foreground at phone
    show screen carlos_phone_system_pac

screen carlos_phone_system_pac:
    imagebutton:
        auto "point_and_click/phone_system/phone_map_pac_carlos_home_%s.png"
        # hover "ui/ui_button_tel_hover.png"
        action Jump("carlos_home_phone_system_location")
        at phone_map_carlos_home

    imagebutton:
        auto "point_and_click/phone_system/phone_map_pac_guillermo_home_%s.png"
        # hover "ui/ui_button_scrapbook_hover.png"
        action Jump("guillermo_home_phone_system_location")
        at phone_map_guillermo_home

    imagebutton:
        auto "point_and_click/phone_system/phone_map_pac_gas_station_%s.png"
        # hover "ui/ui_button_scrapbook_hover.png"
        action Jump("gas_station_phone_system_location")
        at phone_map_gas_station

    imagebutton:
        auto "point_and_click/phone_system/phone_map_pac_old_gas_station_%s.png"
        # hover "ui/ui_button_scrapbook_hover.png"
        action Jump("risky_gas_station_phone_system_location")
        at phone_map_risky_gas_station

    imagebutton:
        auto "point_and_click/phone_system/phone_map_pac_ufo_%s.png"
        # hover "ui/ui_button_scrapbook_hover.png"
        action Jump("al_zodiak_phone_system_location")
        at phone_map_al_zodiak
        
   

label carlos_home_phone_system_location:
    "Casa Carlos"
    call handle_carlos_phone_ui_button
    show gas station
    return

label guillermo_home_phone_system_location:
    "Casa Guillermo"
    call handle_carlos_phone_ui_button
    show gas station
    return

label gas_station_phone_system_location:
    "Estación de servicio ok"
    call handle_carlos_phone_ui_button
    show gas station
    return

label risky_gas_station_phone_system_location:
    "Estación de servicio edgy"
    call handle_carlos_phone_ui_button
    show gas station
    return

label al_zodiak_phone_system_location:
    "Al Zodiak"
    call handle_carlos_phone_ui_button
    show gas station
    return