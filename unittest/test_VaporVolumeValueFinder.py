import unittest
import os

import VaporVolumeValueFinder

from VaporVolumeValueFinder import XyzDataFile, OUfile_Parser

class TestXyzDataFile(unittest.TestCase):
    def test_init(self):
        data_file = XyzDataFile(
            filename="test_data.txt",
            type_of_file="text",
            x_var="x",
            y_var="y",
            z_var="z",
            x_unit="m",
            y_unit="m",
            z_unit="m",
            xdata=[1, 2, 3],
            ydata=[4, 5, 6],
            zdata=[7, 8, 9]
        )
        self.assertEqual(data_file.filename, "test_data.txt")
        self.assertEqual(data_file.type_of_file, "text")
        self.assertEqual(data_file.x_var, "x")
        self.assertEqual(data_file.y_var, "y")
        self.assertEqual(data_file.z_var, "z")
        self.assertEqual(data_file.x_unit, "m")
        self.assertEqual(data_file.y_unit, "m")
        self.assertEqual(data_file.z_unit, "m")
        self.assertListEqual(data_file.xdata, [1, 2, 3])
        self.assertListEqual(data_file.ydata, [4, 5, 6])
        self.assertListEqual(data_file.zdata, [7, 8, 9])

    def test_set_filename(self):
        data_file = XyzDataFile()
        data_file.set_filename("test_data.txt")
        self.assertEqual(data_file.filename, "test_data.txt")

    # Similar tests can be written for other setter methods

class TestOUfileParser(unittest.TestCase):
    def setUp(self):
        self.filepath = "test_data.txt"
        with open(self.filepath, "w") as file:
            file.write(
                "vapor_volume-rfile\n"
                "\"Time Step\" \"vapor_volume etc..\"\n"
                "(\"Time Step\" \"vapor_volume\" \"flow-time\")\n"
                "0 0 0\n"
                "1 0.2509840045191862 2e-06\n"
                "2 0.0663933315875346 4e-06\n"
                "3 0.04220392081767918 6e-06\n"
                "4 0.03762467853132718 8e-06\n"
            )

    def tearDown(self):
        # Clean up the test file after testing
        os.remove(self.filepath)

    def test_read_datafile(self):
        parser = OUfile_Parser()
        parser.read_datafile(self.filepath)
        self.assertEqual(parser.type_of_file, "text")
        self.assertEqual(parser.x_var, "Time Step")
        self.assertEqual(parser.y_var, "vapor_volume")
        self.assertEqual(parser.z_var, "flow-time")
        self.assertListEqual(parser.xdata, [0, 1, 2, 3, 4])
        self.assertListEqual(parser.ydata, [0, 0.2509840045191862, 0.0663933315875346, 0.04220392081767918, 0.03762467853132718])
        self.assertListEqual(parser.zdata, [0, 2e-06, 4e-06, 6e-06, 8e-06])

if __name__ == "__main__":
    unittest.main()
