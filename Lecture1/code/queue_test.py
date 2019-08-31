from queue import Queue

def RunTests():
    q = Queue()
    
    # Test 1
    print("Test 1, expected:  got: " + q.ShowData())
    if not q.ShowData() == "":
        return False

    # Test 2
    q.Enqueue(123)
    q.Enqueue(456)
    q.Enqueue(7)
    print("Test 2, expected: 123, 456, 7 got: " + q.ShowData())
    if not q.ShowData() == "123, 456, 7":
        return False

    # Test 3
    e = q.Dequeue()
    print("Test 3, expected: 456, 7 got: " + q.ShowData())
    if not q.ShowData() == "456, 7":
        return False

    # Test 4
    print("Test 4, expected: 123 got: " + str(e))
    if not e==123:
        return False

    # Test 5
    q.Dequeue()
    q.Dequeue()
    e = q.Dequeue()
    print("Test 5, expected: -1 got: " + str(e))
    if not e == -1:
        return False

    return True

if not RunTests():
    print("See messages for error, please correct.")
else:
    print("Congrats, all tests passed.")