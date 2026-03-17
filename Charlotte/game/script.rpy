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
