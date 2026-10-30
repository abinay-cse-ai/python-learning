# Student Marks Analysis Project - by Abinay
students = ["Abinay", "Rahul", "Priya", "Anil"]
marks = [85, 90, 88, 92]

print("--- Student Report ---")
for i in range(len(students)):
    print(f"{students[i]} got {marks[i]} marks")

# Find topper
max_marks = max(marks)
topper_index = marks.index(max_marks)
print(f"\nTopper is {students[topper_index]} with {max_marks} marks")
print("\nProject done using Python basics")
