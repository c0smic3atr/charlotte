# IMAGES
#========================================================
image bgnotebook = "UserInterface/Notebook.png"


# NOTEBOOK PAGE TRACKING
# =========================================================
# This keeps track of which page the player is viewing.
default notebook_page = 0

# Total number of pages minus 1
# If there are 2 pages, the max page index is 1.
default notebook_max_page = 2


# =========================================================
# NOTEBOOK SCREEN
# =========================================================
screen notebook_screen():

    tag notebook
    modal True

    # Dark transparent overlay behind the notebook
    add Solid("#0008")

    # Main notebook window
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 800

        # Remove frame background
        background None

        # Remove default margins
        padding (0,0)

        add "bgnotebook"

        # -------------------------------------------------
        # MAIN LAYOUT
        # -------------------------------------------------
        # We use an hbox to split the notebook into two sections:
        # 1. Left side for portrait
        # 2. Right side for notes
        hbox:
            spacing 40
            xpos 40
            ypos 40

            # =================================================
            # LEFT SIDE: CHARACTER PORTRAIT
            # =================================================
            frame:
                xsize 310
                ysize 260
                xpos 190 - 45
                ypos 120 - 35

                # Remove frame background
                background None

                # Remove default margins
                padding (0,0)

                # Show a different portrait depending on the current page
                if notebook_page == 0:
                    add anna_facts['portrait']:
                        xalign 0.5
                        yalign 0.5
              
                elif notebook_page == 1:
                    add sarah_facts['portrait']:
                        xalign 0.5
                        yalign 0.5
                elif notebook_page == 2:
                    add rick_facts['portrait']:
                        xalign 0.5
                        yalign 0.5

            # =================================================
            # RIGHT SIDE: CHARACTER NOTES
            # =================================================
            frame:
                xsize 750
                ysize 650
                xpos 550 - 350
                ypos 90 - 80

                # Remove frame background
                background None

                # Remove default margins
                padding (0,0)

                vbox:
                    spacing 20
                    xpos 30   
                    ypos 30

                    # Show different notes depending on the current page
                    if notebook_page == 0:

                        text anna_facts['name'] size 42
                        text "Notes:" size 30

                        text "* [anna_facts['fact1']]"
                        text "* [anna_facts['fact2']]"
                        text "* [anna_facts['fact3']]"

                    elif notebook_page == 1:

                        text sarah_facts['name'] size 42
                        text "Notes:" size 30

                        text "* [sarah_facts['fact1']]"
                        text "* [sarah_facts['fact2']]"
                        text "* [sarah_facts['fact3']]"
                    elif notebook_page == 2:

                        text rick_facts['name'] size 42
                        text "Notes:" size 30

                        text "* [rick_facts['fact1']]"
                        text "* [rick_facts['fact2']]"
                        text "* [rick_facts['fact3']]"

        # -------------------------------------------------
        # PAGE NUMBER
        # -------------------------------------------------
        text "Page [notebook_page + 1] / [notebook_max_page + 1]":
            xalign 0.5
            yalign 0.93

        # -------------------------------------------------
        # PREVIOUS BUTTON
        # -------------------------------------------------
        if notebook_page > 0:
            textbutton "Previous":
                xpos 60
                ypos 730
                action SetVariable("notebook_page", notebook_page - 1)

        # -------------------------------------------------
        # NEXT BUTTON
        # -------------------------------------------------
        if notebook_page < notebook_max_page:
            textbutton "Next":
                xpos 1240
                ypos 730
                action SetVariable("notebook_page", notebook_page + 1)

    # Press N to close notebook
    key "n" action Hide("notebook_screen")


# =========================================================
# NOTEBOOK KEY LISTENER
# =========================================================
# This lets the player press N at any time to open/close
# the notebook.
screen notebook_key_listener():
    key "n" action [SetVariable("notebook_page", 0), ToggleScreen("notebook_screen")]


# =========================================================
# REGISTER THE KEY LISTENER
# =========================================================
init python:
    if "notebook_key_listener" not in config.overlay_screens:
        config.overlay_screens.append("notebook_key_listener")