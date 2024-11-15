init python:
    scrapbook_gui_notes_part_2 = True
    scrapbook_gui_notes_part_3 = True

init:
    transform scrapbook_gui_book:
        zoom 0.7
        xalign 0.5
        ypos 2500
        # Move the character across the screen (to the right)
        linear .5 yalign 0.42

#armo el cuaderno con los sprites
screen carlos_gui_scrapbook:
    imagebutton:
        idle "point_and_click/crypto_notes/cryptos_book.png" at scrapbook_gui_book
    if scrapbook_gui_notes_part_2:
        imagebutton:
            idle "point_and_click/crypto_notes/cryptos_book.png" at scrapbook_gui_book
    if scrapbook_gui_notes_part_3:
        imagebutton:
            idle "point_and_click/crypto_notes/cryptos_book.png" at scrapbook_gui_book