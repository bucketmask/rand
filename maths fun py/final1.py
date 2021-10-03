import find_cord

graph = find_cord.find_cord()

def make_graph(graph):
    for y in range(20, -21, -1):
        for x in range (-20,21):
            found = False
            for cord in graph:
                if x == cord[0] and y == cord[1]:
                    #print("(%d, %d)" %(x,y), end="")
                    print("#", end=" ")
                    found = True
                    break
            if (x == 0 and y == 0) and found == False:
                print("+", end=" ")
            elif (x == 0) and found == False:
                print("|", end=" ")
            elif (y == 0) and found == False:
                print("-", end=" ")
            elif found == False:
                print(" ", end=" ")
        print("")

make_graph(graph)
print("\n")