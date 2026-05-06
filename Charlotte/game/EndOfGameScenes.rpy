label twentyeigth_apartment_scene:
    $ contamination_level = 5
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg gggh
    call screen EndSceneNav
    "Fence before end scene"
    menu:
        "Continue onward":
            scene
        "Go back":
            jump twentyseventh_apartment_scene


label twentyninth_apartment_scene:
    scene bg vvb
    call screen WarehouseNav
    "You're outside the warehouse"
    
    menu:
        "Investigate body bags":
            jump thirtieth_apartment_scene
        "Go back":
            jump twentyeigth_apartment_scene

label thirtieth_apartment_scene:
    scene bg bodybag
    call screen BodyBagNav
    "You're looking at the bags"
    menu:
        "Go back":
            jump twentyninth_apartment_scene


    # This ends the game.

    return

screen EndSceneNav():
    frame:
        xpos 155
        ypos 50
        xsize 1845 - 155
        ysize 725 - 50
        background "#6527F5"

    button:
        xpos 155
        ypos 50
        xsize 1845 - 155
        ysize 725 - 50
        background None
        hover_background None

        mouse "move"

        action Jump("twentyninth_apartment_scene")


    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        action Jump("twentyseventh_apartment_scene")

screen WarehouseNav():
    frame:
        xpos 105
        ypos 500
        xsize 430 - 105
        ysize 685 - 500
        background "#6527F5"

    button:
        xpos 105
        ypos 500
        xsize 430 - 105
        ysize 685 - 500
        background None
        hover_background None

        mouse "move"

        action Jump("thirtieth_apartment_scene")


    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        action Jump("twentyseventh_apartment_scene")

screen BodyBagNav():
    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        action Jump("twentyninth_apartment_scene")