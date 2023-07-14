The Checkbox
------------------

The checkbox is a togglable button.

Creation
***********


.. code-block:: py

    from TermUI.checkbox import Checkbox
    from TermUI.position import Position

    def on_checkbox(checkbox):
        # do something.
        ...

    checkbox = Checkbox(False, Position(0,0), callback=on_checkbox)


Properties
**************

Some properties are properties of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~~

``checked: bool`` - Whether the checkbox is checked or not.

``colors: list`` - A length 2 list of color_pair integers. [Off, On]. See :doc:`colors`

``spacing: bool`` - Whether there should be spacing around the check. Default is False.

``color: int`` - The current color_pair int displayed by the checkbox.



Methods
***********

Some methods are methods of :doc:`element` which apply to all elements and will not be repeated here.

Instance
~~~~~~~~~~~

``spaced(spacing: bool)`` - Changes the spacing property of the checkbox and recalculates the size.

