from stack import Stack

def RunTests():
    s = Stack()
    
    # Test 1
    print("Test 1, expected:  got: " + s.ShowData())
    if not s.ShowData() == "":
        return False

    # Test 2
    s.Push(123)
    s.Push(456)
    s.Push(7)
    print("Test 2, expected: 123, 456, 7 got: " + s.ShowData())
    if not s.ShowData() == "123, 456, 7":
        return False

    # Test 3
    e = s.Pop()
    print("Test 3, expected: 123, 456 got: " + s.ShowData())
    if not s.ShowData() == "123, 456":
        return False

    # Test 4
    print("Test 4, expected: 7 got: " + str(e))
    if not e==7:
        return False

    # Test 5
    s.Pop()
    s.Pop()
    e = s.Pop()
    print("Test 5, expected: -1 got: " + str(e))
    if not e == -1:
        return False

    return True

if not RunTests():
    print("See messages for error, please correct.")
else:
    print("Congrats, all tests passed.")