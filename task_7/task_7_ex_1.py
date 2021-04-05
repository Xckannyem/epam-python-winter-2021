"""
Develop Rectangle class with following content:
    2 private fields type of float side_a and side_b (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method get_side_a, returning value of the side А;
    Method get_side_b, returning value of the side В;
    Method area, calculating and returning the area value;
    Method perimeter, calculating and returning the perimeter value;
    Method is_square, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method replace_sides, swapping rectangle sides.
Develop class ArrayRectangles, in which declare:
    Private attribute rectangle_array (list of rectangles);
    One constructor that creates a list of rectangles with length n filled with None and that receives an
    arbitrary amount of objects of type Rectangle or a list of objects of type Rectangle (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If n is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Method add_rectangle that adds a rectangle of type Rectangle to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method number_max_area, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method number_min_perimeter, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method number_square, that returns the number of squares in the array of rectangles
"""


class Rectangle:
    def __init__(self, a: float = 4, b: float = 3):
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = a
        self.__side_b = b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return 2 * (self.__side_a + self.__side_b)

    def is_square(self):
        if self.__side_a == self.__side_b:
            return True
        else:
            return False

    def replace_sides(self):
        return self.__side_a, self.__side_b == self.__side_b, self.__side_a


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        self.__n = n
        for i in args:
            if isinstance(i, Rectangle):
                self.__rectangle_array.append(i)
            elif isinstance(i, list):
                self.__rectangle_array.extend(i)
        if len(self.__rectangle_array) < n:
            add_values_num = n - len(self.__rectangle_array)
            self.__rectangle_array += [None] * add_values_num

    def add_rectangle(self, rectangle):
        if len(self.__rectangle_array) < self.__n and isinstance(rectangle, Rectangle):
            self.__rectangle_array.append(rectangle)
            return True
        else:
            return False

    def number_max_area(self):
        max_area = 0
        index = 0
        for i, rectangle in enumerate(self.__rectangle_array):
            if rectangle.area() > max_area:
                max_area = rectangle.area()
                index = i
        return index

    def number_min_perimeter(self):
        min_perimeter = None
        index = 0
        for i, rectangle in enumerate(self.__rectangle_array):
            if min_perimeter is None:
                min_perimeter = rectangle.perimeter()
                index = i
            elif rectangle.perimeter() < min_perimeter:
                min_perimeter = rectangle.perimeter()
                index = i
        return index

    def number_square(self):
        squares = 0
        for rectangle in self.__rectangle_array:
            if rectangle.is_square():
                squares += 1
        return squares
