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
  floor.init(window)
  while window.running:
      keys = window.frame()
      if keys[27]:
          return 1

if __name__ == "__main__":
  main()
