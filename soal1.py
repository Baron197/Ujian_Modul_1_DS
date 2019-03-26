def nbYear(p0, percent, aug, p) :
    year = 0
    while p0 < p :
        p0 = p0 + (p0 * percent/100) + aug
        year += 1
    
    return year

print(nbYear(1000,2,50,1200))
