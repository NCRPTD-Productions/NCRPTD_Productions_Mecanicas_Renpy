init python:
    scrapbook_gui_notes_part_1 = True
    scrapbook_gui_notes_part_2 = False
    scrapbook_gui_notes_part_3 = False

init:
    transform scrapbook_gui_book:
        zoom 0.7
        xalign 0.5
        ypos 2500
        # Move the character across the screen (to the right)
        linear .5 yalign 0.42

#armo el cuaderno con los sprites
screen carlos_gui_scrapbook:
    if scrapbook_gui_notes_part_1:
        imagebutton:
            idle "point_and_click/crypto_notes/cryptos_book.png" at scrapbook_gui_book
            action Return()
    if scrapbook_gui_notes_part_2:
        imagebutton:
            idle "point_and_click/crypto_notes/cryptos_book_2.png" at scrapbook_gui_book
            action Return()
    if scrapbook_gui_notes_part_3:
        imagebutton:
            idle "point_and_click/crypto_notes/cryptos_book_3.png" at scrapbook_gui_book
            action Return()