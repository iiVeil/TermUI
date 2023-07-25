TaskHandler
-------------

TaskHandler is simple support for background processes in your TermUI apps using threading.

Using the TaskHandler
*******************

Lets make a timer that can be toggled by a checkbox. (with some active centering)

.. code-block:: py

    import time
    import curses
    from pyTermUI.ui import UI
    from pyTermUI.text import Text
    from pyTermUI.region import Region
    from pyTermUI.checkbox import Checkbox
    from pyTermUI.position import Position
    from pyTermUI.Toolkit.taskhandler import TaskHandler

    def main(stdscr):
        ui = UI(stdscr)
        
        count = 0
        def background():
            nonlocal count
            count += 1
            
            text.set_text(f"LIVE COUNTER: {count}")
            text.centerXY()
            checkbox.move(text.pack.get("left")-Position(3,0)) 
            
            ui.draw()
            time.sleep(.125)
                
        def on_checkbox(checkbox):
            text.color = checkbox.color
            if checkbox.checked:
                handler.run("counter")
            else:
                handler.kill("counter")
            
            
        region = Region("A cool region", Position.ORIGIN(), Position.DEFAULT_TERM_SIZE())
        
        
        handler = TaskHandler()
        # init task handler
        
        checkbox = Checkbox(False, Position(0,0), on_checkbox)
        
        text = Text(f"LIVE COUNTER: {count}", Position(0,0))
        
        text.callback = checkbox.event_mask
        
        handler.create("counter", background, args=(), iterations=0)
        # create an infinite loop background task
        
        region.add_element(checkbox)
        region.add_element(text)
        
        text.centerXY()
        checkbox.move(text.pack.get("left")-Position(3,0))    
        
        ui.add_toolkits(handler)
        ui.add_region(region)
        
        ui.activate()
        
    if __name__ == "__main__":
        curses.wrapper(main)
