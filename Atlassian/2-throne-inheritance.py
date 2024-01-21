from typing import List

# Initialize a king class with name, alive status and children
# Keep track of the family in a tree structure
# Use a hash map to keep store all the created objects
# Birth: add the child to the parent's children list and add the child to the hash map
# Death: set the alive status to False
# Inheritance: preorder traversal of the tree

class King:
    def __init__(self, kingName: str):
        self.name = kingName
        self.alive = True
        self.children = []

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = King(kingName)        
        self.hash = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        t = King(childName)
        self.hash[parentName].children.append(t)
        self.hash[childName] = t

    def death(self, name: str) -> None:
        self.hash[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def preorder(node):
            if node.alive:
                res.append(node.name)
            for child in node.children:
                preorder(child)
        preorder(self.root)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()