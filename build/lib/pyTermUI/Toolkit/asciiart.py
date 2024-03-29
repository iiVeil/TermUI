from ..text import Text
from ..position import Position
from ..region import Region
from math import floor


class AsciiArt:
    def __init__(self, lines: list | str, region: Region, center: Position):
        """

        Args:
            lines (list | str): A list of lines or a str with line breaks representing the ascii art.
            region (Region): The region it should be placed in.
            center (Position): Where the center position of the ascii art should be.
        """

        self.center = center
        "The center of the art"
        self.lines = lines if type(lines) == list else lines.split("\n")
        "A list of the lines representing the ascii art"
        self.elements = []
        "The text elements that make up the art"
        self.region = region

        self.startpos = Position()

        self.endpos = Position()

    def create(self):
        """Create and add the ascii art to the region."""
        for i, line in enumerate(self.lines):
            position = Position(
                self.center.x - floor(len(line) / 2),
                self.center.y - floor(len(self.lines) / 2) + i,
            )
            if i == 0:
                self.startpos = position
            if i == len(self.lines) - 1:
                self.endpos = position + Position(len(line), 0)
            element = Text(line, position)
            self.elements.append(element)
            self.region.add_element(element)

    def end(self):
        return
