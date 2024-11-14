init:
    transform ui_right_side_buttons:
        align(1.0, .3)
        zoom(.5)
        
init python:
    def ui_button_pressed():
        global is_button_pressed
        is_button_pressed = True
        renpy.pause(0.5)

screen ui_buttons:
    
    imagebutton:
        idle "ui_button_tel.png"
        hover "ui_button_tel_clicked.png"
        action Jump("ui_right_side_button_phone")
        at ui_right_side_buttons
        # hovered Show("displayTextScreen", displayText = "¿Regar?")
        # unhovered Hide("displayTextScreen")

label ui_right_side_button_phone:
    "Buenas tardes"


label show_ui_button:
    $ ui.frame = Frame("ui_button_tel.png", 0, 0, 800, 600)

    $ is_button_pressed = False
    $ ui.button("Click me", clicked= ui_button_pressed)

    # while not is_button_pressed:
    #     hacer algo

