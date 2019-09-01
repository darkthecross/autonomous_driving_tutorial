class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """
        param node_list: a list of nodes in the format: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    def GetMaxDepth(self):
        # TODO: Implement the method
        return 0

    def FindElement(self, node_id):
        # TODO: Implement the method
        return False

    def FindPath(self, node_id):
        # TODO: Implement the method
        return str([]).strip('[]')

    def ShowData(self):
        return self.PreorderTrav(self.root)

    def PreorderTrav(self, treenode):
        if treenode is not None:
            return treenode.data + ", " + self.PreorderTrav(treenode.left) + self.PreorderTrav(treenode.right)
        else: 
            return ""