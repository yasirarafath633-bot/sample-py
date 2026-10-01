colour = ["BLUE", "RED", "GREEN", "YELLOW"]
Vehicle= ["CAR", "BIKE", "BUS", "TRUCK"]
ans1=(list(zip(colour, Vehicle)))
print(ans1)
for i in ans1:
   print(f"{i[0]} {i[1]}")
