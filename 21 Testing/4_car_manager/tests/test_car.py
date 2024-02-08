from unittest import TestCase, main

from project.car_manager import Car


class TestCarManager(TestCase):
    def setUp(self) -> None:
        self.car = Car('VW', 'Polo', 5, 70)

    def test_the_constructor(self):
        self.assertEqual('VW', self.car.make)
        self.assertEqual('Polo', self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_not_correct_empty_error(self):
        expected_error_message = "Make cannot be null or empty!"
        with self.assertRaises(Exception) as ec:
            self.car.make = ''
        self.assertEqual(expected_error_message, str(ec.exception))

    def test_model_not_correct_empty_error(self):
        expected_error_message = "Model cannot be null or empty!"
        with self.assertRaises(Exception) as ec:
            self.car.model = ''
        self.assertEqual(expected_error_message, str(ec.exception))

    def test_fuel_consumption_not_correct_error(self):
        expected_error_message = "Fuel consumption cannot be zero or negative!"
        with self.assertRaises(Exception) as ec:
            self.car.fuel_consumption = 0
        self.assertEqual(expected_error_message, str(ec.exception))

    def test_fuel_capacity_not_correct_error(self):
        expected_error_message = "Fuel capacity cannot be zero or negative!"
        with self.assertRaises(Exception) as ec:
            self.car.fuel_capacity = 0
        self.assertEqual(expected_error_message, str(ec.exception))

    def test_refuel_with_correct_values(self):
        fuel_amount_to_add = 1
        expected_fuel = self.car.fuel_amount + 1
        self.car.refuel(fuel_amount_to_add)
        self.assertEqual(expected_fuel, self.car.fuel_amount)

    def test_refuel_with_incorrect_values_error(self):
        fuel_amount_to_add = 0
        expected_error_message = "Fuel amount cannot be zero or negative!"
        with self.assertRaises(Exception) as ec:
            self.car.refuel(fuel_amount_to_add)
        self.assertEqual(expected_error_message, str(ec.exception))

    def test_drive_with_correct_values(self):
        distance_to_drive = 100
        self.car.fuel_amount = 70
        expected_fuel_amount = self.car.fuel_amount - ((distance_to_drive / 100) * self.car.fuel_consumption)
        self.car.drive(distance_to_drive)
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_drive_with_incorrect_values_error(self):
        distance_to_drive = 200000000
        expected_error_message = "You don't have enough fuel to drive!"
        with self.assertRaises(Exception) as ec:
            self.car.drive(distance_to_drive)
        self.assertEqual(expected_error_message, str(ec.exception))


if __name__ == '__main__':
    main()
