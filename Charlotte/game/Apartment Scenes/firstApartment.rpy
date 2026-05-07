label first_apartment_scene:
    scene bg aptonee

    play music "music/Atmosphere.mp3" fadein 1.0 loop volume 1
   
    
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

        action Jump("theDumpsterArea")

    # to the fifth apartment scene
    imagebutton:
        xanchor -800
        yanchor 0.8
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton4.png"
        mouse "move"
        action Jump("fifth_apartment_scene")