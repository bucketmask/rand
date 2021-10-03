def make_graph():
    for y in range(4, -5, -1):
        for x in range (-7, 7):
            print("(%d, %d)" %(x,y), end="")
        print("\n")

make_graph()