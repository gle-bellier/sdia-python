def is_unique(x):
    for i in x:
        if x.count(i) > 1 :
            return False
    return True
