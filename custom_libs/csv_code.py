import csv as c
import os
from file_management_code import FileManagement


class CsvFile(FileManagement):
    def __init__(self):
        super().__init__()

    def read_csv_file(self, directory):
        data = []

        code = super().get_test_code()
        path = super().get_data_folder_path() + directory + "\\" + code + ".csv"

        with open(path, 'rt') as csv_file:
            reader = c.reader(csv_file)
            for row in reader:
                data.append(row)
        return data

    def create_csv_file(self, directory, filename):
        path = os.getcwd() + "\\data\\" + directory + "\\" + filename + ".csv"
        path = path.replace("custom_libs", "")

        super().create_directory_on_data_folder(directory)

        validate = super().check_if_file_exists(path)
        if validate:
            super().clear_file(path)
        else:
            open(path, "x").close()

    def add_row_to_csv(self, directory, values_to_add):
        code = super().get_test_code()

        path = super().get_data_folder_path() + directory + "\\" + code + ".csv"

        validate = super().check_if_file_exists(path)
        if validate:
            with open(path) as file:
                rows = sum(1 for line in file)
                file.close()
            with open(path, 'a') as file:
                if rows > 0:
                    file.write("\n" + values_to_add)
                else:
                    file.write(values_to_add)
                file.close()
        else:
            self.create_csv_file(directory, code)
            self.add_row_to_csv(directory, values_to_add)


if __name__ == "__main__":
    csv = CsvFile()
    #csv.create_csv_file("directory\\example\\example2\\example3", "filename_example")
    for i in range(10):
        csv.add_row_to_csv("directory\\example\\example2\\example3", "value 1")
    print(csv.read_csv_file("directory\\example\\example2\\example3"))