import subprocess
import unittest
from glob import glob
from itertools import product
from os.path import dirname


class TestBuilds(unittest.TestCase):
    pass


for file, device in product(glob("{}/*.py".format(dirname(__file__))), ["Beta", "MicroR2", "Zybo"]):
    if "test_builds" in file:
        continue


    def make_test_builds(file, device):
        def test_builds(self):
            process = subprocess.Popen(['python', file, '-e', '-d', device], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout, stderr = process.communicate()
            print(stdout.decode("utf-8"))
            print(stderr.decode("utf-8"))

            self.assertEqual(0, process.returncode)

        return test_builds


    filename_stripped = file.split("/")[-1].replace(".py", "")
    setattr(TestBuilds, "test_{}_{}".format(filename_stripped, device), make_test_builds(file, device))