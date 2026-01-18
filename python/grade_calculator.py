def desire_grade(grade, grade_needed, assignment_worth, assigment_weight, total_points, earned_points):
    category_grade = (earned_points/total_points) * assignment_weight
    grade -= category_grade
    result = (((grade_needed - grade) / assignment_weight) * (total_points + assignment_worth)) - earned_points
    round(result, 2)


# def assigment_affect()   
grade = float(input("What's your grade (%): "))
grade_needed = float(input("Your desired grade (%): "))
assignment_worth = float(input("Assignment points: "))
assignment_weight = float(input("Weight of assignment category (%): "))
total_points = float(input("Total points in category: "))
earned_points = float(input("Earned points in category: "))

print(desire_grade(grade, grade_needed, assignment_worth, assignment_weight, total_points, earned_points))

    
 