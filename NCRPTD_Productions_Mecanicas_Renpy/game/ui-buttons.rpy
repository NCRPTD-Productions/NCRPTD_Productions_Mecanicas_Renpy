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
        action ShowMenu("ui_scrapbook_right_side_button")
        at ui_right_side_button_scrapbook

label handle_carlos_phone_ui_button:
    
    # show carlos_phone_system
    show screen ui_phone_right_side_button
    jump carlos_phone_system 
    "Teléfono de carlos"

screen ui_phone_right_side_button:
    imagebutton:
        at ui_right_side_button_phone
        idle "ui/ui_button_tel_clicked.png"
        action Return()


screen ui_scrapbook_right_side_button:
    imagebutton:
        at ui_right_side_button_scrapbook
        idle "ui/ui_button_scrapbook_clicked.png"
        action Return()
        