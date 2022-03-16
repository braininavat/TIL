import sys
n,r,c = map(int,sys.stdin.readline().split())
#r = row c = col

def div(n,row,col,val):
    if n == 0:
        return val
    quad = 2**(n-1)
    val_quad = quad*quad
    n -= 1
    if row<quad and quad<=col:      #1사분면 
        return div(n,row,col-quad,val+val_quad)
    elif row<quad and col<quad:     #2사분면
        return div(n,row,col,val)
    elif quad<=row and col<quad:    #3사분면
        return div(n,row-quad,col,val+2*val_quad)
    else:                           #4사분면
        return div(n,row-quad,col-quad,val+3*val_quad)
        
print(div(n,r,c,0))