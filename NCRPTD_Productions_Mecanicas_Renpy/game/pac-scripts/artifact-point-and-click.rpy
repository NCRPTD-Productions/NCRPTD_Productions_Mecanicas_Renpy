init:
    transform artifact_point_and_click_artifact_displacement:
        zoom 1.4
        align (0.5, 0.5)

    transform artifact_point_and_click_turn_on_off_button:
        zoom 1.2
        align (.26, .31)
        
    transform artifact_point_and_click_big_button:
        zoom 1.5
        align (.67, .91)

    transform artifact_point_and_click_small_button:
        zoom 1.5
        align (.787, .91)
    
    transform artifact_point_and_click_thin_antenna:
        zoom 1.2
        align (.3, 0.02)
    
    transform artifact_point_and_click_weird_antenna:
        zoom 1.2
        align (.55, 0.02)
    

init python:
    artifact_is_on= False
    artifact_thin_antenna_position = -1
    artifact_weird_antenna_position= 1
    artifact_on = False
    artifact_big_button_pressed = False
    artifact_small_button_pressed = True

#Point and click image buttons
screen artifact_point_and_click:
    if artifact_is_on:
        add "artifact_on.png" at artifact_point_and_click_artifact_displacement
        # "on"
    else:
        add "artifact_off.png" at artifact_point_and_click_artifact_displacement
        # "off"
    if artifact_is_on:
        imagebutton:
            auto "point_and_click/artifact/buttons/button_onoff_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_onoff_button_deactivate_action")
            at artifact_point_and_click_turn_on_off_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            auto "point_and_click/artifact/buttons/button_onoff_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_onoff_button_activate_action")
            at artifact_point_and_click_turn_on_off_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    if artifact_big_button_pressed:
        imagebutton:
            auto "point_and_click/artifact/buttons/big_button_1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_big_button_01_action")
            at artifact_point_and_click_big_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            auto "point_and_click/artifact/buttons/big_button_0_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_big_button_00_action")
            at artifact_point_and_click_big_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    if artifact_small_button_pressed:
        imagebutton:
            auto "point_and_click/artifact/buttons/small_button_1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_small_button_01_action")
            at artifact_point_and_click_small_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    else:
        imagebutton:
            auto "point_and_click/artifact/buttons/small_button_0_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_small_button_00_action")
            at artifact_point_and_click_small_button
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
            
    if artifact_thin_antenna_position == -1:
        imagebutton:
            auto "point_and_click/artifact/antenna/thin_antenna_-1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_thin_antenna_minus_one_action")
            at artifact_point_and_click_thin_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    elif artifact_thin_antenna_position == 0:
        imagebutton:
            auto "point_and_click/artifact/antenna/thin_antenna_0_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_thin_antenna_zero_action")
            at artifact_point_and_click_thin_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    elif artifact_thin_antenna_position == 1:
        imagebutton:
            auto "point_and_click/artifact/antenna/thin_antenna_1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_thin_antenna_one_action")
            at artifact_point_and_click_thin_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")

    if artifact_weird_antenna_position == -1:
        imagebutton:
            auto "point_and_click/artifact/antenna/weird_antenna_-1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_weird_antenna_minus_one_action")
            at artifact_point_and_click_weird_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    elif artifact_weird_antenna_position == 0:
        imagebutton:
            auto "point_and_click/artifact/antenna/weird_antenna_0_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_weird_antenna_zero_action")
            at artifact_point_and_click_weird_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")
    elif artifact_weird_antenna_position == 1:
        imagebutton:
            auto "point_and_click/artifact/antenna/weird_antenna_1_%s.png"
            # idle "point_and_click/top_down_desk/pac_desk_plant.png"
            # hover "pac_edgar_hover.png"
            action Jump("artifact_point_and_click_weird_antenna_one_action")
            at artifact_point_and_click_weird_antenna
            # hovered Show("displayTextScreen", displayText = "El horror.")
            # unhovered Hide("displayTextScreen")


# Point and click action end scenes


# Onoff Button
label artifact_point_and_click_onoff_button_activate_action:
    # "botón encendido on"
    $ artifact_is_on = True
    call screen artifact_point_and_click
    return

label artifact_point_and_click_onoff_button_deactivate_action:
    # "botón encendido off"
    $ artifact_is_on = False
    call screen artifact_point_and_click
    return




# Big Button
label artifact_point_and_click_big_button_00_action:
    # "Boton grande apretado"
    $ artifact_big_button_pressed=True
    call screen artifact_point_and_click
    return

label artifact_point_and_click_big_button_01_action:
    # "Boton grande vuelto a 0"
    $ artifact_big_button_pressed=False
    call screen artifact_point_and_click
    return



# Small Button

label artifact_point_and_click_small_button_00_action:
    $ artifact_small_button_pressed=True
    call screen artifact_point_and_click
    return

label artifact_point_and_click_small_button_01_action:
    $ artifact_small_button_pressed=False
    call screen artifact_point_and_click
    return



# Thin Antenna

label artifact_point_and_click_thin_antenna_minus_one_action:
    $ artifact_thin_antenna_position=0
    call screen artifact_point_and_click
    return

label artifact_point_and_click_thin_antenna_zero_action:
    $ artifact_thin_antenna_position=1
    call screen artifact_point_and_click
    return

label artifact_point_and_click_thin_antenna_one_action:
    $ artifact_thin_antenna_position=-1
    call screen artifact_point_and_click
    return



# Weird Antenna

label artifact_point_and_click_weird_antenna_minus_one_action:
    $ artifact_weird_antenna_position=0
    call screen artifact_point_and_click
    return

label artifact_point_and_click_weird_antenna_zero_action:
    $ artifact_weird_antenna_position=1
    call screen artifact_point_and_click
    return

label artifact_point_and_click_weird_antenna_one_action:
    $ artifact_weird_antenna_position=-1
    call screen artifact_point_and_click
    return


#