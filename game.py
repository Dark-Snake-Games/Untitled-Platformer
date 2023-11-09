from DSEngine import *
class Player(AnimatedSprite2D):
    def __init__(self, position=...):
        sheet = AnimationSheet(default=Image2D("Test.png"))
        super().__init__(sheet, 1, position)
    
    def render(self, window: Window):
        super().render(window)


def main():
  window = Window(title="Test", fps=120, size=(1280, 720), bg=(100, 100, 100))
  audio_man = AudioManager()
  text = Text2D("Test", position=Vector2(550, 0))
  floor = Rect2D(1, Vector2(0, 660), (255, 0, 0), Vector2(1280, 720))
  text.init(window)
  rect = Rect2D(1, position=Vector2(100, 150), size=Vector2(50, 80))
  floor.init(window)
  rect.init(window)
  while window.running:
      keys = window.frame()
      vel = Vector2(0, 0)
      if keys[key_to_scancode(" ")] and rect.is_on_floor():
         vel.y = -35
      vel.x = (keys[key_to_scancode("d")]-keys[key_to_scancode("a")])*2
      print(vel)
      rect.move(vel)
      if not rect.is_on_floor():
         rect.move(vec=Vector2(0, 1))
         #rect.move(vec=Vector2(0, 1))
      if keys[27]:
          return 1

if __name__ == "__main__":
  main()
