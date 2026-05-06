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
    thought "All relations have ceased? But they sent me. Nothing's ceased."
    thought "I thought I was the first to be sent out since..."
    thought "These notes are from forever ago..."
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


    #go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
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


    #go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action Jump("fourteenth_apartment_scene")

default object_visible2 = False

screen officeTableButtonNav():
    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        action [SetVariable("object_visible", False), Jump("fifteenth_apartment_scene")]


    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "test2.png"
        action [SetVariable("object_visible", True)]

    

    if object_visible:
        # The area to click that pops up/shows the image
        imagebutton:
                idle "TableNote.png" # The image that appears
                xpos 465 ypos 10       # Position on screen
                mouse "move"
           
                # Action: Set variable to False to make it disappear
                action [SetVariable("object_visible2", True), SetVariable("object_visible", False)]
                
    if object_visible2:
            imagebutton:
                idle "testArrow.png"
                xpos 1823 ypos 400
                mouse "move"

                action [SetVariable("object_visible2", False)]

screen officeDeskButtonNav():
    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action [SetVariable("object_visible", False), Jump("fifteenth_apartment_scene")]


    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 165
        ypos 80
        idle "test2.png"
        action [SetVariable("object_visible", True)]

    if object_visible:
        # The area to click that pops up/shows the image
        imagebutton:
                idle "DeskNote.png" # The image that appears
                xpos 90 ypos 5       # Position on screen
                mouse "move"
           
                # Action: Set variable to False to make it disappear
                action [SetVariable("object_visible", False)]

