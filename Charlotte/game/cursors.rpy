# Cursor definitions
init -1 python:

    # Make sure the dictionary exists
    config.mouse = {}

    # Default cursor
    config.mouse["default"] = [
        ("images/Cursors/cursor_normal.png", 0, 0)
    ]

    # Hover cursor for doors
    config.mouse["move"] = [
        ("images/Cursors/cursor_move.png", 0, 0)
    ]