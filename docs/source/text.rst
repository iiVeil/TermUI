The Text Object
----------------

The text object is how you put text on the screen.



Creation
**********


.. code-block:: py

    from pyTermUI.text import Text
    from pyTermUI.position import Position

    text = Text("I love TermUI!", Position(0,0))


Properties
***************

Some properties are properties of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~~

``text: str`` - The text that is displayed in this element.

``underlined: bool`` - Whether the text should be underlined.



Methods
***********

Some methods are methods of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~
``set_text(text: str) -> None`` - Set the text displayed by the element.

