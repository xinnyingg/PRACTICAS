def update_arrival(h,m,d):
    total_minutes = h*60 + m + d
    new_h = (total_minutes //60)%24
    new_m = total_minutes %60
    return (new_h, new_m)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())