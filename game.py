from DSEngine import *
class Player(AnimatedSprite2D):
    def __init__(self, position: Vector2):
        f1 = Image2D("assets/Slime_sprite1.png")
        f2 = Image2D("assets/Slime_sprite2.png")
        f3 = Image2D("assets/Slime_sprite3.png")
        f4 = Image2D("assets/Slime_sprite4.png")
        left = Spritesheet(0, f3, f3, f3, f3, f3, f3, f3, f3, f3, f3, \
                           f4, f4, f4, f4, f4, f4, f4, f4, f4, f4)
        right = Spritesheet(0, f1, f1, f1, f1, f1, f1, f1, f1, f1, f1, \
                           f2, f2, f2, f2, f2, f2, f2, f2, f2, f2)
        sheet = AnimationSheet(default=f1, left=left, right=right)
        self.jumps = 0
        super().__init__(sheet, 2, position)
    
    def render(self, window: Window):
        vel = Vector2(0, 0)
        if window.pressed_keys[key_to_scancode(" ")]:
            if self.is_on_floor() or self.jumps < 2:
              vel.y = -45
              self.jumps += 1
        vel.x = (window.pressed_keys[key_to_scancode("d")]-window.pressed_keys[key_to_scancode("a")])*2
        if vel.x < 0 and not self.playing and self.sheet_name != "left":
           self.play_sheet("left")
        else:
           if not self.playing and self.sheet_name != "right":
              self.play_sheet("right")
        # elif vel.x == 0:
        #    self.stop()
           
        if not self.is_on_floor():
          self.move(vec=Vector2(0, 1))
          self.move(vec=Vector2(0, 2))
        else:
           self.jumps = 0
        print(vel)
        self.move(vel)
        super().render(window)


def main():
  window = Window(title="Test", fps=120, size=(1280, 720), bg=(100, 100, 100))
  audio_man = AudioManager()
  bg = Image2D("assets/bg_resize.png")
  text = Text2D("Test", position=Vector2(550, 0))
  floor = Rect2D(2, Vector2(0, 660), (255, 0, 0), Vector2(1280, 720))
  player = Player(position=Vector2(100, 150))
  player.init(window)
  text.init(window)
  floor.init(window)
  bg.init(window)
  while window.running:
      keys = window.frame()
      if keys[27]:
          return 1

SURFACE=Surface(size=pygame.Vector2(1280, 720))

if __name__ == "__main__":
  main()

def tosurfaceinit():
  window = SURFACE
  resetwindow(window)
  audio_man = AudioManager()
  text = Text2D("Test", position=Vector2(550, 0))
  floor = Rect2D(1, Vector2(0, 660), (255, 0, 0), Vector2(1280, 720))
  player = Player(position=Vector2(100, 150))
  player.init(window)
  text.init(window)
  floor.init(window)

def tosurface():
  SURFACE.frame()
  keys = SURFACE.frame()
  if keys[key_to_scancode("q")]:
    return 1