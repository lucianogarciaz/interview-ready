import bisect
from typing import List
import unittest
class MyCalendar:
    def __init__(self):
        self.start:List[int] = []
        self.end:List[int] = []

        """
        10  30
        20  40
        s 15 e 35
        """
    def book(self, start: int, end:int)->bool:
        i = bisect.bisect_left(self.start, start)
        if i >0 and start < self.end[i-1]:
            return False
        if i < len(self.start) and self.start[i] < end:
            return False
        
        self.start.insert(i,start)
        self.end.insert(i,end)
        return True

class TestMyCalendar(unittest.TestCase):
    def test_single_booking(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
    
    def test_non_overlapping_bookings(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(30, 40))
    
    def test_overlapping_same_start(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(10, 25))
    
    def test_overlapping_within_existing(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 30))
        self.assertFalse(cal.book(15, 25))
    
    def test_overlapping_start_before_end_after(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(20, 30))
        self.assertFalse(cal.book(15, 35))
    
    def test_overlapping_at_boundary_before(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(20, 30))
        self.assertFalse(cal.book(15, 25))
    
    def test_overlapping_at_boundary_after(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
    
    def test_multiple_bookings_with_failures(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))
        self.assertFalse(cal.book(5, 15))
        self.assertTrue(cal.book(5, 10))
        self.assertTrue(cal.book(30, 40))
    
    def test_booking_before_existing(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(5, 10))
    
    def test_edge_case_adjacent_bookings(self):
        cal = MyCalendar()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(0, 10))
        self.assertTrue(cal.book(30, 40))

if __name__ == '__main__':
    unittest.main()