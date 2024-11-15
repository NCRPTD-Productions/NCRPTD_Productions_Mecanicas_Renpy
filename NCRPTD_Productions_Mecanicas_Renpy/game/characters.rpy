#Characters

define Carlos = Character('Carlos', color= "#e2b520")
define Edgar = Character('Edgar', color= "#14d1d1")
define Justo= Character('Justo', color= "#bd4acc")
define Guillermo= Character('Guillermo', color= "#db4141")
define AlZodiak= Character('Al Zodiak', color= "#70d1ac")

#Phone characters and variables
define carlos_phone_nvl = Character("Carlos", kind=nvl, image="nighten", callback=Phone_SendSound)
define justo_phone_nvl = Character("Justo", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)
