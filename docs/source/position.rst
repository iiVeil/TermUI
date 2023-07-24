Positioning
-------------

The ``Position`` object is a hyper simple 2D positioning tool.



Creation
*********

.. code-block:: py

    from pyTermUI.position import Position

    position = Position(x: int, y: int)

OR create it with a tuple ``(x, y)``

.. code-block:: py

    from pyTermUI.position import Position

    position = Position(xypair: tuple)


Properties
***********

Instance
~~~~~~~~~~

``x: int`` - Returns the x value

``y: int`` - Returns the y value


Methods
**********

Instance
~~~~~~~~~~

``half() -> Position`` - Returns a positioning object equal to half of the current x and y rounded down. 
    ``Position(10, 5).half()`` = ``Position(5, 2)``


Class
~~~~~~~~

``ORIGIN() -> Position`` - Returns ``Position(0, 0)``. This is here for clarities sake.

``DEFAULT_TERM_SIZE() -> Position`` - Returns ``Position(108, 28)``. This is the screenspace curses gets when a terminal is on the default size (120 columns, 30 rows). Its here because I hate remembering it.



Notable Features
******************

Position objects support addition and subtraction from other position objects.
    ex. ``Position(10,2) - Position(3, 1) = Position(7, 1)``

    ex. ``Position(10,2) + Position(3, 1) = Position(13, 3)``

Centering Elements
*********************

Centering objects can be a daunting task if you are looking at it blind.

To truly center an object in a region we first need the middle of the region, we can get that by using the size of the region, which can be found in ``Region().size``.

To get the horizontal center, take half of the regions size's x coordinate ``Region().size.half().x``

Getting the vertical center is no different ``Region().size.half().y``

Now to actually center an element, we need to offset it by half the length of the element (so the center of our element is on the middle space). Lets keep it simple and use text for this example.

We want to center ``I love TermUI!``.

.. code-block:: py

    import curses
    import math
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.text import Text
    from TermUI.position import Position


    def main(stdscr):

        ui = UI(stdscr)

        region = Region("", Position.ORIGIN(), Position.DEFAULT_TERM_SIZE())
        region.framed = False  # lets hide its border for now

        center_me = "I love TermUI!"
        # the text we want to center

        center_of_region = Position(region.size.half().x, region.size.half().y)
        # the center space in the region

        half_of_length = math.floor(len(center_me)/2)
        # get half the length of the string, rounded down because TermUI only works in whole numbers.

        offset_by_length = center_of_region - Position(half_of_length, 0)
        # offset the position by half of the length of the text

        text = Text(center_me, offset_by_length)

        region.add_element(text)

        ui.add_region(region)
        ui.activate()

    if __name__ == "__main__":
        curses.wrapper(main)

While we used text in this example, the same logic will work with any element.

Find the center, subtract by half of the length.