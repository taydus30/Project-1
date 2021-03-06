from sprite import Sprite
import main
import random


def spawnInWorld():
    for x in range(main.world.width):
        for y in range(main.world.height):
            # bush generation
            if main.world.terrainAt(x, y) == "grass":
                if random.randrange(0, 30) == 0:
                    bb = Berry_Bush()
                    bb.x = x * 8
                    bb.y = y * 8
                    main.world.spawnObjectAt(bb, x, y)


class Berry_Bush(Sprite):

    type: str = "plant"
    id:   str = "berry bush"
    x:    int = 0
    y:    int = 0

    def __init__(self):
        super().__init__('berries.png')
        self.alive = True
        self.death_tolerance = random.randrange(0, 5)

    def update(self):
        # if this is somehow in water, it should not be alive
        if self.terrAt() == "water":
            self.alive = False
        super().update()
        if self.alive is False:
            return
        # if it is on the beach we want to know
        on_beach = False
        if self.terrAt() == "beach":
            on_beach = True
            self.age += 1

        # dies quicker in the snow
        if(self.terrAt() == "snow"):
            self.age += 1

        if(self.years()) > 3:
            if random.randrange(0, 100) == 0:

                xx = random.randrange(-3, 3) + self.world_x()
                yy = random.randrange(-3, 3) + self.world_y()
                if(xx != 0 and yy != 0) and not on_beach:
                    main.world.spawnObjectAt(Berry_Bush(), xx, yy)

        if self.years() > 8 + self.death_tolerance:
            self.alive = False
