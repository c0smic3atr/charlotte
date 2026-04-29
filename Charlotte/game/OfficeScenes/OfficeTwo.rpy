label fourteenth_apartment_scene:
    $ contamination_level = 3
    call use_oxygen
    if oxygen <= 0:
        jump out_of_oxygen
    
    scene bg window2alley
    call screen throughWindow

    menu:
        "Go through the window":
            jump fifteenth_apartment_scene
        "Go back":
            jump tenth_apartment_scene

label fifteenth_apartment_scene:
    scene bg mainoffice
    call screen officeTwoNav

    "You're in the second office"
    menu:
        "Investigate table":
            jump sixteenth_apartment_scene
        "Investigate desk":
            jump seventeenth_apartment_scene
        "Go out door":
            jump eigteenth_apartment_scene
        "Go back":
            jump fourteenth_apartment_scene

label sixteenth_apartment_scene:
    scene bg officetable
    call screen officeTableButtonNav
    "Youre at the table"
    menu:
        
        "Go back":
            jump fifteenth_apartment_scene

label seventeenth_apartment_scene:
    scene bg officedesk
    call screen officeDeskButtonNav
    "You're at the desk"
    menu: 
        
        "Go back":
            jump fifteenth_apartment_scene



screen throughWindow():
    # through the window

    frame:
        xpos 190
        ypos 100
        xsize 660 - 190
        ysize 260 - 100
        background "#6527F5"

    button:
        xpos 190
        ypos 100
        xsize 660 - 190
        ysize 260 - 100
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")


    # back to tenth apartment scene

    frame:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background "#6527F5"

    button:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background None
        hover_background None

        mouse "move"

        action Jump("tenth_apartment_scene")

screen officeTwoNav():
    # Table

    frame:
        xpos 85
        ypos 265
        xsize 300 - 85
        ysize 390 - 265
        background "#6527F5"

    button:
        xpos 85
        ypos 265
        xsize 300 - 85
        ysize 390 - 265
        background None
        hover_background None

        mouse "move"

        action Jump("sixteenth_apartment_scene")

    # Desk

    frame:
        xpos 1290
        ypos 205
        xsize 1550 - 1290
        ysize 355 - 205
        background "#6527F5"

    button:
        xpos 1290
        ypos 205
        xsize 1550 - 1290
        ysize 355 - 205
        background None
        hover_background None

        mouse "move"

        action Jump("seventeenth_apartment_scene")

    # Door

    frame:
        xpos 485
        ypos 2
        xsize 620 - 485
        ysize 145 - 2
        background "#6527F5"

    button:
        xpos 485
        ypos 2
        xsize 620 - 485
        ysize 145 - 2
        background None
        hover_background None

        mouse "move"

        action Jump("eigteenth_apartment_scene")


    # back to fourteenth apartment scene

    frame:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background "#6527F5"

    button:
        xpos 690
        ypos 890
        xsize 990 - 690
        ysize 1070 - 890
        background None
        hover_background None

        mouse "move"

        action Jump("fourteenth_apartment_scene")


screen officeTableButtonNav():
    # go back

    frame:
        xpos 210
        ypos 920
        xsize 1730 - 210
        ysize 1065 - 920
        background "#6527F5"

    button:
        xpos 210
        ypos 920
        xsize 1730 - 210
        ysize 1065 - 920
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")


    #grab the note (DOESNT WORK YET MAKE THE NOTE THING FIRST)

        #frame:
            #xpos 145
            #ypos 685
            #xsize 390 - 145
            #ysize 780 - 685
            #background "#77C7BA"

        #button:
            #xpos 145
            #ypos 685
            #xsize 390 - 145
            #ysize 780 - 685
            #background None
            #hover_background None

            #mouse "move"

            #action Jump("fifth_apartment_scene")

screen officeDeskButtonNav():
    # go back

    frame:
        xpos 260
        ypos 785
        xsize 1260 - 260
        ysize 1055 - 785
        background "#6527F5"

    button:
        xpos 260
        ypos 785
        xsize 1260 - 260
        ysize 1055 - 785
        background None
        hover_background None

        mouse "move"

        action Jump("fifteenth_apartment_scene")


    #grab the note (DOESNT WORK YET MAKE THE NOTE THING FIRST)

        #frame:
            #xpos 50
            #ypos 25
            #xsize 330 - 50
            #ysize 325 - 25
            #background "#77C7BA"

        #button:
            #xpos 50
            #ypos 25
            #xsize 330 - 50
            #ysize 325 - 25
            #background None
            #hover_background None

            #mouse "move"

            #action Jump("fifth_apartment_scene")