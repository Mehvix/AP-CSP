import math

x = input("What are you solving for?\n"  # Max
          "Num | Solving for\t| Given\n"
          "[1] | Final Velocity| Initial velocity, acceleration, and time\n"
          "[2] | △ X\t\t\t| Final and initial velocity, and time\n"
          "[3] | △ X\t\t\t| Acceleration)| Initial Velocity, time, and acceleration\n"
          "[4] | Final Velocity| Initial velocity, acceleration, and distance)\n"
          )


def Velocity(dX, dT):
    print("This function will calculate the Velocity given the change in position and the change in time.")
    dX = float(input("Enter the change in position (meters)\n"))
    dT = float(input("Enter the change in time (seconds)\n"))
    V = dX / dT
    return "The velocity is " + str(round(V, 2)) + " m/s"


if x == "1":  # Jack
    print(Velocity(0, 0))

if x == "2":  # Max
    veli = float(input("Initial Velocity?\n"))
    velf = float(input("Final Velocity?\n"))
    acc = float(input("Acceleration?\n"))
    time = float(input("Time?\n"))
    print(round(((velf + veli) / 2) * time, 2), " meters")

if x == "3":  # Aidan
    vel = float(input("Initial Veclocity?\n"))
    time = float(input("Time?\n"))
    accel = float(input("Acceleration?\n"))
    print(round(((vel * time) + (0.5 * accel * (time ** 2))), 2), " meters")


def finalVelocity():
    """
    This method finds the second velocity when the user gives the first velocity, the acceleration, and the distance
    """
    velocity1 = input("Enter the first velocity: \n")
    acceleration = input("Enter the acceleration: \n")
    distance = input("Enter the distance (meters): \n")

    velocity2 = (int(velocity1) ** 2) + (2 * (int(acceleration) * int(distance)))
    return "Your second velocity is: " + str(round(math.sqrt(velocity2), 2)) + " meters per second."


if x == "4":  # Bert
    print(finalVelocity())
