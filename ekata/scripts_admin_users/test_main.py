import subprocess
import unittest
import csv
class test_user_add(unittest.TestCase):
    def test_add_a_user(self):
        # with open('ekata_user_sheet.csv', "w") as csv_file:
        #     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #     csv_writer.writerow(
        #         ['Username','email'])
        subprocess.run("python3 user_1.py & python3 user_2.py & python3 user_3.py & python3 user_4.py & python3 user_5.py"  , shell=True)
