# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Employer")
define p = Character ("Player")
define thought = Character (None, what_prefix = "{i}", what_suffix="{/i}")
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

    e "I know this isn't your typical line of work"
    e "But it'll be a service to 'em, you'll see"
    e "Quick and painless, no fear. There are worse ways to go."
    p "Like putting down a dog."
    e "Don't get all sentimental on me, now"
    e "It's not unlike you to try to worm your way out of responsibility"
    e "Not this time"
    e "We've all got jobs to do."
    p "Wasn't prepared for mine to be 'interrogation and execution'"
    p "Thought that was more your thing."
    e "Used to be."
    e "I'm passing down the torch."
    e "Lucky you"


    jump first_apartment_scene
   
