
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_set = sorted(students_list)
st_gr_1 = (sum(grades[0]))/ len(grades[0])
st_gr_2 = (sum(grades[1]))/ len(grades[1])
st_gr_3 = (sum(grades[2]))/ len(grades[2])
st_gr_4 = (sum(grades[3]))/ len(grades[3])
st_gr_5 = (sum(grades[4]))/ len(grades[4])
students_average_grades = {}
students_average_grades.update({students_set[0] : st_gr_1, students_set[1] : st_gr_2, students_set[2] : st_gr_3,
      students_set[3] : st_gr_4, students_set[4] : st_gr_5})
print(students_average_grades)
