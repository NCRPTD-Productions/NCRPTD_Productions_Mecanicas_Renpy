init:
    transform ui_right_side_button_phone:
        align(1.01, 0.1)
        offset(-15, 15)
        zoom 0.5

    transform ui_right_side_button_scrapbook:
        align(1.01, .3)
        offset(-15, 15)
        zoom 0.5
        
screen ui_buttons:
    imagebutton:
        idle "ui/ui_button_tel_idle.png"
        hover "ui/ui_button_tel_hover.png"
        action ShowMenu("handle_carlos_phone_ui_button")
        at ui_right_side_button_phone

    imagebutton:
        idle "ui/ui_button_scrapbook_idle.png"
        hover "ui/ui_button_scrapbook_hover.png"
        action ShowMenu("handle_carlos_scrapbook_ui_button")
        at ui_right_side_button_scrapbook

label carlos_bedroom_navigation_gui:
    scene bg habitacion carlos at carlos_bedroom_background_size
    show screen ui_buttons

label handle_carlos_phone_ui_button:
    # show carlos_phone_system
    scene black
    call screen carlos_phone_system 
    # show screen ui_phone_right_side_button
    "Teléfono de carlos."
    # return
    return

label handle_carlos_scrapbook_ui_button:
    scene black
    call screen carlos_gui_scrapbook
    # show screen ui_scrapbook_right_side_button
    "Crypto Notes."
    return

screen ui_phone_right_side_button:
    imagebutton:
        idle "ui/ui_button_tel_clicked.png"
        at ui_right_side_button_phone
        action Return()


screen ui_scrapbook_right_side_button:
    imagebutton:
        at ui_right_side_button_scrapbook
        idle "ui/ui_button_scrapbook_clicked.png"
        action Return()
        