"""
the function counts the number of holes in digits
0/4/6/9-one hole
8-two hole
"""

def count_holes(n):
    if type(n) != str and type(n) != int:
        return 'ERROR'
    else:
        n=int(n)
        n=str(n)
        otvet=0
        for i in n:
            if i == '0' or i=='4' or i=='6' or i=='9' :
                otvet = otvet + 1
            elif i == '8':
                otvet=otvet+2
        return (otvet)
