def multiply(x, y):
    # Base case
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y

    # Splitting x and y into two halves
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2
    a = x // 10**(m2)
    b = x % 10**(m2)
    c = y // 10**(m2)
    d = y % 10**(m2)

    # Recursively compute the products of the two halves
    ac = multiply(a, c)
    bd = multiply(b, d)
    ad_bc = multiply(a+b, c+d) - ac - bd

    # Combine the products of the two halves
    return ac * 10**(2*m2) + ad_bc * 10**(m2) + bd
