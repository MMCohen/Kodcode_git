coordinate_x = int(input("enter coordinates x: "))
coordinate_y = int(input("enter coordinates y: "))

if 10 <= coordinate_x <= 50 and 20 <= coordinate_y <= 80:
    if 10 < coordinate_x < 50 and 20 < coordinate_y < 80:
        print("Inside the rectangle")
    else:
        print("On the edge")
else:
    print("Outside the rectangle")