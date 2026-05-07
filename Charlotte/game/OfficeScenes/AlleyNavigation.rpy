default timesEnteredAlleyNavigation = 0
label tenth_apartment_scene:
    $ current_time = "2:14"
    $ contamination_level = 3
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg mainalley
if timesEnteredAlleyNavigation == 0:
  

    thought "Ugh, it's hard to breathe in this place. Do I keep passing out or something? Is my gas mask broken?"
    thought "Why- why's it morning again?"
    thought "I need to get this over with."
    call oxygen_warning 
    y "Warning oxygen change, check filtration level"
    $ timesEnteredAlleyNavigation += 1
  

    call screen alleyNav
   
else: 
    call screen alleyNav

    

    menu:
        "Go down first alley":
            jump eleventh_apartment_scene
        "Go down second alley":
            jump thirteenth_apartment_scene
        "Go down third alley":
            jump fourteenth_apartment_scene
        "Go back":
            jump ninth_apartment_scene

label thirteenth_apartment_scene:
    scene bg alleyydead
    call screen deadEnd

    thought "There's nothing here..."
    $ current_time = "2:51"
    menu:
        "Go back":
            jump tenth_apartment_scene


screen alleyNav():
    # 1st alley

    frame:
        xpos 840
        ypos 30
        xsize 1010 - 840
        ysize 120 - 30
        background "#e0005d88"

    button:
        xpos 840
        ypos 30
        xsize 1010 - 840
        ysize 120 - 30
        background None
        hover_background None

        mouse "move"

        action Jump("eleventh_apartment_scene")

    # 2nd alley

    frame:
        xpos 1440
        ypos 270
        xsize 1500 - 1440
        ysize 470 - 270
        background "#e0005d88"

    button:
        xpos 1440
        ypos 270
        xsize 1500 - 1440
        ysize 470 - 270
        background None
        hover_background None

        mouse "move"

        action Jump("thirteenth_apartment_scene")

    # 3rd alley

    frame:
        xpos 400
        ypos 150
        xsize 490 - 400
        ysize 310 - 150
        background "#e0005d88"

    button:
        xpos 400
        ypos 150
        xsize 490 - 400
        ysize 310 - 150
        background None
        hover_background None

        mouse "move"

        action Jump("fourteenth_apartment_scene")

    # back to ninth apartment scene

    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action Jump("ninth_apartment_scene")

screen deadEnd():
    # back to tenth apartment scene
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action Jump("tenth_apartment_scene")