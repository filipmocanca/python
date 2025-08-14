father_name = input("Enter father's name: ")
father_age = int(input(f"How old is {father_name}: "))

mother_name = input("Enter mother's name: ")
mother_age = int(input(f"How old is {mother_name}: "))

ref_parent = input("Calculate Isabelle's age based on which parent? (father/mother): ").strip().lower()
age_diff = int(input("Enter the age difference between Isabelle and the chosen parent: "))

if ref_parent == "father":
    age_isa = father_age - age_diff
elif ref_parent == "mother":
    age_isa = mother_age - age_diff
else:
    print("Invalid parent selected.")
    exit()

print(f"Isabelle is {age_isa} years old, her father {father_name} is {father_age} years old, and her mother {mother_name} is {mother_age} years old.")
