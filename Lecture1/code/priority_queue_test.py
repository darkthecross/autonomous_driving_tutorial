from priority_queue import PriorityQueue

def RunTests():
    q = PriorityQueue()
    
    # Test 1
    print("Test 1, expected:  got: " + q.ShowData())
    if not q.ShowData() == "":
        return False

    # Test 2
    q.Enqueue({"name": "xiaoming", "age": 12})
    q.Enqueue({"name": "xiaozhang", "age": 20})
    q.Enqueue({"name": "zhaomin", "age": 10})
    print("Test 2, expected: {'name': 'zhaomin', 'age': 10}, {'name': 'xiaoming', 'age': 12}, {'name': 'xiaozhang', 'age': 20} got: " + q.ShowData())
    if not q.ShowData() == "{'name': 'zhaomin', 'age': 10}, {'name': 'xiaoming', 'age': 12}, {'name': 'xiaozhang', 'age': 20}":
        return False

    # Test 3
    e = q.Dequeue()
    print("Test 3, expected: {'name': 'xiaoming', 'age': 12}, {'name': 'xiaozhang', 'age': 20} got: " + q.ShowData())
    if not q.ShowData() == "{'name': 'xiaoming', 'age': 12}, {'name': 'xiaozhang', 'age': 20}":
        return False

    # Test 4
    print("Test 4, expected: {'name': 'zhaomin', 'age': 10} got: " + str(e))
    if not e=={'name': 'zhaomin', 'age': 10}:
        return False

    # Test 5
    q.Dequeue()
    q.Dequeue()
    e = q.Dequeue()
    print("Test 5, expected: {'name':'', 'age': 0} got: " + str(e))
    if not e == {"name":"", "age": 0}:
        return False

    return True

if not RunTests():
    print("See messages for error, please correct.")
else:
    print("Congrats, all tests passed.")