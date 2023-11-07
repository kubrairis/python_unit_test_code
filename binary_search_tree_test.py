import unittest
from binary_search_tree import BinarySearchTree, TreeNode


class TestBinarySearchTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tree = BinarySearchTree()
        cls.tree.insert(5)
        cls.tree.insert(3)
        cls.tree.insert(7)
        cls.tree.insert(2)
        cls.tree.insert(4)
        cls.tree.insert(6)
        cls.tree.insert(8)

    def test_lower_returns_biggest_number_less_if_val_in_tree(self):
        self.assertEqual(self.tree.lower(6), 5)
        self.assertEqual(self.tree.lower(3), 2)

    def test_lower_raises_value_error_if_val_not_present(self):
        with self.assertRaises(ValueError):
            self.tree.lower(1)

    def test_lower_raises_value_error_if_val_is_lowest_value(self):
        with self.assertRaises(ValueError):
            self.tree.lower(2)


if __name__ == '__main__':
    unittest.main()
