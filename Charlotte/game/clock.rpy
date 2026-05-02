default current_time = "12:00"


screen clock_key_listener():
    key "c" action [ToggleScreen("clock_screen")]

# =========================================================
# Clock SCREEN
# =========================================================
screen clock_screen():

    tag clock
    modal True

    # Dark transparent overlay behind the notebook
    add Solid("#0008")

    # Main notebook window
    #frame:
        #xalign 0.5
        #yalign 0.5
        #xsize 1400
        #ysize 800

        # Remove frame background
        #background None

        # Remove default margins
        #padding (0,0)

        
    frame:
        xsize 310
        ysize 260
        xpos 190 - 45
        ypos 120 - 35
        #background None
        #padding (0,0)
        text current_time size 60
        
    key "c" action Hide("clock_screen")


# =========================================================
# REGISTER THE KEY LISTENER
# =========================================================
init python:
    if "clock_key_listener" not in config.overlay_screens:
        config.overlay_screens.append("clock_key_listener")

