def is_unique(x):
<<<<<<< HEAD
    """[This functions tell if all integer element are unique in the list]
=======
    while x != []:
        elt = x.pop()
        if elt in x: return False
    return True


def is_unique2(x):
    return len(x) == len(set(x))


def triangle_shape(n):
    """Do triangle shape in string
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6

    Args:
        x ([int list]): [The input is a list of integer]

    Returns:
        [Boolean]: [We return True if all element of the list are unique and False otherwise]
    """
    for i in x:
        if x.count(i) > 1 :
            return False
    return True

<<<<<<< HEAD
def triangle_shape(height):
    """[This is a funny little functions that creates triangle shaped of "x"]

    Args:
        height ([int]): [We enter the number of floor that the pyramid will have]]

    Returns:
        [list of str]: [We have a list of string that contains each floor of the pyramid]
    """
    print(f"height={height}")
    res = []
    for i in range(0,height):
        pyr = "x"
        res += [((height-i-1)*" "+(2*i+1)*pyr+(height-i-1)*" ")]
    return res
=======
    base_n = 2 * n - 1
    res = []
    for i in range(1, n + 1):
        step_n = 2 * i - 1
        res.append(" " * ((base_n - step_n) // 2) + "x" * step_n + " " *
                   ((base_n - step_n) // 2))

    return "\n".join(res)
>>>>>>> 33d47d303384c651375b0880d2b8406c199949a6
