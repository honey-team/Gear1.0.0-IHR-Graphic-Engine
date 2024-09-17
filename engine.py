from gear.utils.nodes import *
from gear.utils.graphic import *
from gear.process import render

class Loop:
    def __init__(
        self,
        tree: Tree,
        screen: Screen
    ):
        self.tree = tree
        self.screen = screen
        self.tree.loop = self
        self.stop = False

    def run(self):
        self.tree.on_ready()
        while True:
            render.clear()
            self.tree.process()
            self.tree.physic_process()
            screen_copy = self.screen.__copy__()
            for node in self.tree.get_all_nodes():
                node: Node = node
                if isinstance(node, Sprite2D):
                    if node.visible:
                        if node.follow_parent:
                            for y, row in enumerate(node.matrix.elements, 0):
                                for x, element in enumerate(row, 0):
                                    screen_copy.set(x + node.transform.x + node.parent.transform.x, y + node.transform.y + node.parent.transform.y, element)
                        else:
                            for row in node.matrix:
                                for element in row:
                                    element: Element = element
                                    screen_copy.set(x + node.transform.x, y + node.transform.y, element)
            render.render(screen_copy)
            render.sleep(self.screen.FPS)