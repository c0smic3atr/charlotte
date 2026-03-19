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

    menu:
        "Investigate parking lot":
            jump sixth_apartment_scene
            scene bg parking lot
            
           
        "Investigate apartment block two":
            jump seventh_apartment_scene
            scene bg apartments2

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
    "In parking lot"
    menu:
        "Go back":
            jump fifth_apartment_scene
       

label seventh_apartment_scene:
    scene bg apartments2
    "At apartments2"
    
    menu:
        "Go back":
            jump fifth_apartment_scene

label eigth_apartment_scene:
    scene bg park
    "At park"
    menu:
        "Go back":
            jump fifth_apartment_scene

label ninth_apartment_scene:
    scene bg blocked area
    "You cannot go here"
    menu: 
        "Explore alley":
            jump tenth_apartment_scene
        "Go back":
            jump fifth_apartment_scene
            

label tenth_apartment_scene:
    scene bg alley one
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
    "You've met a dead end"
    menu:
        "Go back":
            jump tenth_apartment_scene

label fourteenth_apartment_scene:
    scene bg alley window
    menu:
        "Go through the window":
            jump fifteenth_apartment_scene
        "Go back":
            jump tenth_apartment_scene

label fifteenth_apartment_scene:
    scene bg office two
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
