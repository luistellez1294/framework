import os


class FileManagement:
    def __init__(self):
        pass

    @staticmethod
    def clear_file(filename):
        open(filename, "w").close()

    @staticmethod
    def check_if_file_exists(path):
        return os.path.isfile(path)

    @staticmethod
    def check_if_directory_exists(path):
        return os.path.isdir(path)

    def create_directory_on_data_folder(self, directory):
        path = FileManagement.get_data_folder_path()
        if directory.__contains__("\\"):
            directories_array = directory.split("\\")
            if isinstance(directories_array, list):
                for i in directories_array:
                    path = path + "\\" + i
                    validate = self.check_if_directory_exists(path)
                    if not validate:
                        self.create_directory(path)
        else:
            self.create_directory(path + "\\" + directory)

    @staticmethod
    def create_directory(path):
        os.mkdir(path)

    @staticmethod
    def set_test_code(test_name):
        global global_test_code
        global_test_code = test_name.split("_").get(0)

    @staticmethod
    def get_test_code():
        #return global_test_code
        return "filename_example"

    @staticmethod
    def set_browser(browser):
        global global_browser
        global_browser = browser

    @staticmethod
    def get_browser():
        return global_browser

    @staticmethod
    def set_environment(environment):
        global global_environment
        global_environment = environment.split("_").get(0)

    @staticmethod
    def get_environment():
        return global_environment

    @staticmethod
    def get_data_folder_path():
        return os.getcwd().replace("custom_libs", "") + "\\data\\"

    @staticmethod
    def get_results_folder_path():
        return os.getcwd().replace("custom_libs", "") + "\\results\\"

    @staticmethod
    def get_tests_folder_path():
        return os.getcwd().replace("custom_libs", "") + "\\tests\\"

    @staticmethod
    def get_pom_folder_path():
        return os.getcwd().replace("custom_libs", "") + "\\pom\\"

    @staticmethod
    def remove_file(path):
        os.remove(path)

    @staticmethod
    def get_secrets_ini_path():
        return os.getcwd().replace("custom_libs", "") + "secrets.ini"

    @staticmethod
    def get_database_properties_file_path():
        return os.getcwd().replace("custom_libs", "") + "\\resources\\database.properties"

    def get_credentials(self, credentials):
        secrets_file = self.get_secrets_ini_path()
        validate = self.check_if_file_exists(secrets_file)

        if validate:
            with open(secrets_file, 'r') as secrets:
                text_by_row = [line.rstrip('\n') for line in secrets]
                for i in range(len(text_by_row)):
                    if text_by_row[i].__contains__("[" + credentials + "]"):
                        if text_by_row[i + 1].__contains__("user: ") or \
                                text_by_row[i + 1].__contains__("user: "):
                            username = text_by_row[i + 1].replace(" ", "").split("user:")[-1]
                        if text_by_row[i + 2].__contains__("password: ") or \
                                text_by_row[i + 2].__contains__("password: "):
                            password = text_by_row[i + 2].replace(" ", "").split("password:")[-1]
            secrets.close()
        creds = {
            "username": username,
            "password": password
        }
        return creds

    def get_database_properties(self, database):
        database_properties_file = self.get_database_properties_file_path()
        validate = self.check_if_file_exists(database_properties_file)

        environment = self.get_environment()

        if validate:
            with open(database_properties_file, 'r') as db_prop:
                text_by_row = [line.rstrip('\n') for line in db_prop]
                for i in range(len(text_by_row)):
                    if text_by_row[i].__contains__(database) and\
                            text_by_row[i].__contains__(environment + "hostname"):
                        host = text_by_row[i].replace(" ", "").split(database + environment + "_hostname=")[-1]
                    if text_by_row[i].__contains__(database) and\
                            text_by_row[i].__contains__(environment + "_port"):
                        port = text_by_row[i].replace(" ", "").split(database + environment + "port=")[-1]
            db_prop.close()
        properties = {
            "host": host,
            "port": port
        }
        return properties
