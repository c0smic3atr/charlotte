# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Employer")
define p = Character ("Player")
define a = Character ("Anna")
define s = Character ("Sarah")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg car interior

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

   

    # These display lines of dialogue.

    e "Could you end a human life?"
    e "..."
    e "I know this isn't your typical line of work"
    e "But it'll be a service to 'em, you'll see"
    e "Putting them down"
    e "Quick and painless"
    p "Like a dog"
    e "Don't get all sentimental on me"
    e "It's not unlike you to try to worm your way out of responsibility"
    e "Not this time. We've all got jobs to do"
    p "Wasn't aware mine is 'interrogation and execution'"
    p "Thought that was more your thing"
    e "Used to be. I'm passing down the torch"
    e "Lucky you"


    jump first_apartment_scene
   


 

    




            

label fifth_apartment_scene:
    scene bg apartments3
    call screen fifthApartmentNav

    menu:
        #"Investigate parking lot":
            #jump sixth_apartment_scene
            #scene bg parking lot
            
           
        #"Investigate apartment block two":
            #jump seventh_apartment_scene
            #scene bg apartments2

        "Investigate park":
            jump eigth_apartment_scene
            scene bg park

        "Continue down the road":
            jump ninth_apartment_scene
            scene bg blocked area

        "Go back":
            jump first_apartment_scene
            scene bg apartments1


       
        

label sixth_apartment_scene:
    scene bg parking lot
    call screen sixthApartmentNav

    "In parking lot"
    menu:
        "Go back":
            jump fifth_apartment_scene
       

label seventh_apartment_scene:
    scene bg apartments2
    call screen seventhApartmentNav

    "At apartments2"
    
    menu:
        "Go back":
            jump fifth_apartment_scene

label eigth_apartment_scene:
    scene bg park
    call screen eigthApartmentNav

    "At park"
    menu:
        "Go back":
            jump fifth_apartment_scene

label ninth_apartment_scene:
    scene bg blocked area
    call screen ninthApartmentNav

    "You cannot go here"
    menu: 
        "Explore alley":
            jump tenth_apartment_scene
        "Go back":
            jump fifth_apartment_scene
            

label tenth_apartment_scene:
    scene bg alley one
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

label eleventh_apartment_scene:
    scene bg office
    call screen firstOffice

    "You are at the office"

    menu:
        "Go inside office":
            jump twelvth_apartment_scene
        "Go back":
            jump tenth_apartment_scene

label twelvth_apartment_scene:
    scene bg office one
    "You are in the office"
    menu:
        "Leave office":
            jump tenth_apartment_scene

    
label thirteenth_apartment_scene:
    scene bg dead end alley one
    call screen deadEnd

    "You've met a dead end"
    menu:
        "Go back":
            jump tenth_apartment_scene

label fourteenth_apartment_scene:
    scene bg alley window
    call screen throughWindow

    menu:
        "Go through the window":
            jump fifteenth_apartment_scene
        "Go back":
            jump tenth_apartment_scene

label fifteenth_apartment_scene:
    scene bg office two
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
    scene bg desk
    "Youre at the table"
    menu:
        "Interact with papers"
        "Go back":
            jump fifteenth_apartment_scene

label seventeenth_apartment_scene:
    scene bg office desk
    "You're at the desk"
    menu: 
        "Pick up the phone"
        "Go back":
            jump fifteenth_apartment_scene
label eigteenth_apartment_scene:
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
label ninteenth_apartment_scene:
    scene bg hospital
    call screen enteringHospital

    "You're approaching the hospital"
    menu:
        "Enter Hospital":
            jump twentyfirst_apartment_scene
        "Go back":
            jump eigteenth_apartment_scene
     

label twentieth_apartment_scene:
    scene bg blockade
    "Youre at the blockade"
    menu:
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

label twentyeigth_apartment_scene:
    scene bg enter end scene
    "Fence before end scene"
    menu:
        "Continue onward":
            scene
        "Go back":
            jump twentyseventh_apartment_scene


label twentyninth_apartment_scene:
    scene bg warehouse
    "You're outside the warehouse"
    menu:
        "Investigate body bags":
            jump thirtieth_apartment_scene
        "Go back":
            jump twentyeigth_apartment_scene

label thirtieth_apartment_scene:
    scene bg end scene fence
    "You're looking at the bags"
    menu:
        "Go back":
            jump twentyninth_apartment_scene


    # This ends the game.

    return


screen fifthApartmentNav():
    # to the parking lot scene
    frame:
        xpos 150
        ypos 190
        xsize 380 - 150
        ysize 430 - 190
        background "#e0005d88"

    button:
        xpos 150
        ypos 190
        xsize 380 - 150
        ysize 430 - 190
        background None
        hover_background None

        mouse "move"

        action Jump("sixth_apartment_scene")


    # to the second set of apartments
    frame:
        xpos 1195
        ypos 25
        xsize 1410 - 1195
        ysize 190 - 25
        background "#e0005d88"

    button:
        xpos 1195
        ypos 25
        xsize 1410 - 1195
        ysize 190 - 25
        background None
        hover_background None

        mouse "move"

        action Jump("seventh_apartment_scene")

    # to continue down the road

    frame:
        xpos 1770
        ypos 230
        xsize 1910 - 1770
        ysize 400 - 230
        background "#e0005d88"

    button:
        xpos 1770
        ypos 230
        xsize 1910 - 1770
        ysize 400 - 230
        background None
        hover_background None

        mouse "move"

        action Jump("ninth_apartment_scene")


    # to the park

    frame:
        xpos 1160
        ypos 550
        xsize 1620 - 1160
        ysize 760 - 550
        background "#e0005d88"

    button:
        xpos 1160
        ypos 550
        xsize 1620 - 1160
        ysize 760 - 550
        background None
        hover_background None

        mouse "move"

        action Jump("eigth_apartment_scene")

    #back to 1st apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("first_apartment_scene")


screen sixthApartmentNav():
    #back to 5th apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen seventhApartmentNav():
    #back to 5th apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen eigthApartmentNav():
    #back to 5th apartment scene

    frame:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background "#6527F5"

    button:
        xpos 500
        ypos 980
        xsize 1190 - 500
        ysize 1060 - 980
        background None
        hover_background None

        mouse "move"

        action Jump("fifth_apartment_scene")


screen ninthApartmentNav():

    # to the alley

    frame:
        xpos 1465
        ypos 730
        xsize 1740 - 1465
        ysize 870 - 730
        background "#e0005d88"

    button:
        xpos 1465
        ypos 730
        xsize 1740 - 1465
        ysize 870 - 730
        background None
        hover_background None

        mouse "move"

        action Jump("tenth_apartment_scene")



    #back to 5th apartment scene

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

        action Jump("fifth_apartment_scene")



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

        action Jump("ninth_apartment_scene")


screen firstOffice():
    # into the office

    frame:
        xpos 515
        ypos 850
        xsize 720 - 515
        ysize 1075 - 850
        background "#6527F5"

    button:
        xpos 515
        ypos 850
        xsize 720 - 515
        ysize 1075 - 850
        background None
        hover_background None

        mouse "move"

        action Jump("twelvth_apartment_scene")


screen deadEnd():
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