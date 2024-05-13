# Write your solution here
students = int(input("How many students on the course? "))
desired_group = int(input("Desired group size? "))


print(f"Number of groups formed: {-(-students // desired_group)}")