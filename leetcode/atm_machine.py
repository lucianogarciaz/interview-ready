from typing import List
import unittest
# withdraw y deposit. 
# 20,50,100,200,500   /3200/500
# [0, 0, 0,  4,  11] -- balance. 
# 800 
# [0, 0, 9,  0,  2] = [0,0,1,0,3]
class ATM:
    def __init__(self):
        self.balance = {}
        self.bill = {0:20, 1:50, 2:100, 3:200, 4:500}
    def deposit(self, notes: List[int])->None:
        if not self.balance:
            self.balance = [0] * 5
        for i, val in enumerate(notes):
            self.balance[i] += val
    def withdraw(self, amount:int)->List[int]:
        if not self.balance:
            return [-1]
        
        res:List[int] = [0] * 5
        balance_copy = self.balance.copy()
        
        for i in range(4, -1, -1):
            bill_note = self.bill[i]
            if amount >= bill_note * balance_copy[i]:
                res[i] = balance_copy[i]
                amount -= bill_note * balance_copy[i]
                balance_copy[i] = 0
            else:
                nro_of_bills = amount//bill_note
                res[i] = nro_of_bills
                balance_copy[i] -= nro_of_bills
                amount -= bill_note*nro_of_bills
        if amount!= 0:
            return [-1]
        self.balance = balance_copy
        return res

class TestATM(unittest.TestCase):
    
    def test_basic_example_from_problem(self):
        atm = ATM()
        
        atm.deposit([0, 0, 1, 2, 1])
        self.assertEqual(atm.withdraw(600), [0, 0, 1, 0, 1])
        
        atm.deposit([0, 1, 0, 1, 1])
        self.assertEqual(atm.withdraw(600), [-1])
        
        self.assertEqual(atm.withdraw(550), [0, 1, 0, 0, 1])
    
    def test_withdraw_from_empty_atm(self):
        atm = ATM()
        self.assertEqual(atm.withdraw(100), [-1])
    
    def test_simple_deposit_and_withdraw(self):
        atm = ATM()
        atm.deposit([1, 0, 0, 0, 0])
        self.assertEqual(atm.withdraw(20), [1, 0, 0, 0, 0])
    
    def test_exact_amount_withdrawal(self):
        atm = ATM()
        atm.deposit([2, 2, 2, 2, 2])
        self.assertEqual(atm.withdraw(1540), [2, 0, 1, 2, 2])
    
    def test_prioritize_larger_denominations(self):
        atm = ATM()
        atm.deposit([5, 5, 5, 5, 5])
        result = atm.withdraw(500)
        self.assertEqual(result, [0, 0, 0, 0, 1])
    
    def test_multiple_deposits(self):
        atm = ATM()
        atm.deposit([1, 1, 1, 1, 1])
        atm.deposit([1, 1, 1, 1, 1])
        self.assertEqual(atm.withdraw(1540), [2, 0, 1, 2, 2])
    
    def test_insufficient_funds(self):
        atm = ATM()
        atm.deposit([1, 0, 0, 0, 0])
        self.assertEqual(atm.withdraw(50), [-1])
    
    def test_cannot_make_exact_change(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 0, 1])
        self.assertEqual(atm.withdraw(100), [-1])
    
    def test_greedy_fails_but_solution_exists(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 3, 1])
        self.assertEqual(atm.withdraw(600), [-1])
    
    def test_large_withdrawal(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 0, 10])
        self.assertEqual(atm.withdraw(5000), [0, 0, 0, 0, 10])
    
    def test_mixed_denominations(self):
        atm = ATM()
        atm.deposit([2, 2, 2, 2, 2])
        result = atm.withdraw(720)
        self.assertEqual(result, [1, 0, 0, 1, 1])
    
    def test_balance_updates_after_withdrawal(self):
        atm = ATM()
        atm.deposit([5, 5, 5, 5, 5])
        atm.withdraw(500)
        result = atm.withdraw(500)
        self.assertEqual(result, [0, 0, 0, 0, 1])
    
    def test_balance_not_updated_on_failed_withdrawal(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 0, 1])
        atm.withdraw(100)
        result = atm.withdraw(500)
        self.assertEqual(result, [0, 0, 0, 0, 1])
    
    def test_withdraw_all_smallest_denomination(self):
        atm = ATM()
        atm.deposit([10, 0, 0, 0, 0])
        self.assertEqual(atm.withdraw(200), [10, 0, 0, 0, 0])
    
    def test_multiple_withdrawals_sequence(self):
        atm = ATM()
        atm.deposit([10, 10, 10, 10, 10])
        
        self.assertEqual(atm.withdraw(500), [0, 0, 0, 0, 1])
        self.assertEqual(atm.withdraw(200), [0, 0, 0, 1, 0])
        self.assertEqual(atm.withdraw(100), [0, 0, 1, 0, 0])
        self.assertEqual(atm.withdraw(50), [0, 1, 0, 0, 0])
        self.assertEqual(atm.withdraw(20), [1, 0, 0, 0, 0])

    def test_zero_amount_deposits(self):
        atm = ATM()
        atm.deposit([0, 0, 0, 0, 0])
        self.assertEqual(atm.withdraw(20), [-1])

    def test_withdraw_requiring_all_denominations(self):
        atm = ATM()
        atm.deposit([1, 1, 1, 1, 1])
        self.assertEqual(atm.withdraw(870), [1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()