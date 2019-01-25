from maze import Maze
from room import Room
from door import Door
from wall import Wall
from direction import Direction


class MazeGame:
    def create_maze(self):
        aMaze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        theDoor = Door(r1, r2)

        aMaze.add_room(r1)
        aMaze.add_room(r2)

        r1.set_side(Direction.North.value, Wall())
        r1.set_side(Direction.East.value, theDoor)
        r1.set_side(Direction.South.value, Wall())
        r1.set_side(Direction.West.value, Wall())

        r2.set_side(Direction(0).value, Wall())
        r2.set_side(Direction(1).value, Wall())
        r2.set_side(Direction(2).value, Wall())
        r2.set_side(Direction(3).value, theDoor)

        return aMaze
