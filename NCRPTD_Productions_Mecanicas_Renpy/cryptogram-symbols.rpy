
init python: 
    
    cryptogram_symbols=[
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "y",
    ]

    positions = [
    (100, 100),  # (x, y)
    (300, 100),
    (500, 100),
    (700, 100),
    (100, 300),
    (300, 300),
    (500, 300),
    (700, 300),
    (100, 500),
    (300, 500)
]
    def cryptogram_render():
        x = 0
        y = 100

        for s in cryptogram_symbols:
            # Define a custom transform to position the symbol
            transform = Transform(xpos=x, ypos=y)

            # Show the symbol with the custom transform
            renpy.show(s, at=transform)  # Show the sprite at (x, y)

            # Increment y and x for the next symbol's position
            y += 150  # Adjust the y position
            x += 150  # Optionally, adjust x for horizontal arrangement

            renpy.pause(0.5)  # Pause for half a second before showing the next sprite
