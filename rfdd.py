#1
def join_with_comma(*args):
    return ', '.join(args)
print(join_with_comma('apple', 'banana', 'cherry',))

#2
def get_min_max(*numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return (max_num, min_num)
print(get_min_max(1,2,4,5,10))
#3
def get_stepin(**kwargs):
    squares = {}
    for key, value in kwargs.items():
        squares[key] = value**2
    return squares
print(get_stepin(a = 7, b = 5,c = 10))
#4
def function(*args):
    spys = []
    for i in args:
        spys.append(i)
    else:
        pass
    print(spys)
function(1,2,3,4,5)


