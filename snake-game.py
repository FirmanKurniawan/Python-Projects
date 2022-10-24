import pygame
import sys
import random

class snake(object):
  def __init__(self):
    self.length = 1
    self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
    self.color = (17, 24, 47)

  def get_head_position(self):
    return self.positions[0]

  def turn(self, point):
    if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
      return
    else: 
      self.direction = point

  def move(self):
    curr = self.get_head_position()
    x, y = self.direction
    new = (((curr[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (curr[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
    if len(self.positions) > 2 and new in self.positions[2:]:
      self.reset()
    else:
      self.positions.insert(0, new)
      if len(self.positions) > self.length:
        self.positions.pop()

  def reset(self):
    self.length = 1
    self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
    self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

  def draw(self, surface):
    for p in self.positions:
      rect = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
      pygame.draw.rect(surface, self.color, rect)
      pygame.draw.rect(surface, (93, 216, 228), rect, 1)

  def handle_keys(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          self.turn(UP)
        elif event.key == pygame.K_DOWN:
          self.turn(DOWN)
        elif event.key == pygame.K_LEFT:
          self.turn(LEFT)
        elif event.key == pygame.K_RIGHT:
          self.turn(RIGHT)


class food(object):
  def __init__(self):
    self.position = (0, 0)
    self.color = (223, 163, 49)
    self.randomize_position()

  def randomize_position(self):
    self.position = (
      random.randint(0, GRID_WIDTH-1) * GRIDSIZE, 
      random.randint(0, GRID_HEIGHT-1) * GRIDSIZE
    )
  
  def draw(self, surface):
    rect = pygame.Rect(
      (self.position[0], self.position[1]), 
      (GRIDSIZE, GRIDSIZE)
    )
    pygame.draw.rect(surface, self.color, rect)
    pygame.draw.rect(surface, (93, 216, 228), rect, 1)


def drawGrid(surface):
  for y in range(0, int(GRID_HEIGHT)):
    for x in range(0, int(GRID_WIDTH)):
      if(x + y) % 2 == 0:
        rect = pygame.Rect(
          (x*GRIDSIZE, y*GRIDSIZE), 
          (GRIDSIZE, GRIDSIZE)
        )
        pygame.draw.rect(surface, (93, 216, 228), rect)
      else:
        rrect = pygame.Rect(
          (x*GRIDSIZE, y*GRIDSIZE), 
          (GRIDSIZE, GRIDSIZE)
        )
        pygame.draw.rect(surface, (84, 194, 205), rrect)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
  pygame.init()
  python_snake = snake()
  snake_food = food()

  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

  surface = pygame.Surface(screen.get_size())
  surface = surface.convert()
  drawGrid(surface)

  myfont = pygame.font.SysFont("monospace", 16)

  score = 0
  while(True):
    clock.tick(10)
    python_snake.handle_keys()
    drawGrid(surface)
    python_snake.move()

    if python_snake.get_head_position() == snake_food.position:
      python_snake.length += 1
      score += 1
      snake_food.randomize_position()

    python_snake.draw(surface)
    snake_food.draw(surface)

    screen.blit(surface, (0,0))
    text = myfont.render(f"Score {score}", 1, (0,0,0))
    screen.blit(surface, (5,10))

    pygame.display.update()

main()
