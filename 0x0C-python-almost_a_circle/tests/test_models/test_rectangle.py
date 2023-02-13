#!/usr/bin/python3
"""unit tests for the Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.rectangle import __doc__
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """tests the rectangle class"""
    def setUp(self):
        """initialize nb_objects before each tests"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """cleans up each test"""
        pass

    def test_doc_strings(self):
        """tests doc strings"""
        self.assertIsNotNone(__doc__)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)

    def test_attributes(self):
        """tests if required attributes exits"""
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIs(hasattr(Rectangle, "height"), True)
        self.assertIs(hasattr(Rectangle, "x"), True)
        self.assertIs(hasattr(Rectangle, "y"), True)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIs(hasattr(Rectangle, "__str__"), True)

    def test_class(self):
        """tests if Rectangle is a class"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.\
Rectangle'>")

    def test_inheritance(self):
        """tests if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_instance(self):
        """tests if initialized varible is an instance of a Rectangle"""
        rect_one = Rectangle(1, 2)
        rect_two = Rectangle(3, 4)
        self.assertTrue(isinstance(rect_one, Rectangle), True)
        self.assertTrue(isinstance(rect_two, Rectangle), True)

    def test_required_arguments(self):
        """tests if required arguments were given"""
        with self.assertRaises(TypeError) as err:
            rectangle_one = Rectangle()

            err_msg = "__init__() missing 2 required positional \
arguments: 'width' and 'height'"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(TypeError) as err:
            rectangle_two = Rectangle(10)

            err_msg = "__init__() missing 1 required positional argument: \
'height'"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(TypeError) as err:
            rectangle_three = Rectangle(10, 20, 30, 40, 50, 60, 70)

            err_msg = "__init__() takes from 3 to 6 postional arguments \
but 7 were given"

            self.assertEqual(str(err.exception), err_msg)

    def test_initialization(self):
        """test if initialization is correct"""
        rect_one = Rectangle(2, 4)
        dict_one = {
                'id': 1,
                '_Rectangle__width': 2,
                '_Rectangle__height': 4,
                '_Rectangle__x': 0,
                '_Rectangle__y': 0
                }
        self.assertEqual(rect_one.__dict__, dict_one)
        rect_two = Rectangle(10, 20, 30, 40, 50)
        dict_two = {
                'id': 50,
                '_Rectangle__width': 10,
                '_Rectangle__height': 20,
                '_Rectangle__x': 30,
                '_Rectangle__y': 40
                }
        self.assertEqual(rect_two.__dict__, dict_two)
        rect_three = Rectangle(id=12, x=7, width=89, height=1, y=3)
        dict_three = {
                'id': 12,
                '_Rectangle__width': 89,
                '_Rectangle__height': 1,
                '_Rectangle__x': 7,
                '_Rectangle__y': 3
                }
        self.assertEqual(rect_three.__dict__, dict_three)

    def test_getter_and_setter(self):
        """tests the getter and setter methods"""
        rect = Rectangle(2, 4, id=17)
        rect.width = 6
        rect.height = 8
        rect.x = 10
        rect.y = 10

        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 17)

    def test_invalid_attributes(self):
        """tests invalid attributes"""
        with self.assertRaises(TypeError) as err:
            Rectangle(10, "10")

            err_msg = "height must be an integer"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            Rectangle(10, 0)

            err_msg = "height must be > 0"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(10, 10)
            rect.width = [1, 2]
            err_msg = "width must be an integer"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(10, 10)
            rect.width = -10
            err_msg = "width must be > 0"

            self.assertEqual(str(err.exception), err_msg)
        with self.assertRaises(TypeError) as err:
            Rectangle(10, 10, "5", 5)

            err_msg = "x must be an integer"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            Rectangle(10, 10, -6, 6)

            err_msg = "x must be >= 0"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(TypeError) as err:
            rect = Rectangle(10, 10, 3, 3)
            rect.y = [1, 2]
            err_msg = "y must be an integer"

            self.assertEqual(str(err.exception), err_msg)

        with self.assertRaises(ValueError) as err:
            rect = Rectangle(10, 10, 10, 10)
            rect.y = -10
            err_msg = "y must be >= 0"
            self.assertEqual(str(err.exception), err_msg)

    def test_area(self):
        """tests if the area of a triangle is correct"""
        rect_one = Rectangle(2, 4)

        self.assertEqual(rect_one.area(), 8)

        rect_two = Rectangle(10, 20)

        self.assertEqual(rect_two.area(), 200)

        rect_three = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(rect_three.area(), 56)

    def test_display(self):
        """tests if the rectangle displays correctly"""
        rect_one = Rectangle(4, 6)
        rect_display_one = StringIO()
        with redirect_stdout(rect_display_one):
            rect_one.display()
            display_one = "\
####\n\
####\n\
####\n\
####\n\
####\n\
####\n\
"
        self.assertEqual(rect_display_one.getvalue(), display_one)

        rect_two = Rectangle(2, 2)
        rect_display_two = StringIO()
        with redirect_stdout(rect_display_two):
            rect_two.display()
            display_two = "\
##\n\
##\n\
"
        self.assertEqual(rect_display_two.getvalue(), display_two)

    def test_display_version2(self):
        """tests the display method"""
        rect_one = Rectangle(2, 3, 2, 2)
        rect_display_one = StringIO()
        with redirect_stdout(rect_display_one):
            rect_one.display()
            display_one = "\
\n\
\n\
  ##\n\
  ##\n\
  ##\n\
"
        self.assertEqual(rect_display_one.getvalue(), display_one)

        rect_two = Rectangle(3, 3, 1, 0)
        rect_display_two = StringIO()
        with redirect_stdout(rect_display_two):
            rect_two.display()
            display_two = "\
 ###\n\
 ###\n\
 ###\n\
"
        self.assertEqual(rect_display_two.getvalue(), display_two)

    def test_string_representation(self):
        """tests the string representation of the rectangle"""
        rect_one = Rectangle(4, 6, 2, 1, 12)
        msg = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(rect_one), msg)

        rect_two = Rectangle(5, 5, 1)
        msg = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(rect_two), msg)

    def test_update(self):
        """tests the update method"""
        rect_one = Rectangle(10, 10, 10, 10)
        rect_one.update(89)
        msg1 = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(rect_one), msg1)
        rect_one.update(89, 2)
        msg2 = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(rect_one), msg2)
        rect_one.update(89, 2, 3)
        msg3 = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(rect_one), msg3)
        rect_one.update(89, 2, 3, 4)
        msg4 = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(rect_one), msg4)
        rect_one.update(89, 2, 3, 4, 5)
        msg5 = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(rect_one), msg5)

    def test_update_vesrsion2(self):
        """tests the update method"""
        rect_one = Rectangle(10, 10, 10, 10)
        rect_one.update(height=1)
        msg1 = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(rect_one), msg1)
        rect_one.update(width=1, x=2)
        msg2 = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(rect_one), msg2)
        rect_one.update(y=1, width=2, x=3, id=89)
        msg3 = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(rect_one), msg3)
        rect_one.update(x=1, height=2, y=3, width=4)
        msg4 = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(rect_one), msg4)

    def test_to_dictionary(self):
        """tests the to_dictionary method"""
        rect_one = Rectangle(10, 2, 1, 9)
        dict_one = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(rect_one.to_dictionary(), dict_one)

        rect_two = Rectangle(10, 20, 0, 0)
        dict_two = {'x': 0, 'y': 0, 'id': 1, 'height': 20, 'width': 10}
        self.assertEqual(rect_one.to_dictionary(), dict_one)


if __name__ == "__main__":
    unittest.main()
