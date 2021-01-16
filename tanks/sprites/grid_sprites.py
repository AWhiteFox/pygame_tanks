from ..grid import cell_to_screen
from ..images import load_image
from . import SpriteBase


class GridSpriteBase(SpriteBase):
    char = None
    destroyable = False
    tank_obstacle = True
    shell_obstacle = True
    layer = 0

    def __init__(self, grid_x, grid_y, *groups):
        super().__init__(*cell_to_screen(grid_x, grid_y), *groups)


class ConcreteWall(GridSpriteBase):
    sheet = load_image('concrete.png')
    char = '#'


class BrickWall(GridSpriteBase):
    sheet = load_image('brick.png')
    char = '%'
    destroyable = True


class Bush(GridSpriteBase):
    sheet = load_image('bush.png')
    char = '*'
    tank_obstacle = False
    shell_obstacle = False
    layer = 1


class Water(GridSpriteBase):
    sheet = load_image('water.png')
    char = '~'
    shell_obstacle = False


class Spike(GridSpriteBase):
    sheet = load_image('spike.png')
    char = 'x'
    shell_obstacle = False