init:
    transform day_cicle_bedroom_sizes:
        zoom 1.5
        align((0.0, 0.0))

init python: 
    day_cicle_transforms=[
            day_cicle_bedroom_sizes
        ]

    elements_behind=[
        'bedroom_background'
    ]

    def show_day_cycle():
        renpy.scene()
        renpy.show("bg hab carlos w transparency", at_list=day_cicle_transforms, layer='master', what=None, zorder=1, tag="bedroom_background", behind=[])
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg night", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.pause(3)
        renpy.show("bg day", at_list=day_cicle_transforms, layer='master', what=None, zorder=0, tag=None, behind=elements_behind)
        renpy.scene()
        # show bg night at custom_background_size
        # pause (.5)
        # show bg day zorder 1
        # pause (.5)
        # show bg hab carlos w transparency at custom_background_size onlayer screens

