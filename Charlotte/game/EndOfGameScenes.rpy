label twentyeigth_apartment_scene:
    $ contamination_level = 5
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg gggh

    "Fence before end scene"
    menu:
        "Continue onward":
            scene
        "Go back":
            jump twentyseventh_apartment_scene


label twentyninth_apartment_scene:
    scene bg vvb 
    "You're outside the warehouse"
    
    menu:
        "Investigate body bags":
            jump thirtieth_apartment_scene
        "Go back":
            jump twentyeigth_apartment_scene

label thirtieth_apartment_scene:
    scene bg bodybag
    "You're looking at the bags"
    menu:
        "Go back":
            jump twentyninth_apartment_scene
        "End it":
            jump trust_endings

    # This ends the game.

    return