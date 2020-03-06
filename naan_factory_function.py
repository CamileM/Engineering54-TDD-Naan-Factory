# factory functions

# define our Function here


# 1. As a user, I can use the make_dough with water and flour to make dough
def make_dough(arg1, arg2):
    if (arg1 == 'water') and (arg2 == 'flour'):
        return('dough')

    else:
        return('not dough')

# 2. As a user, I can use the bake_dough with dough to get naan
def bake_dough(arg1, arg2):
    if (arg1 == 'bake_dough') and (arg2 == 'dough'):
        return('naan')

    else:
        return('not naan')