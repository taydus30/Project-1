from sprite import Sprite
import main
import random


def spawnInWorld():
    for x in range(main.world.width):
        for y in range(main.world.height):
            # tree generation
            if main.world.terrainAt(x, y) == "grass":
                if random.randrange(0, 40) == 0:
                    tr = Tree()
                    tr.x = x * 8
                    tr.y = y * 8
                    main.world.spawnObjectAt(tr, x, y)


class Tree(Sprite):

    type: str = "plant"
    id:   str = "tree"
    x:    int = 0
    y:    int = 0

    def __init__(self):
        super().__init__('tree.png')
        self.alive = True
        self.death_tolerance = random.randrange(0, 50)

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
            self.age += 2

        if(self.years()) > 50:
            if random.randrange(0, 500) == 0:
                print("generating new tree")
                xx = random.randrange(-3, 3) + self.world_x()
                yy = random.randrange(-3, 3) + self.world_y()
                if(xx != 0 and yy != 0) and not on_beach and main.world.objectAt(self.world_x, self.world_y) is not None:
                    main.world.spawnObjectAt(Tree(), xx, yy)

        if self.years() > 60 + self.death_tolerance:
            self.alive = False
            print("tree died")
