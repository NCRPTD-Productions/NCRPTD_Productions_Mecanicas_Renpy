define thinAntValue = 0
define weirdAntValue = 1
define bButton = 0
define sButton = 0
define isOn = False
define onoff = 0
define imageIndex = 0

define canClickThings = False
define canClickOnOff = False

label artifact_pac(momentIndex):
    stop music
    
    show screen Artifact(isOn, thinAntValue, weirdAntValue, bButton, sButton)
    show screen ThinAntenna(thinAntValue)
    show screen WeirdAntenna(weirdAntValue)
    show screen BigButton(bButton)
    show screen SmallButton(sButton)
    show screen OnOff

    if(momentIndex == 1):
        Carlos "¿Qué es esto?"
        Guillermo "Enciéndelo. Ya verás que te vas a reír."
        $ canClickOnOff = True
    
    label showArtifact:
        show screen Artifact(isOn, thinAntValue, weirdAntValue, bButton, sButton)
        show screen ThinAntenna(thinAntValue)
        show screen WeirdAntenna(weirdAntValue)
        show screen BigButton(bButton)
        show screen SmallButton(sButton)
        show screen OnOff

        if (imageIndex >= 3 and momentIndex == 1):
            $ canClickThings = False
            $ canClickOnOff = False
            stop music
            Guillermo "¡Allí está! ¡¿Ves!? ¡Te dije que habíamos encontrado algo: ese QR es algo de otro mundo!"
            Carlos "No. Eso no es un QR. Es un {i}MaxiCode{/i}, un tipo de código de barras."
            Carlos "Imagino que el Artefacto lo conseguiste de {i}4chan{/i}, ¿verdad?"
            Guillermo "¿Qué me habrá delatado?"
            Guillermo "Sí. Un usuario anónimo lo publicó en un foro de conspiracionismo."
            Guillermo "Dijo que se podía obtener señales alienígenas con él. ¡¿No es genial?!"
            Carlos "Podrás haberme impresionado con el Artefacto, pero no por ello creeré en los alienígenas, Guillermo."
            Guillermo "¡Oh, vamos!"
            Carlos "Y aún así no preguntaste por ahí qué clase de código es este. Ni siquiera investigaste."
            Guillermo "Blah, blah, blah."
            # TODO APARECE LA UI PARA TELEFONO Y CUADERNO

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

label ArtifactOnOff_1:
    play sound "sfx_boton_presionado.mp3"
    $ isOn = not isOn
    $ onoff += 1
    $ canClickOnOff = False

    show screen Artifact(isOn, thinAntValue, weirdAntValue, bButton, sButton)
    show screen ThinAntenna(thinAntValue)
    show screen WeirdAntenna(weirdAntValue)
    show screen BigButton(bButton)
    show screen SmallButton(sButton)
    show screen OnOff


    Carlos "¡¿Qué?!"
    Guillermo "Ay, no. El viento debió haber descalibrado las antenas."
    play sound "sfx_rage_scream.mp3"
    Carlos "¿Lo dices en serio?"
    Guillermo "¡No, no! ¡Escúchame! Solo tienes que mover algunas cosas."
    Carlos "¿Y por qué dejar esta cosa al aire?"
    Guillermo "Primero, {i}esta cosa{/i} se llama \"El Artefacto\". O Willy, como sugirió Justo."
    Carlos "No voy a llamarlo Wi-{nw=0.5}"
    # TODO #camara shake
    Guillermo "Y segundo, tienes que reacomodar las antenas y tocar los botones como muestra en el papel ahí a la derecha. ¡Fácil!"
    Carlos "¿Y tercero?"
    Guillermo "Nada."
    Guillermo "¡Vamos, hazlo de una vez!"

    $ canClickThings = True
    $ canClickOnOff = True
    play music "bgm_thundersnail.mp3"
    
    jump showArtifact

label ArtifactOnOff_2:
    play sound "sfx_vibe_stops.mp3"
    $ onoff += 1
    $ canClickThings = False
    $ canClickOnOff = False

    $ isOn = not isOn
    show screen Artifact(isOn, thinAntValue, weirdAntValue, bButton, sButton)
    show screen ThinAntenna(thinAntValue)
    show screen WeirdAntenna(weirdAntValue)
    show screen BigButton(bButton)
    show screen SmallButton(sButton)
    show screen OnOff

    stop music
    Guillermo "..."
    Guillermo "¿Por qué hiciste eso?"
    Carlos "Se paró una mosca."
    Guillermo "El diablo."
    play music "bgm_thundersnail.mp3"
    $ canClickThings = True
    $ canClickOnOff = True

    jump showArtifact


label ArtifactOnOff_3:
    play sound "sfx_boton_presionado.mp3"
    $ isOn = not isOn

    jump showArtifact

label GoBack:
    "allo allooo"