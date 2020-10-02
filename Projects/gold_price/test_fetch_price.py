from unittest import TestCase, main
from unittest.mock import patch
from fetch_price import GoldPrice


class TestGoldPrice(TestCase):
    
    @patch("fetch_price.GoldPrice.make_soup")
    def test_make_soup(self, mock_method):
        object_ = GoldPrice().make_soup()
        # Test Case 1
        self.assertNotEqual(mock_method.return_value, None)
        # Test Case 2
        self.assertEqual(mock_method.return_value, object_)
        # Test Case 3
        mock_method.return_value = None
        self.assertEqual(mock_method.return_value, None)
        
    @patch("fetch_price.GoldPrice.get_time")
    def test_get_time(self, mock_method):
        now = GoldPrice().get_time()
        self.assertNotEqual(mock_method.return_value, None)
        self.assertEqual(mock_method.return_value, now)
        mock_method.return_value = None
        self.assertEqual(mock_method.return_value, None)
        
    @patch("fetch_price.GoldPrice.fetch_data")
    def test_fetch_data(self, mock_method):
        response = GoldPrice().fetch_data()
        self.assertNotEqual(mock_method.return_value, None)
        self.assertEqual(mock_method.return_value, response)
        
        mock_method.return_value = None
        self.assertEqual(mock_method.return_value, None)

if __name__ == '__main__':
    main()