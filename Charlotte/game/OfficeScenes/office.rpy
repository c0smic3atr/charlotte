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