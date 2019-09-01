from bin_tree import BinTree, BinTreeNode

node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


def RunTests():
    btree = BinTree.build_from(node_list)
    
    # Test 1
    print("Test 1, expected: A, B, D, E, H, C, F, G, I, J,  got: " + btree.ShowData())
    if not btree.ShowData() == "A, B, D, E, H, C, F, G, I, J, ":
        return False

    # Test 2, no element
    print("Test 2, expected: False got: " + str(btree.FindElement('K')))
    if not btree.FindElement('K') == False:
        return False

    # Test 3, get path for non-element
    print("Test 3, expected: '' got: " + btree.FindPath('K'))
    if not btree.FindElement('K') == "":
        return False

    # Test 4, found element
    print("Test 4, expected: True got: " + str(btree.FindElement('I')))
    if not btree.FindElement('I') == True:
        return False

    # Test 5, found element
    print("Test 5, expected: 'A, C, G, I, ' got: " + str(btree.FindElement('I')))
    if not btree.FindElement('I') == "A, C, G, I, ":
        return False

    return True

if not RunTests():
    print("See messages for error, please correct.")
else:
    print("Congrats, all tests passed.")