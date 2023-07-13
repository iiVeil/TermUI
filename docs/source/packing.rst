Packing
-------------

Packing is a useful feature that allows you to place regions and elements directly beside each other without having to handle their coordinates seperately.



Using an objects pack dictionary
**********************************

.. code-block:: py
    checkbox = Checkbox(checked=False, position=Position(
        region.size.half().x-3, region.size.half().y))
    # Center the checkbox inside of the region.
    
    checkbox.callback = on_checkbox
    # Point the checkboxes callback at the on_checkbox method.


    label = Text(content="A label", position=checkbox.pack.get("right"))
    # Notice how am I not specifying coordinates here, the pack dictionary has them for me
    # since I have already placed my checkbox.

This is a snippet of code from our :doc:`createanapp` document.

Lets explore whats really happening here.

``checkbox = Checkbox(checked=False, position=Position(region.size.half().x-3, region.size.half().y))``

When we create our checkbox, we are placing it at the center of the region it is contained in.

Once we place the checkbox its starting and ending position are calculated and from that we can create coordinates on the edge easily.

These "created" coordinates are stored in the ``pack`` dictionary:
    * The output from the checkboxes pack dictionary should be used as coordinates to another element in the same region, to place it beside it.
    * ``pack.get("up")`` - The coordinate directly above the top left corner.
        * To pack an object above another object, its position will need to be subtracted by its height ``Position(0, size.y)`` to fit it properly.
    * ``pack.get("right")`` - The coordinate directly to the right of the top right corner.
    * ``pack.get("down")`` - The coordinate directly below the bottom left corner.
    * ``pack.get("left")`` - The coordinate directly to the left of the top left corner.
        * To pack an object to the left another object, its position will need to be subtracted by its width ``Position(size.x, 0)`` to fit it properly.

Lets see it in action.

``label = Text(content="A label", position=checkbox.pack.get("right"))``

You can see in the ``position`` argument, we are using the pack dictionary to retrieve those coordinates.

When packing below or to the right, no changes will need to be made based on size like we do when pack above and to the left.