# This is the math project for HW 1

import sympy as sp

######## Problem 2 ########
def prob2():
    # Setup
    x1, x2, u1 = sp.symbols('x1 x2 u')
    b, m, l, g = sp.symbols('b m l g')

    x = sp.Matrix([x1, 
                x2])

    u = sp.Matrix([u1])

    f = sp.Matrix([x2,
                    -b/(m*l)*x2 - g*sp.sin(x1) + u1])

    h = sp.Matrix([x1,
                   0])

    # First eq point theta = 0
    xn = sp.Matrix([0, 
                    0])
    un = sp.Matrix([0])

    px = x - xn
    pu = u - un

    eval_dict = {**{xi:xni for xi,xni in zip(x,xn)}, **{ui:uni for ui,uni in zip(u,un)}}
    A = f.jacobian(x).subs(eval_dict)
    B = f.jacobian(u).subs(eval_dict)
    C = h.jacobian(x).subs(eval_dict)
    D = h.jacobian(u).subs(eval_dict)

    print("\n\n\n Problem 2a \n")

    for M in [A,B,C,D]:
        sp.pprint(M)
        print(sp.latex(M))

    pdx = A*px + B*pu
    py = C*px + D*pu



    sp.pprint(pdx)
    print(sp.latex(pdx))

    sp.pprint(py)
    print(sp.latex(py))





    # Second eq point theta = pi
    xn = sp.Matrix([sp.pi, 
                    0])
    un = sp.Matrix([0])

    px = x - xn
    pu = u - un

    eval_dict = {**{xi:xni for xi,xni in zip(x,xn)}, **{ui:uni for ui,uni in zip(u,un)}}
    A = f.jacobian(x).subs(eval_dict)
    B = f.jacobian(u).subs(eval_dict)
    C = h.jacobian(x).subs(eval_dict)
    D = h.jacobian(u).subs(eval_dict)

    print("\n\n\n Problem 2b \n")

    for M in [A,B,C,D]:
        sp.pprint(M)
        print(sp.latex(M))

    pdx = A*px + B*pu
    py = C*px + D*pu

    sp.pprint(pdx)
    print(sp.latex(pdx))

    sp.pprint(py)
    print(sp.latex(py))

prob2()




######## Problem 3 ########
def prob3():
    x1, x2, x3, v, w  = sp.symbols("x1 x2 x3 v w")

    x = sp.Matrix([x1,
                   x2,
                   x3])
    u = sp.Matrix([v,
                   w])
    
    f = sp.Matrix([w*x2+v,
                   -w*x1,
                   w])
    h = sp.Matrix([x1,
                   x2])
    
    xn = sp.Matrix([0,
                    0,
                    0])
    un = sp.Matrix([0,
                    0])

    
    px = x - xn
    pu = u - un
    eval_dict = {**{xi:xni for xi,xni in zip(x,xn)}, **{ui:uni for ui,uni in zip(u,un)}}
    A = f.jacobian(x).subs(eval_dict)
    B = f.jacobian(u).subs(eval_dict)
    C = h.jacobian(x).subs(eval_dict)
    D = h.jacobian(u).subs(eval_dict)

    print("\n\n\n Problem 3 \n")

    for M in [A,B,C,D]:
        sp.pprint(M)
        print(sp.latex(M))

    pdx = A*px + B*pu
    py = C*px + D*pu

    sp.pprint(pdx)
    print(sp.latex(pdx))

    sp.pprint(py)
    print(sp.latex(py))

prob3()