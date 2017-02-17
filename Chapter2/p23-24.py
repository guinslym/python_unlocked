def f1():
   v1 = 'ohm'
   def f2():
       print('f2', v1)
       def f3():
           nonlocal v1
           v1 = 'mho' # this value will be output only within the scope of f3()
           print('f3', v1)
       f3()
       print('f2', v1)
   f2()
   print('f1', v1)


def fun():
    localsum = sum
    return localsum(localsum((a, a+1)) for a in range(1000))
