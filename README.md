# django_unit_testing
=====================

Exploring the django unit testing.

In Django testing, assertions are used to verify the expected behavior of your code. Below is a list of common assertions used in Django's `TestCase` class.

## 1. **Equality Checks**

- **`assertEqual(a, b)`**  
  Verifies that `a` and `b` are equal.  
  Example:  
  `self.assertEqual(1 + 1, 2)`

- **`assertNotEqual(a, b)`**  
  Verifies that `a` and `b` are not equal.  
  Example:  
  `self.assertNotEqual(1 + 1, 3)`

- **`assertAlmostEqual(a, b, places=7)`**  
  Verifies that `a` and `b` are approximately equal up to a given number of decimal places.  
  Example:  
  `self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)`

- **`assertNotAlmostEqual(a, b, places=7)`**  
  Verifies that `a` and `b` are not approximately equal up to a given number of decimal places.  
  Example:  
  `self.assertNotAlmostEqual(0.1 + 0.2, 0.4, places=7)`

## 2. **Boolean Checks**

- **`assertTrue(x)`**  
  Verifies that `x` is `True`.  
  Example:  
  `self.assertTrue(1 + 1 == 2)`

- **`assertFalse(x)`**  
  Verifies that `x` is `False`.  
  Example:  
  `self.assertFalse(1 + 1 == 3)`

## 3. **Container Checks**

- **`assertIn(member, container)`**  
  Verifies that `member` is in `container`.  
  Example:  
  `self.assertIn('banana', ['apple', 'banana', 'cherry'])`

- **`assertNotIn(member, container)`**  
  Verifies that `member` is not in `container`.  
  Example:  
  `self.assertNotIn('grape', ['apple', 'banana', 'cherry'])`

## 4. **Exception Checks**

- **`assertRaises(exception, callable, *args, **kwargs)`**  
  Verifies that calling `callable` with `*args` and `**kwargs` raises the specified `exception`.  
  Example:  
  `with self.assertRaises(ValueError):`  
  `    int("abc")`

## 5. **Object Identity Checks**

- **`assertIs(a, b)`**  
  Verifies that `a` and `b` are the same object.  
  Example:  
  `self.assertIs(a, b)`  

- **`assertIsNot(a, b)`**  
  Verifies that `a` and `b` are not the same object.  
  Example:  
  `self.assertIsNot(a, b)`  

- **`assertIsNone(x)`**  
  Verifies that `x` is `None`.  
  Example:  
  `self.assertIsNone(None)`

- **`assertIsNotNone(x)`**  
  Verifies that `x` is not `None`.  
  Example:  
  `self.assertIsNotNone("hello")`

## 6. **Type Checks**

- **`assertIsInstance(obj, cls)`**  
  Verifies that `obj` is an instance of class `cls`.  
  Example:  
  `self.assertIsInstance(42, int)`

- **`assertNotIsInstance(obj, cls)`**  
  Verifies that `obj` is not an instance of class `cls`.  
  Example:  
  `self.assertNotIsInstance(42, str)`

## 7. **Numerical Comparisons**

- **`assertGreater(a, b)`**  
  Verifies that `a` is greater than `b`.  
  Example:  
  `self.assertGreater(5, 3)`

- **`assertGreaterEqual(a, b)`**  
  Verifies that `a` is greater than or equal to `b`.  
  Example:  
  `self.assertGreaterEqual(5, 5)`

- **`assertLess(a, b)`**  
  Verifies that `a` is less than `b`.  
  Example:  
  `self.assertLess(3, 5)`

- **`assertLessEqual(a, b)`**  
  Verifies that `a` is less than or equal to `b`.  
  Example:  
  `self.assertLessEqual(3, 5)`

## 8. **Element Count Comparison**

- **`assertCountEqual(a, b)`**  
  Verifies that `a` and `b` have the same elements, regardless of order.  
  Example:  
  `self.assertCountEqual([1, 2, 3], [3, 2, 1])`

---