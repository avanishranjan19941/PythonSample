
class Test:
    def multiply(a, b):
        return a * b

    def square(x):
        Test.dsaFun(x)
        return Test.multiply(x, x)

    def dsaFun(x):
        my_list = [1, 2, 3, 4, 5]
        if 5 in my_list:
            print("contains 5")
