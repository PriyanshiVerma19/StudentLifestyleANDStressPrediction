print("Student Marks:\n", marks)#Rows=students,column=subjects
student_avg = np.mean(marks, axis=1)
print("\nAverage marks of each student:", student_avg)# avg of stu wise
subject_avg = np.mean(marks, axis=0)
print("\nAverage marks per subject:", subject_avg)# avg of colum wise
best_student = np.argmax(student_avg)
weak_student = np.argmin(student_avg)
print("\nBest Student Index:", best_student)
print("Weak Student Index:", weak_student)#best and weak students
pass_fail = student_avg >= 50
print("\nPass/Fail Status:", pass_fail)#pass fail
for i, status in enumerate(pass_fail):
    if status:
        print(f"Student {i+1}: PASS")
    else:
        print(f"Student {i+1}: FAIL")#student wise
weak_subjects = marks < 60
print("\nWeak marks (below 60):\n", weak_subjects)#weak students
test1 = np.array([65, 70, 80, 45, 60])
test2 = np.array([75, 72, 85, 50, 68])
improvement = test2 - test1
print("\nImprovement:", improvement)#improvements