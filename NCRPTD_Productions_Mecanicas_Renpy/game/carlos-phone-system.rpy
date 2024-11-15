init python:

    isCameraEnabled = False

init:
    transform phone:
        zoom 0.7
        xalign 0.5
        ypos 2500
        # Move the character across the screen (to the right)
        linear .5 yalign 0.42



label carlos_phone_system:
    show phone_foreground at phone