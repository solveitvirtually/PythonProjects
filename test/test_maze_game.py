import unittest
from maze_game import MazeGame
from direction import Direction
from wall import Wall
from door import Door


class TestMazeGame(unittest.TestCase):
    def setUp(self):
        self._mg = MazeGame()

    def test_create_maze(self):
        maze = self._mg.create_maze()
        self.assertIsNotNone(maze.room_no(1))
        self.assertIsNotNone(maze.room_no(2))
        self.assertIsNone(maze.room_no(0))

        r1 = maze.room_no(1)
        self.assertIsInstance(r1.get_side(Direction.North.value), Wall)
        self.assertIsInstance(r1.get_side(Direction.South.value), Wall)
        self.assertIsInstance(r1.get_side(Direction.West.value), Wall)
        self.assertIsInstance(r1.get_side(Direction.East.value), Door)

        r2 = maze.room_no(2)
        self.assertIsInstance(r2.get_side(Direction.North.value), Wall)
        self.assertIsInstance(r2.get_side(Direction.South.value), Wall)
        self.assertIsInstance(r2.get_side(Direction.West.value), Door)
        self.assertIsInstance(r2.get_side(Direction.East.value), Wall)

        r1.enter()

        for idx in range(4):
            side = r1.get_side(idx)
            side_str = str(side.__class__)\
                .replace("<class '__main__.", "")\
                .replace("'>", "")
            print('    Room: {}, {:<15s}, Type: {}'
                  .format(r1._room_number, Direction(idx), side_str))
            print('    Trying to enter: ', Direction(idx))
            side.enter()
            if 'Door' in side_str:
                door = side
                self.assertFalse(door.is_open())
                door.open_door()
                self.assertTrue(door.is_open())
