from typing import List
import unittest

class ExamRoom:
    def __init__(self,n):
        self.arr:List[int] = []
        self.n:int = n
    
    def seat(self)->int:
        if not self.arr:
            self.arr.append(0)
            return 0
        seat = 0
        max_distance = self.arr[0]
        for i in range(len(self.arr)-1):
            seat_1 = self.arr[i]
            seat_2 = self.arr[i+1]
            dist = (seat_2-seat_1)//2
            if dist > max_distance:
                seat = (seat_1 + seat_2)//2
                max_distance = dist

        if (self.n-1 - self.arr[-1]) > max_distance:
            seat = self.n - 1
        self.arr.append(seat)
        self.arr.sort()
        return seat

    
    def leave(self, i:int):
        self.arr.remove(i)


class TestExamRoom(unittest.TestCase):

    def test_basic_seating(self):
        room = ExamRoom(10)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 9)
        self.assertEqual(room.seat(), 4)
        self.assertEqual(room.seat(), 2)

    def test_leave_and_reseat(self):
        room = ExamRoom(10)
        room.seat()
        room.seat()
        room.seat()
        room.seat()
        room.leave(4)
        self.assertEqual(room.seat(), 5)

    def test_single_seat(self):
        room = ExamRoom(1)
        self.assertEqual(room.seat(), 0)

    def test_two_seats(self):
        room = ExamRoom(2)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 1)

    def test_multiple_leaves(self):
        room = ExamRoom(10)
        room.seat()
        room.seat()
        room.seat()
        room.leave(0)
        self.assertEqual(room.seat(), 0)

    def test_leave_from_middle(self):
        room = ExamRoom(10)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 9)
        self.assertEqual(room.seat(), 4)
        room.leave(4)
        self.assertEqual(room.seat(), 4)

    def test_sequential_seating(self):
        room = ExamRoom(4)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 3)
        self.assertEqual(room.seat(), 1)
        self.assertEqual(room.seat(), 2)

    def test_edge_preference(self):
        room = ExamRoom(8)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 7)
        self.assertEqual(room.seat(), 3)

    def test_large_room(self):
        room = ExamRoom(100)
        self.assertEqual(room.seat(), 0)
        self.assertEqual(room.seat(), 99)
        self.assertEqual(room.seat(), 49)
        self.assertEqual(room.seat(), 74)
        self.assertEqual(room.seat(), 24)

    def test_empty_room_after_leaves(self):
        room = ExamRoom(5)
        room.seat()
        room.seat()
        room.leave(0)
        room.leave(4)
        self.assertEqual(room.seat(), 0)


if __name__ == '__main__':
    unittest.main()

