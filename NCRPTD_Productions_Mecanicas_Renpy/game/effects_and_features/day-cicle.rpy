init:
    transform day_cicle_bedroom_sizes:
        zoom 1.5
        align((0.0, 0.0))
    
    transform zoomed_window_bedroom:
        zoom 1.5
        align((0.5, 0.5))

init python: 
    day_cicle_transforms=[
            zoomed_window_bedroom
        ]

    elements_behind=[
        'bedroom_background',
    ]

    def show_day_cycle():
        renpy.scene()
        renpy.show("bg hab carlos w transparency_zoomed", at_list=day_cicle_transforms, layer='master', what=None, zorder=1, tag="bedroom_background", behind=[])
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg night", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.scene()

