""" We have n students' id and their GPAs. We want to find the 2nd maximum GPA. """
def find_second_max (id_gpa_list : list):
    """ Finding the second maximum GPA. """
    max_gpa =0
    second_max_gpa = 0
    max_id, second_max_id = None, None
    if len(id_gpa_list) < 2:
        return None
    for id,gpa in id_gpa_list:
        if gpa > max_gpa:
            second_max_id = max_id
            second_max_gpa = max_gpa
            max_gpa = gpa
            max_id = id
        elif gpa > second_max_gpa and gpa != max_gpa:
            second_max_gpa = gpa
            second_max_id = id
    return second_max_id, second_max_gpa


def main() -> None:
    """ The main function. """
    number = int(input("Enter the number of students:"))

    id_gpa_list = list()

    for i in range(number):
        print(f"Enter student ID and GPA of student {i+1}")
        student_id = input("ID: ")

        student_gpa = float(input("GPA: "))

        id_gpa_list.append((student_id, student_gpa))

    second_max_id, second_max_gpa = find_second_max(id_gpa_list)

    if second_max_gpa is None:
        print("There are less than two students or all GPAs are equal.")
    else:
        print(f"Second max student ID : {second_max_id}")
        print(f"Second max student GPA : {second_max_gpa}")


if __name__ == "__main__":
    main()
