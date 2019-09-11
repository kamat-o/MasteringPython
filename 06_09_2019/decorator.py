def deco(func):

    def inner():
        print("Test Case Tear up")
        func()
        print("Test Case Tear Down")

    return inner

@deco
def printMessege():
    print("Test Case")

printMessege()