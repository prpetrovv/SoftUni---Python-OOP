from unittest import TestCase, main

# from project.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(1, '2', 3.5, 4, '10')

    def test_correct_integer_and_get_data(self):
        self.assertEqual([1, 4], self.integer_list.get_data())

    def test_operation_adds_integer_to_list(self):
        expected_data = self.integer_list.get_data() + [5]
        acceptable_v = self.integer_list.add(5)
        self.assertEqual(expected_data, acceptable_v)

    def test_add_operation_not_integer_error(self):
        expected_error_message = "Element is not Integer"
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.5)
        self.assertEqual(expected_error_message, str(ex.exception))

    def test_remove_index_operation_out_of_index_error(self):
        expected_error_message = "Index is out of range"
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(200)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_remove_index_with_valid_index(self):
        expected = [1]
        deleted_element = 4
        removed_element = self.integer_list.remove_index(1)

        self.assertEqual(expected, self.integer_list.get_data())
        self.assertEqual(deleted_element, removed_element)

    def test_get_data_with_invalid_inndex_error(self):
        expected_error_message = "Index is out of range"
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(200)
        self.assertEqual(expected_error_message, str(ie.exception))

    def test_get_data_with_valid_index(self):
        expected = 4
        found_element = self.integer_list.get(1)
        self.assertEqual(expected, found_element)

    def test_insert_integer_with_valid_index(self):
        expected_list = [1, 6, 4]
        self.integer_list.insert(1, 6)
        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_insert_element_with_valid_index(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(200, 6)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_float_element_with_valid_index_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1, 6.5)
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_get_biggest_element(self):
        self.assertEqual(4, self.integer_list.get_biggest())

    def test_get_index_of_element(self):
        self.assertEqual(1, self.integer_list.get_index(4))


if __name__ == '__main__':
    main()
