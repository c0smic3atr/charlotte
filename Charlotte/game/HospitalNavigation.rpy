label eigteenth_apartment_scene:
    $ oxygen_loss = 6
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
  
    scene bg road to hospital
    call screen eigteenthApartmentNav

    "You've left the office building"
    menu: 
        "Continue toward the road":
            jump ninteenth_apartment_scene
        "Investigate blockade":
            jump twentieth_apartment_scene
        "Go back":
            jump fifteenth_apartment_scene

label twentieth_apartment_scene:
    scene bg blockade
    "Youre at the blockade"
    menu:
        "Go back":
            jump eigteenth_apartment_scene

label ninteenth_apartment_scene:
    scene bg hospital
    call screen enteringHospital

    "You're approaching the hospital"
    menu:
        "Enter Hospital":
            jump twentyfirst_apartment_scene
        "Go back":
            jump eigteenth_apartment_scene

label twentyfirst_apartment_scene:
    scene bg front hospital
    "Youre in the hospital"
    menu:
        "Enter storage room":
            jump twentysecond_apartment_scene
        "Enter operating room":
            jump twentythird_apartment_scene
        "Enter hallway":
            jump twentyfourth_apartment_scene
        "Go back":
            jump ninteenth_apartment_scene

label twentysecond_apartment_scene:
    scene bg hospital storage room
    "You're in the storage room"
    menu: 
        "Go back":
            jump twentyfirst_apartment_scene

label twentythird_apartment_scene:
    scene bg operating room
    "You're in the operating room"
    menu: 
        "Go back":
            jump twentyfirst_apartment_scene

label twentyfourth_apartment_scene:
    scene bg hospital hallway
    "You're in the hallway"
    menu:
        "Enter left door":
            jump twentyfifth_apartment_scene
        "Enter right door":
            jump twentysixth_apartment_scene
        "Investigate door at the end of the hall":
            jump twentyseventh_apartment_scene
        "Go back":
            jump twentyfirst_apartment_scene

label twentyfifth_apartment_scene:
    scene bg hospital room one
    "Youre in the first hospital room"
    show character1onehospital
    menu:
        "Go back":
            jump twentyfourth_apartment_scene

label twentysixth_apartment_scene:
    scene bg hospital room two
    "You're in the second hospital room"
    menu:
        "Go back":
            jump twentyfourth_apartment_scene

label twentyseventh_apartment_scene:
    scene bg back room hospital
    "You're in the back room"
    menu:
        "Exit the hospital":
            jump twentyeigth_apartment_scene

        "Go back":
            jump twentyfourth_apartment_scene

screen eigteenthApartmentNav():
    # to blockage

    frame:
        xpos 175
        ypos 105
        xsize 415 - 175
        ysize 255 - 105
        background "#6527F5"

    button:
        xpos 175
        ypos 105
        xsize 415 - 175
        ysize 255 - 105
        background None
        hover_background None

        mouse "move"

        action Jump("twentieth_apartment_scene")

    # down the road

    frame:
        xpos 1600
        ypos 30
        xsize 1790 - 1600
        ysize 190 - 30
        background "#6527F5"

    button:
        xpos 1600
        ypos 30
        xsize 1790 - 1600
        ysize 190 - 30
        background None
        hover_background None

        mouse "move"

        action Jump("ninteenth_apartment_scene")

    #go back

    frame:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background "#6527F5"

    button:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background None
        hover_background None

        mouse "move"

        action Jump("eigteenth_apartment_scene")

screen enteringHospital():
    # enter the hospital

    frame:
        xpos 790
        ypos 430
        xsize 960 - 790
        ysize 560 - 430
        background "#6527F5"

    button:
        xpos 790
        ypos 430
        xsize 960 - 790
        ysize 560 - 430
        background None
        hover_background None

        mouse "move"

        action Jump("twentyfirst_apartment_scene")


    #go back

    frame:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background "#6527F5"

    button:
        xpos 7
        ypos 490
        xsize 181 - 7
        ysize 760 - 490
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")