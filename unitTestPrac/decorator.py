def my_decorator(func):
    print('add some perfume')
    # return func


@my_decorator  # 將 my_func 當做參數傳入 my_decorator 中
def my_func():
    print('Executed by decoractor')


# my_func = my_decorator(my_func)
my_func()
