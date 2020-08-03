import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote["stock"], quote["top_bid"]["price"], quote["top_ask"]["price"], (quote["top_bid"]["price"] + quote["top_ask"]["price"])/2 ))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculate_ratio(self):
    prices = [
      {"price_a": 10.0, "price_b": 3.1},
      {"price_a": 3.1, "price_b": 3.2},
      {"price_a": 3, "price_b": 10},
      {"price_a": 0, "price_b": 3},
    ]
    
    for price in prices:
      self.assertEqual(getRatio(**price), price["price_a"]/price["price_b"])

  def test_getRatio_calculate_ratio_zero_division(self):
    prices = [
      {"price_a": 10.0, "price_b": 0},
      {"price_a": 3.1, "price_b": 0},
      {"price_a": 3, "price_b": 0},
      {"price_a": 0, "price_b": 0},
    ]
    
    for price in prices:
      self.assertEqual(getRatio(**price), None)


if __name__ == '__main__':
    unittest.main()
