def bricks(n, m, z):
    resto = z
    resto = resto - 5 * min(m, z/5)
    return resto - n <= 0