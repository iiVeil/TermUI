The Button
-------------

While anything can be clickable, not everything is a button.

This element will draw a "clickable" looking button and requires a callback.

Creation
**************

.. code-block:: py

    from pyTermUI.button import Button
    from pyTermUI.position import Position

    def on_button(button):
        # swap the buttons colors between green and red when you click it
        button.color = 204 if button.clicked else 85

    button = Button("Change my color!", Position(0,0), on_button)
    button.color = 85

Properties
*************

Some properties are properties of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~

``text: str`` - The text displayed in the button.

``clicked: bool`` - Whether the button is in a clicked state, Functions as a checkbox.

``highlight: str`` - The pieces of text that should wrap the inner button text. Defaults to "><". This string should always be 2 characters

``framed: bool`` - Whether the buttons frame should be drawn.

Methods
***********

Some methods are methods of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~

``set_text(text: str) -> None`` - Set the inner text of the button and recalculate the size.

