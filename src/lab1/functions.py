def is_unique(x):
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
    return "\n".join(res)
