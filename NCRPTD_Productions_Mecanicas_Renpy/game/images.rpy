
init:

#Custom image sizes
    transform video_formatter:
        zoom 1.5
        align((0.0, 0.0))
    transform pac_custom_library_zoom:
        zoom 1.37

    transform opening_image_size: #Opening text size adjustment
        xalign 0.5
        yalign 0.5

    transform characters_half_size_placed_at_left: 
        zoom 0.5
        pos (-10, 350) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3  # Shake right and down again # Move to the right over 2 seconds
        # easeinout 2.0 xalign 0.5  # Optionally ease the character to the center after

    transform characters_half_size_placed_at_center: 
        zoom 0.5
        # xalign .5
        ypos 350
        
        linear .25 xalign .6  # Shake right and down again  # Move to the right over 2 seconds
        # pos (600, 350)

    transform characters_half_size_placed_at_right: 
        zoom 0.5
        xpos 900
        ypos 350
        # pos (900, 350)
        linear .25 xalign .8  # Shake right and down again

    transform characters_half_size_placed_at_right_no_transition: 
        zoom 0.5
        xalign .8
        ypos 350
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again

    transform characters_half_size_placed_at_left_no_transition: 
        zoom 0.5
        xalign .3
        ypos 350
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        # pos (-5, 350) # pos (300, 500)

    transform characters_half_size_placed_at_center_no_transition: 
        zoom 0.5
        ypos 350
        xalign .6
        linear 0.090 xoffset -5 yoffset -5  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        
    transform edgar_placed_at_right:
        zoom 0.35
        pos (2350, 370) # pos (1650, 370)
        linear .25 xalign .75

    transform edgar_placed_at_left:
        zoom 0.35
        pos (400, 300)

    transform characters_zoomed_placed_at_right: 
        zoom 0.7
        
        pos (300, 400)

    transform custom_background_size: 
        zoom 2.7
        pos (0,0)
    transform carlos_bedroom_background_size: 
        zoom .75
        pos (0,0)
        
    transform carlos_bedroom_left_library: 
        zoom .75
        pos (0,0)
        
    transform carlos_bedroom_right_library: 
        zoom .75
        pos (0,-150)
        
    transform carlos_corner_bedroom_background_size: 
        zoom 1.5
        pos (0,0)

    transform menu_position:
        pos(0,0)
        
    transform phone_placed_at_left_shake:
        zoom 1
        pos (-10, 125)  # Initial position of the sprite
        xalign .3
        # Vibrate every 3 seconds (alternating x and y offsets)
        linear 0.090 xoffset -10 yoffset -10  # Shake left and up
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down
        linear 0.090 xoffset -10 yoffset -10  # Shake left and up again
        linear 0.090 xoffset +5 yoffset +5  # Shake right and down again
        pause .5  # Pause for 3 seconds before starting the next shake cycle
        repeat

    transform phone_placed_at_left_jump:
        zoom 1
        ypos 125 # pos (300, 500)
        xalign .3
        # Move the character across the screen (to the right)
        linear 0.090 xoffset -25 yoffset -25  # Shake left and up again
        linear 0.090 xoffset +25 yoffset +25  # Shake right and down again

    transform phone_placed_at_left_no_shake:
        zoom 1
        pos (-10, 125) # pos (300, 500)
        # Move the character across the screen (to the right)
        linear .25 xalign .3
    
    transform dreaming_background:
        zoom 1.5
        pos(0, 0)
    
    transform cryptogram_symbol: 
        xpos 0
        ypos 100

    transform door_centered:
        zoom 3.2
        align(0.5, 0.8)

#
