label first_apartment_scene:
    scene bg apartments1
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

    # Left door → Room A
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


screen fenceNavigation():

    # Left door → Room A
    frame:
        xpos 1419
        ypos 276
        xsize 1199 - 1419
        ysize 289 - 276
        background "#e0005d88"

    button:
        xpos 1419
        ypos 276
        xsize 1199 - 1419
        ysize 289 - 276
        background None
        hover_background None

        mouse "move"

        action Jump("third_apartment_scene")