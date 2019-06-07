from sprite import Sprite
import main
import random


def spawnInWorld():
    for x in range(main.world.width):
        for y in range(main.world.height):
            # chicken generation
            if main.world.terrainAt(x, y) == "grass":
                if random.randrange(0, 40) == 0:
                    ch = Chicken()
                    ch.x = x * 8
                    ch.y = y * 8
                    main.world.spawnObjectAt(ch, x, y)


class Chicken(Sprite):

    type: str = "Animal"
    id:   str = "chicken"
    x:    int = 0
    y:    int = 0

    def __init__(self):
        super().__init__('chicken.png')
        self.alive = True
        self.death_tolerance = random.randrange(0, 4)
        self.hunger = 10

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
            self.hunger = self.hunger - 1

        # dies quicker in the snow
        if(self.terrAt() == "snow"):
            self.age += 2
            self.hunger = self.hunger - 1

        if(self.years()) > 3:
            if random.randrange(0, 50) == 0:

                xx = random.randrange(-3, 3) + self.world_x()
                yy = random.randrange(-3, 3) + self.world_y()
                if(xx != 0 and yy != 0) and not on_beach:
                    main.world.spawnObjectAt(Chicken(), xx, yy)
                    print("generating new chicken at", xx, ", ", yy)

        if self.years() > 6 + self.death_tolerance:
            self.alive = False
            print("chicken died")

        if self.hunger == 0:
            self.alive = False
            print("chicken starved to death")
