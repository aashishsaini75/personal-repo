import subprocess
import csv
import unittest
class test_multi_user(unittest.TestCase):
    with open('ekata_player_sheet.csv', "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ['player_Username','business_email'])
    subprocess.run("python3 player1.py & python3 player2.py & python3 player3.py & python3 player4.py & python3 player5.py"  , shell=True)
