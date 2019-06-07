from sprite import Sprite
import main
import random


def spawnInWorld():
    for x in range(main.world.width):
        for y in range(main.world.height):
            # chicken generation
            if main.world.terrainAt(x, y) == "grass":
                if random.randrange(0, 100) == 0:
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
        self.hunger = 300

    def update(self):
        # if this is in water, it should not be alive
        if self.terrAt() == "water":
            self.alive = False
        super().update()
        if self.alive is False:
            return

        self.hunger -= 1 * main.simulation_speed

        speed = 5 * main.simulation_speed
        if (self.terrAt() == "snow"):
            speed = 3 * main.simulation_speed
        target_x = random.randrange(-speed, speed + 1)
        target_y = random.randrange(-speed, speed + 1)

        if self.hunger < 600:
            # find food
            objs = self.objectsOfIdInRange("berry bush", 3)
            if objs != []:
                d = 9999
                oo = None
                for obj in objs:
                    if self.distance(obj) < d:
                        d = self.distance(obj)
                        oo = obj
                    if self.distance(obj) < 16:
                        self.hunger += 201 * main.simulation_speed
                        obj.alive = False
                if oo.x > self.x:
                    target_x = speed + 1
                elif oo.x < self.x:
                    target_x = -speed - 1
                if oo.y > self.y:
                    target_y = speed + 1
                elif oo.y < self.y:
                    target_y = -speed - 1

        self.move(target_x, target_y)

        if(self.years()) > 3 and self.hunger > 300:
            if random.randrange(0, 150 * main.simulation_speed) == 0:
                xx = random.randrange(-3, 3) + self.world_x()
                yy = random.randrange(-3, 3) + self.world_y()
                if(xx != 0 and yy != 0):
                    main.world.spawnObjectAt(Chicken(), xx, yy)

        if self.years() > 6 + self.death_tolerance:
            self.alive = False

        if self.hunger == 0:
            self.alive = False
