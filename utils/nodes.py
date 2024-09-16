from __future__ import annotations
from abc import abstractmethod
from utils.vectors import *
from utils.graphic import *

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

    @abstractmethod
    def on_ready(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def physic_process(self):
        pass

class Node:
    def __init__(self, identifier: Identifier[str], scripts: list[Script] = [], nodes: list[Node] = []):
        self.identifier = Identifier(identifier)
        self.scripts = scripts
        self.nodes = nodes
        self.parent: Node | None = None

        self.set_parents() # Set Node.parent for every node in self.nodes
        self.set_scripts_nodes_and_trees() # Set Script.node and Script.tree for every script in self.scripts
    
    def set_parents(self):
        """Set Node.parent for every node in self.nodes"""
        for node in self.nodes:
            node.parent = self
    
    def set_scripts_nodes_and_trees(self):
        """Set Script.node and Script.tree for every script in self.scripts"""
        for script in self.scripts:
            script.node, script.tree = self, self.get_tree()

    def get_tree(self) -> Tree:
        """Get the highest point in nodes tree"""
        if self.parent is None:
            return self
        else:
            return self.parent.get_tree()
        
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
        self.nodes.append(node)
        return self.nodes

    def on_ready(self):
        """`on_ready` function invokes `on_ready` function in every node's script"""
        for script in self.scripts:
            script: Script = script
            script.on_ready()
        for node in self.nodes:
            node: Node = node
            node.on_ready()
    
    def process(self):
        """`process` function invokes `process` function in every node's script"""
        for script in self.scripts:
            script: Script = script
            script.process()
        for node in self.nodes:
            node: Node = node
            node.process()
    
    def physic_process(self):
        """`physic_process` function invokes `physic_process` function in every node's script"""
        for script in self.scripts:
            script: Script = script
            script.physic_process()
        for node in self.nodes:
            node: Node = node
            node.physic_process()

    def __repr__(self) -> str:
        return f"Node({self.identifier})"

class Tree(Node):
    def __init__(self, scripts: tuple[Script] = (), nodes: list[Node] = []):
        super().__init__("tree", scripts, nodes)
        self.parent = False

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