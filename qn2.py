# using a function create a program that calc the volume of the cylinder
#v= V = πr^2h

# define a function to calculate the volume of a cylinder
def calculate_volume_of_cylinder(radius, height):
    pi = 3.14159
    volume = pi * (radius ** 2) * height
    return volume

#  radius and height inputs 
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate the volume by calling the function
volume = calculate_volume_of_cylinder(radius, height)

# print the result
print(f"The volume of the cylinder is: {volume:.3f}")
