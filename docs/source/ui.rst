The UI
----------

The UI is a simple object and one you wont interact with much outside of adding regions to it and activating it.

Creation
***********

.. code-block:: py

    from pyTermUI.ui import UI

    ui = UI(stdscr: curses.stdscr)

for more information on UI creation and TermUI boilerplate see: :doc:`basics`

Properties
**************

Instance
~~~~~~~~~~~~

``regions: list`` - A list of regions added to the ui using ``UI().add_region()``.

``draw_callback: Function`` - A method to run immediately before every frame is drawn. Default is ``None``. Passes no arguments to the callback function.

``event_callback: Function`` - A method to run when a input is recieved via ``stdscr.getch()``. Default is ``None``. Passes the curses event to the callback function.

``default_color: int`` - The curses ``color_pair()`` int that will propogate to regions inside of it that have no color set. Default is ``232``.

Class
~~~~~~~~~~

``last_element_clicked: int`` - The unix epoch time of the last time a element was clicked

``clickable_cooldown: int`` - The cooldown between clicks in milliseconds. Default is 300

Methods
**********

``add_region(region: Region) -> None`` - Add a region to this UI, allowing it and its elements to be drawn in the UI loop.

``draw() -> None`` - Draw the next frame instantly. This is seperate from the UI loop that normally draws the frame once every interaction (clicks and terminal resizes).

``get_clickable(position: Position) -> Element`` - Click an element at a position if an element occupies the coordinates, is not hidden, and is placed in a region inside the currently active UI. 

        ``get_clickable`` is **overly complicated and slow**, just use ``Element().event_mask()`` if you want to click on an element programatically.

``swap(ui: UI) -> None`` - Swap control of the UI loop to another UI object. Useful if you have specific "scenes", like a login and main screen.

``activate() -> None`` - Activate the UI loop. In most cases, this should be the last thing you do when creating your UI. This loop is blocking.

``add_toolkits(*args: Toolkit-Instance) -> None`` - Setup toolkits for cleanup when the program ends.

Overdrawing
********************

The UI object will not allow you to overdraw outside of curses space. In the case that you do, we choose to ignore the data until the space is large enough to fit it, allowing you to resize your terminal in real time.

Understanding the UI loop
**************************

The UI loop is pretty simple but understanding it fully will help you write better TermUI code.

It consists of 3 steps:
    * Wait for an input (click or resize)
    * Clicks check the clicked position for a non-hidden element that is inside of a region, and runs its underlying click method if it exists (the click method runs the callback when its core functionality finishes).  
    * Terminal resizes will dynamically update and refresh the available working space for curses.
