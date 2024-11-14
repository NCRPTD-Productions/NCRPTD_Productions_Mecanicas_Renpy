label artifact_pac:
    define thinAntValue = 0
    define weirdAntValue = 1
    define bButton = 0
    define sButton = 0
    define isOn = False
    
    show screen Artifact(isOn) with dissolve
    
    label showArtifact:
        show screen Artifact(isOn)
        show screen ThinAntenna(thinAntValue)
        show screen WeirdAntenna(weirdAntValue)
        show screen BigButton(bButton)
        show screen SmallButton(sButton)
        show screen OnOff

        window hide
        $ ui.interact()

label setThinAntennaValue(value):
    $ thinAntValue = value
    
    jump showArtifact

label setWeirdAntennaValue(value):
    $ weirdAntValue = value
    
    jump showArtifact

label setBButtonValue(value):
    $ bButton = value
    
    jump showArtifact

label setSButtonValue(value):
    $ sButton = value
    
    jump showArtifact

label ArtifactOnOff:
    $ isOn = not isOn

    jump showArtifact