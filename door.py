from map_site import MapSite


class Door(MapSite):
    def __init__(self, room1=None, room2=None):
        '''Do Nothing'''
        self._room1 = room1
        self._room2 = room2
        self._is_open = False

    def enter(self):
        message = '    ** Door must be opened before ' \
                  'you can pass through it...'
        if self._is_open:
            message = '    **** You have passed through this door...'
        print(message)

    def other_side_from(self, room):
        room_number = room.get_room_number()
        message = '\tDoor obj: This door is a side of Room: {}'\
            .format(room_number)
        print(message)
        if 1 == room_number:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room

    def open_door(self):
        self._is_open = True

    def is_open(self):
        return self._is_open
