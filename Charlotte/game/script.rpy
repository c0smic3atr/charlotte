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

    scene bg carlayout

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
   

label first_apartment_scene:
    scene bg apartments1


    menu:
        "Investigate apartments":
            jump second_apartment_scene
   
        "Investigate fence":
            jump third_apartment_scene
        "Continue down the street":
            jump fifth_apartment_scene
 
label second_apartment_scene:
    scene bg apartments2

    menu:
        "Knock on door 1":
            show first apartment npc
            a "..."
            a "You don't look familiar"
            a "I'd know, being there's so few people in town these days"
            a "Not like there ever was many"
            a "What's your deal? If you're here to tell me to keep the noise down, you can get lost"
            p "Um, no"
            p "I've been sent to check up on the residents here. See how you're handling... things"
            a "Huh. I guess that checks out"
            a "Some of us will be pretty happy to see you here"
            a "But most of us gave up on an intervention a long time ago"
            p "Intervention?"
            a "Yeah. I mean, you can't blame us for wanting out"
            p "You know we can't just let you go"
            a "Some of us know better than others"
            a "You should talk to Sarah next door. She's something of an optimist"
            a "Seems to be handling things better than most"

            jump second_apartment_scene

        "Knock on door 2":
            show second apartment npc
            "you talked to door 2"
        "Go Back":
            jump first_apartment_scene

    jump second_apartment_scene
    



label third_apartment_scene:
    scene bg apartmentsfence

    menu:
        "Interact with trashcan":
            show trashcan npc
            "you talked to trashcan npc"
        "Go back":
            jump third_apartment_scene
            
label fourth_apartment_scene:
    scene bg apartments1
    
    menu:
        "Continue down the street":
            jump fifth_apartment_scene
            

label fifth_apartment_scene:
    scene bg apartments3

    menu:
        "Investigate parking lot":
            jump sixth_apartment_scene
            scene bg parking lot
            
           
        "Investigate apartment block two":
            jump seventh_apartment_scene
            scene bg apartments2

       
        

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

    
        

    







    # This ends the game.

    return
