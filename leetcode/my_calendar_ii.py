import bisect
import unittest

class MyCalendar2:
    def __init__(self):
        self.booking = []
        self.overlaps = []
    def book(self, start: int, end:int)->bool:
        i = bisect.bisect_left(self.overlaps,(start,end))
        if i>0:
            prevStart,prevEnd = self.overlaps[i-1]
            if prevEnd > start:
                return False
        if len(self.overlaps) >i:
            nextStart,nextEnd = self.overlaps[i]
            if nextStart < end:
                return False
        # add new overlaps
        for s,e in self.booking:
            if s < end and e>start:
                newStart, newEnd = max(s,start), min(end,e)
                i = bisect.bisect_left(self.overlaps,(newStart,newEnd))
                self.overlaps.insert(i, (newStart,newEnd))

        self.booking.append((start,end))
        return True

class TestMyCalendar2(unittest.TestCase):
    def test_single_booking(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
    
    def test_double_booking_allowed(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(15, 25))
    
    def test_triple_booking_rejected(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(15, 25))
        self.assertFalse(cal.book(17, 22))
    
    def test_non_overlapping_bookings(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(30, 40))
    
    def test_leetcode_example_1(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(50, 60))
        self.assertTrue(cal.book(10, 40))
        self.assertFalse(cal.book(5, 15))
        self.assertTrue(cal.book(5, 10))
        self.assertTrue(cal.book(25, 55))
    
    def test_double_booking_same_start(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(10, 20))
        self.assertFalse(cal.book(10, 20))
    
    def test_double_booking_partial_overlap_left(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(10, 25))
        self.assertTrue(cal.book(5, 15))
        self.assertFalse(cal.book(12, 22))
    
    def test_double_booking_partial_overlap_right(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(15, 30))
        self.assertTrue(cal.book(25, 35))
        self.assertFalse(cal.book(17, 27))
    
    def test_double_booking_contained(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 40))
        self.assertTrue(cal.book(20, 30))
        self.assertFalse(cal.book(22, 28))
    
    def test_double_booking_containing(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(10, 40))
        self.assertFalse(cal.book(15, 35))
    
    def test_multiple_double_bookings_no_triple(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(30, 40))
        self.assertTrue(cal.book(15, 25))
        self.assertTrue(cal.book(25, 35))
    
    def test_edge_case_adjacent_to_overlap(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(15, 25))
        self.assertTrue(cal.book(20, 30))
        self.assertTrue(cal.book(5, 15))
    
    def test_complex_scenario(self):
        cal = MyCalendar2()
        self.assertTrue(cal.book(10, 20))
        self.assertTrue(cal.book(50, 60))
        self.assertTrue(cal.book(10, 40))
        self.assertTrue(cal.book(5, 10))
        self.assertFalse(cal.book(5, 15))
        self.assertTrue(cal.book(50, 55))
        self.assertFalse(cal.book(45, 55))

if __name__ == '__main__':
    unittest.main()