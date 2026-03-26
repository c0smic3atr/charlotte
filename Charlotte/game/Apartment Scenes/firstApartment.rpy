label first_apartment_scene:
    scene bg aptone
    
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
        xpos 240
        ypos 250
        xsize 350 - 240
        ysize 320 - 250
        background "#e0005d88"

    button:
        xpos 240
        ypos 250
        xsize 350 - 240
        ysize 320 - 250
        background None
        hover_background None

        mouse "move"

        action Jump("second_apartment_scene")


        # to the apartment fence area
    frame:
        xpos 1200
        ypos 300
        xsize 1475 - 1200
        ysize 500 - 300
        background "#000000"

    button:
        xpos 1200
        ypos 300
        xsize 1475 - 1200
        ysize 500 - 300
        background None
        hover_background None

        mouse "move"

        action Jump("third_apartment_scene")

        # to the fifth apartment scene
    frame:
        xpos 660
        ypos 50
        xsize 930 - 660
        ysize 200 - 50
        background "#A0DB53"

    button:
        xpos 660
        ypos 50
        xsize 930 - 660
        ysize 200 - 50
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")