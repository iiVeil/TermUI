.. TermUI documentation master file, created by
   sphinx-quickstart on Wed Jul 12 22:29:56 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Introduction to TermUI
------------------------

pyTermUI or just TermUI is a rapid development terminal user interface library for python command-line interface applications.

TermUI is meant to be barebones by design, giving the developer control of everything outside of the drawing and interaction of the elements themselves.

If you are on windows, TermUI requires ``windows-curses``

``pip install windows-curses``

Features
---------------------
* User element support:
    * Buttons
    * Checkboxes
    * User input boxes (textboxes)
    * Interactable Text
* Color support
* Runs on any modern terminal
* Multi UI support



Getting started with TermUI
-----------------------------

.. toctree::
   :maxdepth: 2
   :caption: Quickstart:

   basics.rst
   createanapp.rst

.. toctree::
   :maxdepth: 2
   :caption: UI:

   ui.rst
   region.rst
   position.rst
   colors.rst
   packing.rst


.. toctree::
   :maxdepth: 1
   :caption: Elements:

   element.rst
   text.rst
   button.rst
   checkbox.rst
   textbox.rst