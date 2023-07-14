The Basics
-------------------

Every TermUI app will start with the same but small boilerplate.

This guide will walk you through that boilerplate and more  basics of TermUI; Create a UI, a Region, and finally add an element to the region.

Object Hierarchy and Structure
*******************************

In TermUI the three main objects, UI, Region, and Elements have a hierarchy; Its important to understand how it effects the UI you are making.

The UI
~~~~~~~~~~~~

Very simply, the UI is the foundation of your program; You can have multiple of these, but only one can be activate at a time.

The UI controls how and when regions inside of it are interacted with as well as the drawing of each frame.

Lets create some basic boilerplate for a TermUI app:

.. code-block:: py

    import curses
    from TermUI.ui import UI


    def main(stdscr):

        ui = UI(stdscr)  # create our main ui

        # other UI components

        ui.activate() # activate the ui loop, this should always be the last line.


    if __name__ == "__main__":
        curses.wrapper(main)


If you dont understand whats going on with the ``curses.wrapper()`` thats okay! 
TermUI was built around curses and uses it for drawing to the screen. In about 99% of your apps, you will never have to write curses code.

Regions
~~~~~~~~~~~~~~~

The Region is the home of your elements (buttons, text, textboxes, and checkboxes.).

It sits inside of the UI object and acts as a positioning layer between your elements and the UI loop.

To use a region, we have to add it to the UI object using ``UI().add_region()``

Lets expand on our boilerplate from the UI section:

.. code-block:: py

    import curses
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.position import Position


    def main(stdscr):
        ui = UI(stdscr)  # create our main ui
        region = Region(name="A cool name!",
                    position=Position.ORIGIN(), size=Position.DEFAULT_TERM_SIZE()) 
        # create our region

        ui.add_region(region) # add the region to the ui
        ui.activate() # activate the ui loop, this should always be the last line. 

    if __name__ == "__main__":
        curses.wrapper(main)

For now, you dont have to understand positioning, but for clarities sake:
    * Position.ORIGIN() = Position(0, 0) = Top left corner of the parent object.
    * Position.DEFAULT_TERM_SIZE() = Position(108, 28) = The default terminal size for most modern operating systems.

Elements
~~~~~~~~~~

    * :doc:`text`
    * :doc:`button`
    * :doc:`checkbox`
    * :doc:`textbox`

Elements are the things you interact with.

To use an element, we have to add it to the Region object using ``Region().add_element()``

Lets add a piece of text to our code:

.. code-block:: py

    import curses
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.text import Text
    from TermUI.position import Position


    def main(stdscr):
        ui = UI(stdscr)  # create our main ui
        region = Region(title="A cool name!",
                    position=Position.ORIGIN(), size=Position.DEFAULT_TERM_SIZE()) 
        # create our region with the default terminal size for most operating systems. 
        # Position.ORIGIN() = Position(0,0)
        # Position.DEFAULT_TERM_SIZE() = Position(108, 28)

        text = Text(content="My first element!", position=Position.ORIGIN()) 
        # create our text element, with the text "My first element!"
        # and place it at the origin or (0,0) of the region.
        # Position.ORIGIN() = Position(0,0)

        region.add_element(text) # add the text to our region.

        ui.add_region(region) # add the region to the ui
        ui.activate() # activate the ui loop, this should always be the last line. 

    if __name__ == "__main__":
        curses.wrapper(main)

Your Next Steps
~~~~~~~~~~~~~~~~~~

Learn about the UI, Regions, Positioning, Coloring and Packing.

    * :doc:`ui`
    * :doc:`region`
    * :doc:`position`
    * :doc:`colors`
    * :doc:`packing`

Learn about the Elements and how they can interact with each other:

    * :doc:`element`
    * :doc:`text`
    * :doc:`button`
    * :doc:`checkbox`
    * :doc:`textbox`


Lastly, :doc:`createanapp`!