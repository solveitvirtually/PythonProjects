from map_site import MapSite


class Wall(MapSite):
    def __init__(self):
        '''Do Nothing'''

    def enter(self):
        print("You just ran in to a wall...")
