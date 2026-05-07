label fourteenth_apartment_scene:
    $ current_time = "5:28"
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
    $ current_time = "5:31"
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
    $ current_time = "5:31"
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
    $ current_time = "5:31"
    scene bg officedesk
    call screen officeDeskButtonNav
    "You're at the desk"
    menu: 
        
        "Go back":
            jump fifteenth_apartment_scene



screen throughWindow():
    # through the window

    frame:
        xpos 2
        ypos 10
        xsize 585 - 2
        ysize 350 - 10
        background None

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
        xpos 2
        ypos 480
        xsize 315 - 2
        ysize 760 - 480
        background None

    button:
        xpos 2
        ypos 480
        xsize 315 - 2
        ysize 760 - 480
        background None
        hover_background None

        mouse "move"

        action Jump("sixteenth_apartment_scene")

    # Desk

    frame:
        xpos 965
        ypos 165
        xsize 1645 - 965
        ysize 420 - 165
        background None

    button:
        xpos 965
        ypos 165
        xsize 1645 - 965
        ysize 420 - 165
        background None
        hover_background None

        mouse "move"

        action Jump("seventeenth_apartment_scene")

    # Door

    frame:
        xpos 335
        ypos 60
        xsize 670 - 335
        ysize 595 - 60
        background None

    button:
        xpos 335
        ypos 60
        xsize 670 - 335
        ysize 595 - 60
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
        xpos 0.45
        ypos 0.55
        idle "TableNoteButton.png"
        action [SetVariable("object_visible", True)]

    

    if object_visible:
        # The area to click that pops up/shows the image
        imagebutton:
                idle "TableNote.png" # The image that appears
                xpos 465 ypos 10       # Position on screen
                mouse "move"
           
                # Action: Set variable to False to make it disappear
                action [SetVariable("object_visible", False)]
                
default object_visible2 = False

screen officeDeskButtonNav():
    #Go back
    imagebutton:
        xanchor 0.5
        yanchor -675
        xpos 0.5
        ypos 0.28
        idle "Arrowbutton.png"
        mouse "move"
        action [SetVariable("object_visible", False), SetVariable("object_visible2", False), Jump("fifteenth_apartment_scene")]


    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 175
        ypos 180
        idle "deskNoteButton.png"
        action [SetVariable("object_visible", True)]

    if object_visible:
        # The area to click that pops up/shows the image
        imagebutton:
                idle "DeskNote.png" # The image that appears
                xpos 90 ypos 5       # Position on screen
                mouse "move"
           
                # Action: Set variable to False to make it disappear
                action [SetVariable("object_visible", False), SetVariable("object_visible2", True)]

    if object_visible2:
                imagebutton:
                    idle "DeskNote2.png"
                    xpos 90 ypos 5 
                    mouse "move"

                    action [SetVariable("object_visible2", False)]
