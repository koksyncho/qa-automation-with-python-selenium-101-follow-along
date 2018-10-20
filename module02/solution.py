IS_TRUE = True
IS_FALSE = False

PANCAKE_INGREDIENTS = {
    "flour": 2,
    "eggs": 4,
    "milk": 200,
    "butter": False,
    "salt": 0.001
}

FIBONACCI_NUMBERS = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def num_add(a, b):
    add = a + b
    return add

def num_sub(a, b):
    sub = a - b
    return sub

def num_mul(a, b):
    mul = a * b
    return mul

def num_div(a, b):
    div = a / b
    return div

def num_floor(a, b):
    floorDiv = a // b
    return floorDiv

def num_rem(a, b):
    rem = a % b
    return rem

def ingredient_exists(ingr, dict):
    if (ingr in dict):
        return True
    else:
        return False

def fatten_pancakes(dict):
    dictCopy = dict.copy()
    dictCopy["eggs"] = 6
    dictCopy["butter"] = True
    return dictCopy

def add_sugar(dict):
    dict["suggar"] = 0.001
    return dict

def remove_salt(dict):
    del dict["salt"]
    return dict

def add_fibonacci(lst):
    lst.append(lst[len(lst)-1] + lst[len(lst)-2])
    return lst

def fib_exists(lst, n):
    if (n in lst):
        return True
    else:
        return False

def which_fib(lst, n):
    if (n in lst):
        return (lst.index(n)+1)

if __name__ == "__main__":
    c = 7
    d = 5
    print(num_add(c, d))
    print(num_sub(c, d))
    print(num_mul(c, d))
    print(num_div(c, d))
    print(num_floor(c, d))
    print(num_rem(c, d))

    print(PANCAKE_INGREDIENTS)
    print(ingredient_exists("eggs", PANCAKE_INGREDIENTS))

    FATTER_PANCAKE_INGREDIENTS = fatten_pancakes(PANCAKE_INGREDIENTS)
    print(FATTER_PANCAKE_INGREDIENTS)
    add_sugar(PANCAKE_INGREDIENTS)
    print(PANCAKE_INGREDIENTS)
    remove_salt(PANCAKE_INGREDIENTS)
    print(PANCAKE_INGREDIENTS)

    print(FIBONACCI_NUMBERS)
    FIBONACCI_NUMBERS = add_fibonacci(FIBONACCI_NUMBERS)
    print(FIBONACCI_NUMBERS)
    print(fib_exists(FIBONACCI_NUMBERS, 5))
    print(which_fib([1, 1], 2))

    ''' errors in add_sugar(), remove_salt(), and which_fib() '''
