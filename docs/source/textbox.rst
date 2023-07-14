The Textbox
------------------

The Textbox is the user input box.

Features:
    * Lost Focus on click
    * Clearing the box with the delete key
    * Key input callbacks to a custom method
    * Password mode which hides the typed characters
    * Placeholder text
    * Character limit
    * Over-Type box scrolling (move with the text if the text is longer than the box.)

Creation
***********

.. code-block:: py

    from TermUI.textbox import Textbox
    from TermUI.position import Position

    textbox = Textbox("Placeholder Text", Position(0,0), Position(40,0))


Properties
*************

Some properties are properties of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~

``placeholder: str`` - The current placeholder text.

``placeholder_active: bool`` - Whether to draw the placeholder.

``on_enter: Function`` - A function to run when the enter key is hit inside of a textbox. Sends the textbox as the functions argument.

``on_input: Function`` - A function to run when a character is typed in the textbox. Sends the ``chr()`` as the functions argument.

``placeholder_color: int`` - A color_pair int for the placeholder color. See :doc:`colors`

``maxchars: int`` - The calculated max chars to fit inside this textbox.

``char_limit: int`` - The max amount of characters allowed to be typed into this box. Defaults to 0 aka infinite. 

``password: bool`` - Whether to hide the text from display using asterisks. Defaults to False

``text: str`` - The text stored in the textbox.

``display: str`` - The text displayed in the textbox.

Methods
***********

Some methods are methods of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~

``reset() -> None`` - Empty the textbox.