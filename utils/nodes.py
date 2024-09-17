from __future__ import annotations
from gear.utils.vectors import *
from gear.utils.graphic import *

class Identifier(str): pass
class XCoords(int): pass
class YCoords(int): pass
class Transform(Vector2D): pass
class IdenfitierPath(str): pass
class NodeError(Exception): pass
class NodeNotFound(NodeError): pass

class Script:
    def __init__(self):
        self.parent: Node | None = None
        self.tree: Tree | None = None
        self.node: Node | None = None

    def on_ready(self):
        pass

    def process(self):
        pass

    def physic_process(self):
        pass

class Node:
    def __init__(self, identifier: Identifier[str], scripts: list[Script] = [], nodes: list[Node] = []):
        self.identifier = Identifier(identifier)
        self.scripts = scripts
        self.nodes = nodes
        self.tree: Tree | None = None
        self.parent: Node | None = None

    def init_nodes_scripts(self):
        for script_index in range(len(self.scripts)):
            self.scripts[script_index].tree = self.tree
            self.scripts[script_index].node = self

        for node_index in range(len(self.nodes)):
            self.nodes[node_index].tree = self.tree
            self.nodes[node_index].parent = self
            self.nodes[node_index].init_nodes_scripts()
        
    def get_node(self, __identifier: Identifier[str] | list[str]) -> Node:
        """Gets node by a path or an idenfitier (__idenfitier could be path like "test1/test2")."""
        if isinstance(__identifier, list):
            identifiers = __identifier
        elif isinstance(__identifier, str):
            identifiers = __identifier.split("/")
        for node in self.nodes:
            if node.identifier == identifiers[0]:
                if len(identifiers) == 1:
                    return node
                else:
                    return node.get_node(identifiers[1:])
    
    def get_all_nodes(self) -> list[Node]:
        """Gets all nodes from tree."""
        self.__n = []
        self.__get_all_nodes()
        return self.__n
        
    def __get_all_nodes(self) -> list[Node]:
        """Uses for `get_all_nodes` function."""
        for node in self.nodes:
            self.__n.append(node)
            self.__n.extend(node.get_all_nodes())

    def del_node(self, __identifier: Identifier[str]):
        """Deletes node by a path or an idenfitier (__idenfitier could be path like "test1/test2")."""
        if isinstance(__identifier, list): 
            identifiers = __identifier
            if not identifiers:
                raise NodeNotFound()
        elif isinstance(__identifier, str):
            identifiers = __identifier.split("/")
        for index, node in enumerate(self.nodes, 0):
            if node.identifier == identifiers[0]:
                if len(identifiers) == 1:
                    del self.nodes[index]
                else:
                    return node.del_node(identifiers[1:])
    
    def add_child(self, node: Node) -> list[Node]:
        """Appends node to current node."""
        node.parent = self
        node.tree = self.tree
        node.init_nodes_scripts()
        self.nodes.append(node)
        node.on_ready()
        return self.nodes

    def on_ready(self):
        """`on_ready` function invokes `on_ready` function in every node's script"""
        for script in self.scripts:
            script.on_ready()
        for node in self.nodes:
            node.on_ready()
    
    def process(self):
        """`process` function invokes `process` function in every node's script"""
        for script in self.scripts:
            script.process()
        for node in self.nodes:
            node.process()
    
    def physic_process(self):
        """`physic_process` function invokes `physic_process` function in every node's script"""
        for script in self.scripts:
            script.physic_process()
        for node in self.nodes:
            node.physic_process()

    def __repr__(self) -> str:
        return f"Node({self.identifier})"

class Tree(Node):
    def __init__(self, scripts: tuple[Script] = (), nodes: list[Node] = []):
        self.parent = None
        self.loop = None
        super().__init__("tree", scripts, nodes)
        self.init_nodes_scripts()
    
    def init_nodes_scripts(self):
        for script_index in range(len(self.scripts)):
            self.scripts[script_index].tree = self
            self.scripts[script_index].node = self

        for node_index in range(len(self.nodes)):
            self.nodes[node_index].tree = self
            self.nodes[node_index].parent = self
            self.nodes[node_index].init_nodes_scripts()
    
    def add_child(self, node: Node) -> list[Node]:
        """Appends node to current node."""
        node.parent = self
        node.tree = self
        node.init_nodes_scripts()
        self.nodes.append(node)
        node.on_ready()
        return self.nodes

    def __repr__(self) -> str:
        return f"Tree()"

class Node2D(Node):
    def __init__(self, identifier: Identifier[str], x: XCoords[int] = XCoords(), y: YCoords[int] = YCoords(), follow: bool = True, scripts: tuple[Script] = (), nodes: list[Script] = []):
        super().__init__(identifier, scripts, nodes)
        self.transform = Transform(x, y)
        self.follow_parent = follow
    
    def translate(self, x: XCoords = XCoords(), y: YCoords = YCoords()) -> Vector2D[XCoords, YCoords]:
        self.transform = self.transform + Vector2D(x, y)
        for node in self.nodes:
            if isinstance(node, Node2D):
                if node.follow_parent:
                    node.translate(x, y)
    
    def __repr__(self) -> str:
        return f"Node2D({self.identifier})"

class Sprite2D(Node2D):
    def __init__(
        self,
        identifier: Identifier,
        x: XCoords = XCoords(),
        y: YCoords = YCoords(),
        visible: bool = True,
        follow: bool = True,
        scripts: tuple[Script] = (),
        nodes: list[Script] = [],
        matrix: Matrix = Matrix([[]])
    ):
        super().__init__(identifier, x, y, follow, scripts, nodes)
        self.matrix = matrix
        self.visible = visible

    def __repr__(self) -> str:
        return f"Sprite2D({self.identifier})"