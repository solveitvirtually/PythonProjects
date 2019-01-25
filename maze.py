class Maze:
    def __init__(self):
        '''Do Nothing'''
        self._rooms = {}

    def add_room(self, room):
        # use roomNumber as lookup value to retrieve room object
        self._rooms[room._room_number] = room

    def room_no(self, room_number):
        try:

            return self._rooms[room_number]
        except KeyError:
            print('No room: ', room_number)
