class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)

  def move(self, direction):
    if direction == "up":
      self.y -= 1
    elif direction == "down":
      self.y += 1
    elif direction == "left":
      self.x -= 1
    elif direction == "right":
      self.x += 1

class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name
    self.hp = 10
    self.damage = damage

  def info(self):
    print("Ciao sono", self.name, "hp:", self.hp, "/10", "sulla matrice mi trovo a", self.x, ",", self.y)

  def attack(self, enemy):
    if self.hp <= 0:
      print(self.name, "Il mostro non può attaccare da morto.")
    else: 
      print(self.name, "attacca", enemy.name)

      if (enemy.hp <= 0):
        print(enemy.name, "E' morto")
      else:
        enemy.hp -= self.damage

class Field:
  def __init__(self, x, y):
    self.w = 5
    self.h = 5
    self.entities = []

  def draw(self):
    print()
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[|]", end = "")
            break    
        else:
          print("[ ]", end = "")

        if e.x >= self.w:
          e.x = self.w - 1
        elif e.x < 0:
          e.x = 0
        if e.y >= self.h:
          e.y = self.h - 1
        elif e.y < 0:
          e.y = 0

      print()

field = Field(5,5)
m = Monster(10, 10, "Pino", 10, field)
m1 = Monster(2, 2, "Gino", 10, field)
m.info()
m1.info()
field.draw()
