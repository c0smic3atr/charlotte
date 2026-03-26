label fifth_apartment_scene:
    scene bg apartments3
    call screen fifthApartmentNav



screen fifthApartmentNav():
    # to the parking lot scene
    frame:
        xpos 150
        ypos 190
        xsize 380 - 150
        ysize 430 - 190
        background "#e0005d88"

    button:
        xpos 150
        ypos 190
        xsize 380 - 150
        ysize 430 - 190
        background None
        hover_background None

        mouse "move"

        action Jump("sixth_apartment_scene")


    # to the second set of apartments
    frame:
        xpos 1195
        ypos 25
        xsize 1410 - 1195
        ysize 190 - 25
        background "#e0005d88"

    button:
        xpos 1195
        ypos 25
        xsize 1410 - 1195
        ysize 190 - 25
        background None
        hover_background None

        mouse "move"

        action Jump("seventh_apartment_scene")

    # to continue down the road

    frame:
        xpos 1770
        ypos 230
        xsize 1910 - 1770
        ysize 400 - 230
        background "#e0005d88"

    button:
        xpos 1770
        ypos 230
        xsize 1910 - 1770
        ysize 400 - 230
        background None
        hover_background None

        mouse "move"

        action Jump("ninth_apartment_scene")


    # to the park

    frame:
        xpos 1160
        ypos 550
        xsize 1620 - 1160
        ysize 760 - 550
        background "#e0005d88"

    button:
        xpos 1160
        ypos 550
        xsize 1620 - 1160
        ysize 760 - 550
        background None
        hover_background None

        mouse "move"

        action Jump("eigth_apartment_scene")

    #back to 1st apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("first_apartment_scene")