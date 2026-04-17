label tenth_apartment_scene:
    scene bg alley one
    call screen alleyNav

    menu:
        "Go down first alley":
            jump eleventh_apartment_scene
        "Go down second alley":
            jump thirteenth_apartment_scene
        "Go down third alley":
            jump fourteenth_apartment_scene
        "Go back":
            jump ninth_apartment_scene

label thirteenth_apartment_scene:
    scene bg alleyydead
    call screen deadEnd

    "You've met a dead end"
    menu:
        "Go back":
            jump tenth_apartment_scene


screen alleyNav():
    # 1st alley

    frame:
        xpos 840
        ypos 30
        xsize 1010 - 840
        ysize 120 - 30
        background "#e0005d88"

    button:
        xpos 840
        ypos 30
        xsize 1010 - 840
        ysize 120 - 30
        background None
        hover_background None

        mouse "move"

        action Jump("eleventh_apartment_scene")

    # 2nd alley

    frame:
        xpos 1440
        ypos 270
        xsize 1500 - 1440
        ysize 470 - 270
        background "#e0005d88"

    button:
        xpos 1440
        ypos 270
        xsize 1500 - 1440
        ysize 470 - 270
        background None
        hover_background None

        mouse "move"

        action Jump("thirteenth_apartment_scene")

    # 3rd alley

    frame:
        xpos 400
        ypos 150
        xsize 490 - 400
        ysize 310 - 150
        background "#e0005d88"

    button:
        xpos 400
        ypos 150
        xsize 490 - 400
        ysize 310 - 150
        background None
        hover_background None

        mouse "move"

        action Jump("fourteenth_apartment_scene")

    # back to ninth apartment scene

    frame:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background "#6527F5"

    button:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background None
        hover_background None

        mouse "move"

        action Jump("ninth_apartment_scene")

screen deadEnd():
    # back to tenth apartment scene

    frame:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background "#6527F5"

    button:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background None
        hover_background None

        mouse "move"

        action Jump("tenth_apartment_scene")