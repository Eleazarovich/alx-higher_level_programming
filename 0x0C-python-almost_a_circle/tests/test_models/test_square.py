#!/usr/bin/python3
"""unit tests for the Rectangle class"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.square import __doc__
from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """tests the square class"""
    def setUp(self):
        """starts each test"""
        pass

    def tearDown(self):
        """cleans up each test"""
        pass

    def test_doc_strings(self):
        """tests doc strings"""
        self.assertIsNotNone(__doc__)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)
        self.assertIsNotNone(Square.__str__.__doc__)

    def test_attributes(self):
        """tests if required attributes exits"""
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIs(hasattr(Square, "size"), True)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIs(hasattr(Square, "__init__"), True)

    def test_class(self):
        """tests if square is a class"""
        self.assertEqual(str(Square), "<class 'models.square.\
Square'>")

    def test_inheritance(self):
        """tests if Square inherits from Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_instance(self):
        """tests if initialized varible is an instance of a Square"""
        s1 = Square(3)
        s2 = Square(7)
        self.assertTrue(isinstance(s1, Square), True)
        self.assertTrue(isinstance(s2, Square), True)

    def test_required_arguments(self):
        """tests if required arguments were given"""
        with self.assertRaises(TypeError) as err:
            s1 = Square()

            err_msg = "__init__() missing 1 required positional \
argument: 'size'"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(TypeError) as err:
            s2 = Square(2, 4, 5, 6, 7, 7)

            err_msg = "__init__() takes from 2 to 5 positional arguments: \
'but 6 were given'"

            self.assertEqual(str(err.exception), err_msg)

    def test_initialization(self):
        """test if initialization is correct"""
        s1 = Square(4, id=1)
        dict_one = {
                'id': 1,
                '_Rectangle__width': 4,
                '_Rectangle__height': 4,
                '_Rectangle__x': 0,
                '_Rectangle__y': 0
                }
        self.assertEqual(s1.__dict__, dict_one)
        s2 = Square(10, 20, 30, 40)
        dict_two = {
                'id': 40,
                '_Rectangle__width': 10,
                '_Rectangle__height': 10,
                '_Rectangle__x': 20,
                '_Rectangle__y': 30
                }
        self.assertEqual(s2.__dict__, dict_two)
        s3 = Square(id=12, x=7, size=1, y=3)
        dict_three = {
                'id': 12,
                '_Rectangle__width': 1,
                '_Rectangle__height': 1,
                '_Rectangle__x': 7,
                '_Rectangle__y': 3
                }
        self.assertEqual(s3.__dict__, dict_three)

    def test_getter_and_setter(self):
        """tests the getter and setter methods"""
        s = Square(4, id=17)
        s.size = 6
        s.x = 10
        s.y = 10

        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 10)
        self.assertEqual(s.y, 10)
        self.assertEqual(s.id, 17)

    def test_invalid_attributes(self):
        """tests invalid attributes"""
        with self.assertRaises(TypeError) as err:
            Square("10")

            err_msg = "width must be an integer"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            Square(0)

            err_msg = "width must be > 0"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            Square(-4)

            err_msg = "width must be > 0"

            self.assertEqual(str(err.exception), err_msg)

    def test_display(self):
        """tests if the square displays correctly"""
        s1 = Square(4)
        s1_display = StringIO()
        with redirect_stdout(s1_display):
            s1.display()
            display_one = "\
####\n\
####\n\
####\n\
####\n\
"
        self.assertEqual(s1_display.getvalue(), display_one)

        s2 = Square(2)
        s2_display = StringIO()
        with redirect_stdout(s2_display):
            s2.display()
            display_two = "\
##\n\
##\n\
"
        self.assertEqual(s2_display.getvalue(), display_two)

        s3 = Square(2, 2, 2)
        s3_display = StringIO()
        with redirect_stdout(s3_display):
            s3.display()
            display_three = "\
\n\
\n\
  ##\n\
  ##\n\
"
        self.assertEqual(s3_display.getvalue(), display_three)

    def test_string_representation(self):
        """tests the string representation of the square"""
        s1 = Square(4, 6, 1, 12)
        msg = "[Square] (12) 6/1 - 4"
        self.assertEqual(str(s1), msg)

        s2 = Square(5, 5, 1)
        msg = "[Square] (9) 5/1 - 5"
        self.assertEqual(str(s2), msg)

    def test_update(self):
        """tests the update method"""
        s1 = Square(5)
        s1.update(10)
        msg1 = "[Square] (10) 0/0 - 5"
        self.assertEqual(str(s1), msg1)
        s1.update(1, 2)
        msg2 = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(s1), msg2)
        s1.update(1, 2, 3)
        msg3 = "[Square] (1) 3/0 - 2"
        self.assertEqual(str(s1), msg3)
        s1.update(1, 2, 3, 4)
        msg4 = "[Square] (1) 3/4 - 2"
        self.assertEqual(str(s1), msg4)
        s1.update(x=12)
        msg5 = "[Square] (1) 12/4 - 2"
        self.assertEqual(str(s1), msg5)
        s1.update(size=7, y=1)
        msg6 = "[Square] (1) 12/1 - 7"
        self.assertEqual(str(s1), msg6)
        s1.update(size=7, id=89, y=1)
        msg7 = "[Square] (89) 12/1 - 7"
        self.assertEqual(str(s1), msg7)

    def test_to_dictionary(self):
        """tests the to_dictionary method"""
        s1 = Square(10, 2, 1, id=1)
        d1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1.to_dictionary(), d1)

        s2 = Square(4, id=1)
        d2 = {'id': 1, 'x': 0, 'size': 4, 'y': 0}
        self.assertEqual(s2.to_dictionary(), d2)


if __name__ == "__main__":
    unittest.main()
