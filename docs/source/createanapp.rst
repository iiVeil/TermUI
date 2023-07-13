Create your first app
------------------------

This app is very basic, but introduces you to some core concepts:
    * Callbacks; :doc:`element`
    * Dynamic Updating
    * Relative Positioning; :doc:`position`
    * Event Masking, allowing clicks on element A to act like a click on element B; :doc:`element`
    * Changing colors; :doc:`colors`
    * Centering objects in a region using ``Region().size.half()``; :doc:`position`
    * Element Packing, a shorthand for placing elements directly next to another element; :doc:`element`

This app does away with ``Position.ORIGIN()`` and ``Position.DEFAULT_TERM_SIZE()`` to show how low-level positioning works. If you prefer the named classmethods, feel free to use them.

.. code-block:: py

    import curses
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.checkbox import Checkbox
    from TermUI.position import Position
    from TermUI.text import Text


    def main(stdscr):

        def on_checkbox(checkbox):
            # what should happen when this checkbox is clicked?
            label.color = checkbox.color
            # set the label color to the checkbox color.

        ui = UI(stdscr)  # create our main ui

        region = Region(title="A cool name", position=Position(
            0, 0), size=Position(108, 28))  # create our region at 0,0 (top left corner)
        # Position(108, 28) is the default terminal screen size

        checkbox = Checkbox(checked=False, position=Position(
            region.size.half().x-3, region.size.half().y))
        # Center the checkbox inside of the region.
        
        checkbox.callback = on_checkbox
        # Point the checkboxes callback at the on_checkbox method.


        label = Text(content="A label", position=checkbox.pack.get("right"))
        # Notice how am I not specifying coordinates here, the pack dictionary has them for me
        # since I have already placed my checkbox.

        label.callback = checkbox.event_mask
        # Make the label click act as a checkbox click.

        label.color = checkbox.color
        # set the label color to the checkbox color.

        region.add_element(label)
        region.add_element(checkbox)
        
        ui.add_region(region)
        ui.activate()


    if __name__ == "__main__":
        curses.wrapper(main)