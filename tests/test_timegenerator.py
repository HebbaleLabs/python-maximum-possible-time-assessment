import unittest
from delayed_assert import expect, assert_expectations
from timegenerator import generate_max_time

class TimeGeneratorTest(unittest.TestCase):

  # For verifying date times that have 0 as leading digit in hour
  def test_generateMaxTimePreNoonTimes(self):
    expect(lambda: self.assertEqual(generate_max_time([0,5,8,4]), '08:54'))
    expect(lambda: self.assertEqual(generate_max_time([0,7,6,4]), '07:46'))
    assert_expectations()

  # For verifying date times that have 1,2 as leading digit in hour
  def test_generateMaxTimePostNoonTimes(self):
    expect(lambda: self.assertEqual(generate_max_time([1,2,5,9]), '21:59'))
    expect(lambda: self.assertEqual(generate_max_time([1,3,7,4]), '17:43'))
    expect(lambda: self.assertEqual(generate_max_time([1,4,1,3]), '14:41'))
    expect(lambda: self.assertEqual(generate_max_time([2,9,1,9]), '19:29'))
    expect(lambda: self.assertEqual(generate_max_time([2,1,1,2]), '21:21'))
    expect(lambda: self.assertEqual(generate_max_time([3,1,1,3]), '13:31'))
    assert_expectations()

  # For verifying date times where the hour digits will be populated
  def test_generateMaxTimeHourBoundaries(self):
    expect(lambda: self.assertEqual(generate_max_time([0,3,0,0]), '03:00'))
    expect(lambda: self.assertEqual(generate_max_time([0,9,0,0]), '09:00'))
    expect(lambda: self.assertEqual(generate_max_time([0,0,0,1]), '10:00'))
    expect(lambda: self.assertEqual(generate_max_time([0,0,0,2]), '20:00'))
    expect(lambda: self.assertEqual(generate_max_time([2,3,0,0]), '23:00'))
    assert_expectations()

  # For verifying date times where the minute digits will also be populated
  def test_generateMaxTimeMinuteBoundaries(self):
    expect(lambda: self.assertEqual(generate_max_time([3,3,0,0]), '03:30'))
    expect(lambda: self.assertEqual(generate_max_time([0,9,9,0]), '09:09'))
    expect(lambda: self.assertEqual(generate_max_time([0,1,1,1]), '11:10'))
    expect(lambda: self.assertEqual(generate_max_time([2,3,0,2]), '23:20'))
    assert_expectations()

  # For verifying the boundary conditions
  def test_generateMaxTimeBoundaryTests(self):
    expect(lambda: self.assertEqual(generate_max_time([0,0,0,0]), '00:00'))
    expect(lambda: self.assertEqual(generate_max_time([2,3,5,9]), '29:59'))
    assert_expectations()

  # For verifying if the method returns None for input digits that are out of range
  def test_generateMaxTimeOutOfRangeInputs(self):
    expect(lambda: self.assertEqual(generate_max_time([9,9,9,9]), None))
    expect(lambda: self.assertEqual(generate_max_time([5,6,9,9]), None))
    expect(lambda: self.assertEqual(generate_max_time([1,6,9,9]), None))
    expect(lambda: self.assertEqual(generate_max_time([9,2,8,9]), None))
    expect(lambda: self.assertEqual(generate_max_time([7,3,8,2]), None))
    expect(lambda: self.assertEqual(generate_max_time([6,2,3,7]), None))
    assert_expectations()

  # For verifying if the method returns None for input digits that are negative
  def test_generateMaxTimeInvalidInputs(self):
    expect(lambda: self.assertEqual(generate_max_time([-9,9,9,9]), None))
    expect(lambda: self.assertEqual(generate_max_time([1,2,-9,4]), None))
    expect(lambda: self.assertEqual(generate_max_time([11,12,1,2]), None))
    assert_expectations()