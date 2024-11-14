screen Artifact(isOn):
    if (isOn):
        add "artifact/artifact_on.png"
    else:
        add "artifact/artifact_off.png"

screen ThinAntenna(thinAntValue):
    imagebutton:
        pos(510, 0)
        if(thinAntValue == -1):
            idle "artifact/interactibles/antenae/thin_antenna_-1_idle.png"
            hover "artifact/interactibles/antenae/thin_antenna_-1_hover.png"
            action Call("setThinAntennaValue", 0)

        elif (thinAntValue == 0):
            idle "artifact/interactibles/antenae/thin_antenna_0_idle.png"
            hover "artifact/interactibles/antenae/thin_antenna_0_hover.png"
            action Call("setThinAntennaValue", 1)

        elif (thinAntValue == 1):
            idle "artifact/interactibles/antenae/thin_antenna_1_idle.png"
            hover "artifact/interactibles/antenae/thin_antenna_1_hover.png"
            action Call("setThinAntennaValue", -1)

screen WeirdAntenna(weirdAntValue):
    imagebutton:
        pos(850, 0)
        if(weirdAntValue == -1):
            idle "artifact/interactibles/antenae/weird_antenna_-1_idle.png"
            hover "artifact/interactibles/antenae/weird_antenna_-1_hover.png"
            action Call("setWeirdAntennaValue", 0)

        elif (weirdAntValue == 0):
            idle "artifact/interactibles/antenae/weird_antenna_0_idle.png"
            hover "artifact/interactibles/antenae/weird_antenna_0_hover.png"
            action Call("setWeirdAntennaValue", 1)

        elif (weirdAntValue == 1):
            idle "artifact/interactibles/antenae/weird_antenna_1_idle.png"
            hover "artifact/interactibles/antenae/weird_antenna_1_hover.png"
            action Call("setWeirdAntennaValue", -1)

screen BigButton(bButton):
    imagebutton:
        pos(1182, 835)
        if(bButton == 0):
            idle "artifact/interactibles/buttons/big_button_0_idle.png"
            hover "artifact/interactibles/buttons/big_button_0_hover.png"
            action Call("setBButtonValue", 1)

        elif (bButton == 1):
            idle "artifact/interactibles/buttons/big_button_1_idle.png"
            hover "artifact/interactibles/buttons/big_button_1_hover.png"
            action Call("setBButtonValue", 0)

screen SmallButton(sButton):
    imagebutton:
        pos(1402, 857)
        if(sButton == 0):
            idle "artifact/interactibles/buttons/small_button_0_idle.png"
            hover "artifact/interactibles/buttons/small_button_0_hover.png"
            action Call("setSButtonValue", 1)

        elif (sButton == 1):
            idle "artifact/interactibles/buttons/small_button_1_idle.png"
            hover "artifact/interactibles/buttons/small_button_1_hover.png"
            action Call("setSButtonValue", 0)

screen OnOff:
    imagebutton:
        pos(510, 340)
        idle "artifact/interactibles/buttons/button_onoff_idle.png"
        hover "artifact/interactibles/buttons/button_onoff_hover.png"
        action Call("ArtifactOnOff")