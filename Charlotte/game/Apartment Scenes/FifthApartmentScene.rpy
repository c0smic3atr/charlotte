label fifth_apartment_scene:
    scene bg apttwo
    call screen fifthApartmentNav



screen fifthApartmentNav():
    # to the parking lot scene
    frame:
        xpos 230
        ypos 165
        xsize 520 - 230
        ysize 560 - 165
        background None

    button:
        xpos 230
        ypos 165
        xsize 520 - 230
        ysize 560 - 165
        background None
        hover_background None

        mouse "move"

        action Jump("sixth_apartment_scene")


    # to the second set of apartments
    frame:
        xpos 790
        ypos 70
        xsize 1200 - 790
        ysize 285 - 70
        background None

    button:
        xpos 790
        ypos 70
        xsize 1200 - 790
        ysize 285 - 70
        background None
        hover_background None

        mouse "move"

        action Jump("seventh_apartment_scene")

    # to continue down the road

    frame:
        xpos 1750
        ypos 305
        xsize 1900 - 1750
        ysize 560 - 305
        background None

    button:
        xpos 1750
        ypos 305
        xsize 1900 - 1750
        ysize 560 - 305
        background None
        hover_background None

        mouse "move"

        action Jump("ninth_apartment_scene")


    # to the park

    frame:
        xpos 1390
        ypos 710
        xsize 1880 - 1390
        ysize 1030 - 710
        background None

    button:
        xpos 1390
        ypos 710
        xsize 1880 - 1390
        ysize 1030 - 710
        background None
        hover_background None

        mouse "move"

        action Jump("eigth_apartment_scene")

    #back to 1st apartment scene

    frame:
        xpos 200
        ypos 925
        xsize 870 - 200
        ysize 1060 - 925
        background None

    button:
        xpos 200
        ypos 925
        xsize 870 - 200
        ysize 1060 - 925
        background None
        hover_background None

        mouse "move"

        action Jump("first_apartment_scene")