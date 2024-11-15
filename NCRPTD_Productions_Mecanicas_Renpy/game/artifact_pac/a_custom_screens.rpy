    
init:
    transform zoomedin:
        zoom 1.35

init python:
    imageIndex = 0
    is_first_image_discovered = False
    is_second_image_discovered = False

screen Artifact(isOn, thinAntValue, weirdAntValue, bButton, sButton, indexval):
    if (isOn):

        if (thinAntValue == -1 and weirdAntValue == 0 and bButton == 1 and sButton == 0):
            add "point_and_click/artifact/artifact_on_1st.png" zoom 1.35
            # "Primera imagen"
            $ indexval =+ 1
                    
            # $ is_first_image_discovered = True
            # $ global imageIndex
            # $ imageIndex = imageIndex + 1
        
        elif (thinAntValue == 0 and weirdAntValue == -1 and bButton == 1 and sButton == 1):
            add "point_and_click/artifact/artifact_on_2nd.png" zoom 1.35
            $ indexval =+ 1
            # "segunda imagen"
            # $ global imageIndex
            # $ imageIndex = imageIndex + 1
            # $ is_second_image_discovered = True

        else:
            add "point_and_click/artifact/artifact_on.png" zoom 1.35
            
    else:
        add "point_and_click/artifact/artifact_off.png" zoom 1.35
    

screen ThinAntenna(thinAntValue):
    imagebutton:
        pos(610, 0)
        if(thinAntValue == -1):
            idle "point_and_click/artifact/interactibles/antenae/thin_antenna_-1_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/thin_antenna_-1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setThinAntennaValue", 0)

        elif (thinAntValue == 0):
            idle "point_and_click/artifact/interactibles/antenae/thin_antenna_0_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/thin_antenna_0_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setThinAntennaValue", 1)

        elif (thinAntValue == 1):
            idle "point_and_click/artifact/interactibles/antenae/thin_antenna_1_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/thin_antenna_1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setThinAntennaValue", -1)

screen WeirdAntenna(weirdAntValue):
    imagebutton:
        pos(1150, 0)
        if(weirdAntValue == -1):
            idle "point_and_click/artifact/interactibles/antenae/weird_antenna_-1_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/weird_antenna_-1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setWeirdAntennaValue", 0)

        elif (weirdAntValue == 0):
            idle "point_and_click/artifact/interactibles/antenae/weird_antenna_0_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/weird_antenna_0_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setWeirdAntennaValue", 1)

        elif (weirdAntValue == 1):
            idle "point_and_click/artifact/interactibles/antenae/weird_antenna_1_idle.png"
            hover "point_and_click/artifact/interactibles/antenae/weird_antenna_1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setWeirdAntennaValue", -1)

screen BigButton(bButton):
    imagebutton:
        pos(1595, 1130)
        if(bButton == 0):
            idle "point_and_click/artifact/interactibles/buttons/big_button_0_idle.png"
            hover "point_and_click/artifact/interactibles/buttons/big_button_0_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setBButtonValue", 1)

        elif (bButton == 1):
            idle "point_and_click/artifact/interactibles/buttons/big_button_1_idle.png"
            hover "point_and_click/artifact/interactibles/buttons/big_button_1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setBButtonValue", 0)

screen SmallButton(sButton):
    imagebutton:
        pos(1893, 1155)
        if(sButton == 0):
            idle "point_and_click/artifact/interactibles/buttons/small_button_0_idle.png"
            hover "point_and_click/artifact/interactibles/buttons/small_button_0_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setSButtonValue", 1)

        elif (sButton == 1):
            idle "point_and_click/artifact/interactibles/buttons/small_button_1_idle.png"
            hover "point_and_click/artifact/interactibles/buttons/small_button_1_hover.png"
            at zoomedin
            if (canClickThings):
                action Call("setSButtonValue", 0)

screen OnOff:
    imagebutton:
        pos(680, 450)
        idle "point_and_click/artifact/interactibles/buttons/button_onoff_idle.png"
        hover "point_and_click/artifact/interactibles/buttons/button_onoff_hover.png"
        at zoomedin
        
        if (canClickOnOff):
            if (onoff == 0):
                action Call("ArtifactOnOff_1")
            elif(onoff == 1):
                action Call("ArtifactOnOff_2")
            elif(onoff >= 2):
                action Call("ArtifactOnOff_3")
            

screen GoBackArrow:
    imagebutton:
        pos(100, 100)
        idle "ui/ui_arrow_left.png"
        action Call("GoBack")