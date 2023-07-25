The Basic Element
--------------------

The element is what adds functionality to your app. These are the objects people interact with.


Creation
************

The element object themselves arent created, you can create a specified element.

    * :doc:`text`
    * :doc:`button`
    * :doc:`checkbox`
    * :doc:`textbox`

Properties
*************

These are global properties shared by all elements.

Instance
~~~~~~~~~~~~

``region: Region`` - The region the element is stored in assuming it was added to the region using ``Region().add_element()``.

``start: Position`` - The top left corner of the element.

``hidden: bool`` - Whether the element should be drawn.

``size: Position`` - The length and height of the object.

``end: Position`` - The bottom right corner of the object.

``color: int`` - The ``color_pair`` int of this element. See: :doc:`colors`

``data: dict`` - A extra storage dictionary for other data you might want to store with your object.


Methods
************

These are global methods shared by all elements.

Instance
~~~~~~~~~~

``in_bounds(position: Position) -> bool`` - Returns a boolean based on if the element occupies the position.

``addstr(y: int, x: int, string: str, options=0) -> None`` -  A curses shorthand for ``stdscr.addstr()`` with added functionality to remove overdrawing.

``move(position: Position) -> None`` - Move a object within its region and recalculate its pack dictionary.

``resize(position: Position) -> None`` - Resize an object and recalculate its pack dictionary.

``event_mask(*args) -> None`` - Used to emulate a click for this element. This is useful when used as a callback for other elements.

``centerX() -> None`` - Center an element on the horizontal axis after it has been placed inside of a region.

``centerY() -> None`` - Center an element on the vertical axis after it has been placed inside of a region.

``centerXY() -> None`` - Center an element on both axi after it has been placed inside of a region.


Adding a label
*****************

If you are having trouble adding a label to a checkbox :doc:`createanapp` shows how to properly add a label to a checkbox.