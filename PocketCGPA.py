print("====================================")

print(" PERSONAL POCKET CGPA CALCULATOR")

print("====================================")

courses = int(input("Enter number of courses: "))

total_points = 0

total_units = 0

for i in range(1, courses + 1):

    print(f"\nCourse {i}")

    unit = int(input("Course Unit: "))

    grade = input("Grade (A-F): ").upper()

    match grade:

        case "A":

            point = 5

        case "B":

            point = 4

        case "C":

            point = 3

        case "D":

            point = 2

        case "E":

            point = 1

        case "F":

            point = 0

        case _:

            print("Invalid Grade! Grade Point = 0")

            point = 0

    total_points += point * unit

    total_units += unit

if total_units > 0:

    cgpa = total_points / total_units

    print("\n==============================")

    print(f"Total Units : {total_units}")

    print(f"Total Points: {total_points}")

    print(f"CGPA        : {cgpa:.2f}")

    print("==============================")

else:

    print("No course units entered.")
