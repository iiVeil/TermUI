On Hover Effects (in the Terminal!!)
--------------------------------------------

TermUI now has support for on hover effects and they couldnt be easier to set up!

Using Hover Effects
*******************

Lets make a button turn green when we hover it.

.. code-block:: py
    
    import curses
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.button import Button
    from TermUI.position import Position
    from TermUI.Toolkit.hover import Hover


    def main(stdscr):


        # when we hover, make the button green and redraw
        def on_hover_button(element):
            element.color = 47
            element.region.ui.draw()

        # when we stop hovering, reset the color to the default color and redraw
        def off_hover_button(element):
            element.color = element.region.color
            element.region.ui.draw()

        ui = UI(stdscr)

        hover = Hover()

        region = Region(title="A cool name", position=Position(
            0, 0), size=Position(108, 28))

        button = Button("Login", region.size.half(), lambda _: ())
        # dont be scared by this lambda function
        # its just a function that does nothing when run acting as our callback for clicks.
        
        hover.add(button, on_hover_button, off_hover_button)

        region.add_element(button)

        ui.add_region(region)

        hover.build()
        # build our thread handler

        hover.run()
        # start the hover threads

        ui.activate()


    if __name__ == "__main__":
        curses.wrapper(main)

Extras
********

By default the wait time between hover recognition is 125 milliseconds.

This can be changed by changing ``Hover.wait``

Ex. ``Hover.wait = .250`` - 250 milliseconds