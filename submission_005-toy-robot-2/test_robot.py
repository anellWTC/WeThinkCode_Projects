import unittest
from unittest.mock import patch
from robot import help_command, move_forward, move_backward, sprint, move_left, move_right
import sys
from io import StringIO

class test_robot(unittest.TestCase):
    def test_get_help(self):
        sys.stdout = StringIO()
        help_command()
        self.assertEqual(sys.stdout.getvalue(),"""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
""")
    def test_move(self):
        self.assertEqual(move_forward("HAL","forward 5","front",0,0),(0,5))
        # def move_forward(name, command,current_position,x,y):
    
    def test_back(self):
        self.assertEqual(move_backward("HAL","back 5","front",0,0),(0,-5))
        # def move_backward(name, command,current_position,x,y):    
    def test_left(self):
        self.assertEqual(move_left("HAL",0,8,"left","front"),(0,8))
        # def move_left(name,x,y,command,current_position):
    
    def test_right(self):
        self.assertEqual(move_right("HAL",0,8,"right","right"),(0,8))
        # def move_right(name,x,y,command,current_position):

    def test_sprint(self):
        self.assertEqual(sprint("HAL","sprint 5","front",0,0),(0,15))
        # def sprint(name, command,current_position,x,y):
if __name__ == "__main__":
    unittest.main()