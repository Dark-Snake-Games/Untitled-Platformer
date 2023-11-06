from DSEngine import Window, AudioManager, Text2D, Vector2

def main():
  window = Window(title="Test", fps=120, size=(1280, 720), bg=(100, 100, 100))
  audio_man = AudioManager()
  text = Text2D("Test", position=Vector2(550, 0))
  text.init(window)
  while window.running:
      keys = window.frame()
      if keys[27]:
          return 1

if __name__ == "__main__":
  main()
