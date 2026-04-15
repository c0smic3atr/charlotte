label first_apartment_scene:
    scene bg aptonee
    
    call screen firstApartmentNavigation
    #
    #menu:
    #    "Investigate apartments":
    #        jump second_apartment_scene
   
    #    "Investigate fence":
    #        jump third_apartment_scene
    #    "Continue down the street":
    #        jump fifth_apartment_scene
    #




screen firstApartmentNavigation():

    # to the first apartment scene
    frame:
        xpos 6
        ypos 150
        xsize 490 - 6
        ysize 465 - 150
        background None


    button:
        xpos 6
        ypos 150
        xsize 490 - 6
        ysize 465 - 150
        background None
        hover_background None

        mouse "move"

        action Jump("second_apartment_scene")


        # to the apartment fence area
    frame:
        xpos 1675
        ypos 400
        xsize 1915 - 1675
        ysize 840 - 400
        background None

    button:
        xpos 1675
        ypos 400
        xsize 1915 - 1675
        ysize 840 - 400
        background None
        hover_background None

        mouse "move"

        action Jump("third_apartment_scene")

        # to the fifth apartment scene
    frame:
        xpos 1320
        ypos 130
        xsize 1580 - 1320
        ysize 415 - 130
        background None

    button:
        xpos 1320
        ypos 130
        xsize 1580 - 1320
        ysize 415 - 130
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")