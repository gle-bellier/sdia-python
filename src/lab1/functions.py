def is_unique(x):
<<<<<<< HEAD
<<<<<<< HEAD
    """[This functions tell if all integer element are unique in the list]

    Args:
        x ([int list]): [The input is a list of integer]

    Returns:
        [Boolean]: [We return True if all element of the list are unique and False otherwise]
    """
    for i in x:
        if x.count(i) > 1 :
            return False
    return True

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
=======
    while x != []:
        elt = x.pop()
        if elt in x: return False
    return True


def is_unique2(x):
    return len(x) == len(set(x))


def triangle_shape(n):
    """Do triangle shape in string

    Args:
        n (int): [description]

    Returns:
        [type]: [description]
    """

    base_n = 2 * n - 1
    res = []
    for i in range(1, n + 1):
        step_n = 2 * i - 1
        res.append(" " * ((base_n - step_n) // 2) + "x" * step_n + " " *
                   ((base_n - step_n) // 2))

>>>>>>> 5b3c5e33384ccf2de8937b90843561ff0f84b4b8
    return "\n".join(res)
=======
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


def triangle_shape(n, fillchar="x", spacechar=" "):
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
