default timesEnteredSecondApartmentScene = 0

label fifth_apartment_scene:
    scene bg apttwo
    if timesEnteredSecondApartmentScene == 0:
        thought "The Hell? The sky's changed... and the weather. What time is it anyway?"
        thought "It's getting dark out. Swear I got here at, like, noon?"
        thought "Whatever, gotta stay focused."
        $ timesEnteredSecondApartmentScene += 1
        call screen fifthApartmentNav
    else:
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


    #go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action Jump("first_apartment_scene")