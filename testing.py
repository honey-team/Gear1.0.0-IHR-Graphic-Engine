import engine

class MyGame(engine.GameLoop):
    def __init__(self, FPS: int, screen_width: int, screen_height: int) -> None:
        super().__init__(FPS, screen_width, screen_height)
    
    def process(self):
        engine.render.clear()
        if engine.input.keys["right"]:
            self.screen.set(0, 0, engine.colors.RGB(255, 255, 255))
        engine.render.render(self.screen)
        engine.render.sleep(self.FPS)
        self.process()

def main():
    game = MyGame(1, 20, 20)
    game.process()

if __name__ == "__main__":
    main()