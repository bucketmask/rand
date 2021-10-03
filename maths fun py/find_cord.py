def equation(x):
    y = ((x-1)*(x+3)*(x-1)*(x+3))
    return y

def find_cord():
    cord = []
    for x in range(-60,61):
        cord.append([x,round(equation(x))])
    return cord
    
print(find_cord())
