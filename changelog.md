# Version 1.2

Beginning of Toolkits, Hover support, more efficient cursor management, more textbox issues fixed.

- Toolkits are extra (processing expensive) features that increase the possibilities of TermUI
- Hover support using TermUI.Toolkit.hover.Hover()
- Ascii Art helper using TermUI.Toolkit.ascii.AsciiArt()
- Toolkit documentation will be added as its own section in the TermUI documentation
- The viewing cursor is now seperated from the drawing cursor which fixes many flickering issues and makes textboxes a more fluid experience.

## 1.2.3
- Background Task Toolkit implementation
- Standarized toolkit cleanup with `UI.add_toolkits()`
- Full support for KeyboardInterrupts
- Easier centering for elements inside of a region using `Element.centerX()`, `Element.centerY()`, and `Element.centerXY()`



# Version 1.1

Many speed improvements, bug fixes, and added checkbox functionality.

The big stuff first:
- No more errors when the terminal isn't big enough to run the program, TermUI will dynamically skip over-drawing and allow the user to change the size of the terminal while the program is running updating the program in real-time. Ideally until it is all in view.
- A HUGE frame-skipping issues was fixed, this wasn't entirely visible in most programs but caused large deviations and problems when you started to implement threading for background processes.
- Checkbox support! (with functionality to allow other elements callbacks to act as the checkbox aka Label support!)

Smaller stuff:
- A large lag spike when switching between multiple focused textboxes was fixed.
- Solved a draw-line issue on weaker hardware.
- Move and resize functionality for all regions and elements.
- Move or resizing an object will recalculate the relative packing dictionary assuming you use the methods provided.
- Better explanations of properties and more informative doc-strings.
- Documentation on the way.
- Moved around a lot of the functions into the `Element` parent class for parity.

In general, lots of changes, with no required code change for current apps. (maybe a few spacing changes as packing was homogenized for all objects.)
