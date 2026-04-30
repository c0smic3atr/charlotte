screen CarNotePopup():

    tag carnote
    modal True

    add Solid("#0008")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 800

        background None

        padding (0,0)

        #temporary until we make a new note background
        add "bgnotebook"

        text "this is a test"

        #close the note
        textbutton "Close":
            xpos 60
            ypos 730
            text_idle_color "#9DA9C2" # Color when not hovered
            text_hover_color "#404752" # Color when hovered