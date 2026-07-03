import numpy as np

# Generate a 2D array of shape 10 students × 5 subjects) with random marksbetween 30 and 100.
marks = np.random.randint(30, 101, size=(10, 5))
# Print the array 
print("Marks:\n", marks)

# For each student, calculate total marks and average.
totals = marks.sum(axis=1)
averages = marks.mean(axis=1)
print("\nTotal marks:", totals)
print("Average marks:", averages)

# find the student with highest and lowest total marks (use argmax/argmin).
print("\nHighest total: Student", totals.argmax()+1,)
print("Lowest total: Student", totals.argmin()+1,)
print(totals.max())
print(totals.min())

# Calculate overall class mean and standard deviation
class_mean = marks.mean()
class_std = marks.std()

# Reshape the array if needed and demonstrate indexing to extract marks of top 3 students.
top3 = totals.argsort()[-3:][::-1]
print("\nMarks of top 3 students:\n", marks[top3])
