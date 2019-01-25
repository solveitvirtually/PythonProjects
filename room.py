from map_site import MapSite


class Room(MapSite):
    def __init__(self, room_number):
        self._room_number = int(room_number)
        self._sides = [MapSite] * 4

    def enter(self):
        print("You have entered room:  " + str(self._room_number))

    def set_side(self, direction, map_site):
        self._sides[direction] = map_site

    def get_side(self, direction):
        return self._sides[direction]

    def get_room_number(self):
        return self._room_number
