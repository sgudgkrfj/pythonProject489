#теорія
print('bsvbwe',2123,9.0)

def black_hole(*args):
    print(type(args))
    print(args)
    for argument in args:
        print(argument)

black_hole(234,"Earth","rusnia","time")


def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for argument in kwargs:
        print(argument)
black_hole_named(name="Gleb", planet="Earth",number=5)


def black_hole_named(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)
black_hole_named(name="Gleb", planet="Earth",number=5)




black_hole_full(name="Gleb", planet="Earth",number=5)






