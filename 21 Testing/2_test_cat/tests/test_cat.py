from unittest import TestCase, main


# from project.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_cat_size_increased_after_eating(self):
        expected_result = 1
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_result, self.cat.size)

    def test_feed_cat_if_is_fed_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleeping_cat_is_fed_makes_cat_not_sleepy(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

    def test_cat_can_not_fall_asleep_if_not_fed_error(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
