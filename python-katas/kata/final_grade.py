def final_grade(exam, projects):
    print("Exam {exam}, projects {projects}".format(exam=exam, projects=projects))
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    return 0
