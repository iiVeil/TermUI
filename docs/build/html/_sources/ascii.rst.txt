Ascii Art in TermUI
-----------------------

Ascii Art was always possible in TermUI but I decided to make it easily accessible by allowing developers to dodge all the positioning math.


Using AsciiArt()
*******************

Lets draw the D-Word ascii art logo into the center of a region.

.. code-block:: py

    import curses
    from TermUI.ui import UI
    from TermUI.region import Region
    from TermUI.position import Position
    from TermUI.Toolkit.asciiart import AsciiArt


    def main(stdscr):

        ui = UI(stdscr)

        region = Region(title="A cool name", position=Position(
            0, 0), size=Position(108, 28))

        art = " ______                   _______  _______  ______  \n(  __  \        |\     /|(  ___  )(  ____ )(  __  \ \n| (  \  )       | )   ( || (   ) || (    )|| (  \  )\n| |   ) | _____ | | _ | || |   | || (____)|| |   ) |\n| |   | |(_____)| |( )| || |   | ||     __)| |   | |\n| |   ) |       | || || || |   | || (\ (   | |   ) |\n| (__/  )       | () () || (___) || ) \ \__| (__/  )\n(______/        (_______)(_______)|_/  \___(_______/"
        # the ascii art can be a string with new line chars (\n) or a list of lines.

        ascii = AsciiArt(art, region, region.size.half())
        # AsciiArt(lines, region, position)
        ascii.create()
        # initialize the text objects

        ui.add_region(region)
        ui.activate()


    if __name__ == "__main__":
        curses.wrapper(main)



Adding more functionality
*****************************************

You might want to add some extra functionality into your ascii art like an on click event or a hover event

.. code-block:: py

    for element in ascii.elements:
        element.color = ...
        element.callback = ...

Its really as simple as that, ``ascii.elements`` is a list of all elements that make up your art meaning you can change each line seperately if youd like, or all at once like this example.