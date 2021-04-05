"""
File data/students.csv stores information about students in CSV format.
This file contains the student’s names, age and average mark.
1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass
print(get_top_performers("students.csv"))
Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']
2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass
Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv


def get_top_performers(file_path: str, number_of_top_students=5):
    with open(file_path, encoding='utf-8') as csv_file:
        # csv_reader iterator through the lines, each line is represented as a list
        csv_reader = csv.reader(csv_file, delimiter=',')
        content = [lst for lst in csv_reader]
    content = [name[0] for name in sorted(content[1:], key=lambda mark: float(mark[2]), reverse=True)]
    return content[:number_of_top_students]


def write_students_age_desc(file_path: str, output_file: str):
    with open(file_path, encoding='utf-8') as from_csv_file, \
            open(output_file, 'w', newline='', encoding='utf-8') as to_csv_file:
        csv_reader = csv.reader(from_csv_file, delimiter=',')
        csv_writer = csv.writer(to_csv_file, delimiter=',')
        sorted_list = sorted(csv_reader, key=lambda row: row[1], reverse=True)
        for row in sorted_list:
            csv_writer.writerow(row)


if __name__ == '__main__':
    file_path = 'C:/Users/illic/data/students.csv'
    output_file = 'C:/Users/illic/data/students_sorted_by_age.csv'
    print(f'\nThe first 10 lines of {file_path}:')
    with open(file_path) as f:
        for i in range(10):
            print(f.readline().rstrip())
    print(f'\n1) The top performer students: {get_top_performers(file_path)}')
    print(f'\n2) Writing sorted by age data into {output_file} ...')
    write_students_age_desc(file_path, output_file)
    print(f'\n{output_file} created! The first 10 lines of {output_file}: ')
    with open(output_file) as f:
        for i in range(10):
            print(f.readline().rstrip())
