
#Snow shader variables
image splashbg= Color("#FBF0D9")
image snow1 = Fixed(SnowBlossom("gui/dreaming particle 1.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image snow2 = Fixed(SnowBlossom("gui/dreaming particle 2.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image snow3 = Fixed(SnowBlossom("gui/dreaming particle 3.png", 10, xspeed=(20, 50), yspeed=(100,200), start=10, fast=True, horizontal=False))
image rain = Fixed(SnowBlossom("gui/raindrop.png", 50, xspeed=(-600, -1000), yspeed=(1000,1600), start=10))
image rainback:
    "gui/rain1.png"
    pause 0.1
    "gui/rain2.png"
    pause 0.1
    repeat
#

# Videos

image carloswakingupvideo = Movie(play="images/videos/carloswakingup.webm", size=(1920,1080))
image opening_sequence_video = Movie(play="images/videos/opening_sequence.webm", size=(1920,1080))

init python: 

    isintutorial = False
        
screen displayTextScreen:  
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
    #    
#

label start:
    jump opening_sequence_and_intro
    