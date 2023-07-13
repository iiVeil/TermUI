# TermUI

TermUI is a rapid development user interface library for python command-line applications.

If you would like a reference for the library D-Word is built on it. You can find it here: https://github.com/iiVeil/D-Word-Password-Manager

To view a list of avaiable color_pair colors, inside the src folder of the library, you can run `colors.py` this file isnt used anywhere else in the library and is purely to view the color pallete


# Version 1.1

Many speed improvements, bug fixes, and added checkbox functionality.

The big stuff first:
- No more errors when the terminal isn't big enough to run the program, TermUI will dynamically skip over-drawing and allow the user to change the size of the terminal while the program is running updating the program in real-time. Ideally until it is all in view.
- A HUGE frame-skipping issues was fixed, this wasn't entirely visible in most programs but caused large deviations and problems when you started to implement threading for background processes.
- Checkbox support! (with functionality to allow other elements callbacks to act as the checkbox aka Label support!)

Smaller stuff:
- A large lag spike when switching between multiple focused textboxes was fixed.
- Move and resize functionality for all regions and elements.
- Move or resizing an object will recalculate the relative packing dictionary assuming you use the methods provided.
- Better explanations of properties and more informative doc-strings.
- Documentation on the way.
- Moved around a lot of the functions into the `Element` parent class for parity.


In general, lots of changes, with no required code change for current apps. (maybe a few spacing changes as packing was homogenized for all objects.)
