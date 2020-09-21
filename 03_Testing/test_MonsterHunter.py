import unittest
import time
import os
import threading
from queue import Queue

from MonsterHunter_Test import start_game

class TestAssociation(unittest.TestCase):
	""" The methods in the class are the test cases"""
	
	def test_usercommand_go_01(self):
		"""
		to test if the user command to start the game
		"""
		
		user_input = 'go'
		q = Queue()
		
		expected_status , expected_game_status = start_game(user_input , q)
		correct_status = 'Monster attack started'
		
		self.assertEqual(expected_status , correct_status)
		
		
	def test_usercommand_end_02(self):
		"""
		to test if the user command to end the game
		"""
		
		user_input = 'end'
		q = Queue()
		
		expected_status , expected_game_status = start_game(user_input , q)
		correct_status = 'You exitted the game'
		
		self.assertEqual(expected_status , correct_status)
		
		
	def test_usercommand_random_03(self):
		"""
		to test if the user command is incorrect
		"""
		
		user_input = 'yes'
		q = Queue()
		
		expected_status , expected_game_status = start_game(user_input , q)
		correct_status = 'Invalid input. Please enter go to start the game or Enter end to exit game.'
		
		self.assertEqual(expected_status , correct_status)
		
		
	def test_game_lost_04(self):
		"""
		to test the end of the game with playing loosing
		"""
		
		user_input = 'go'
		q = Queue()
		q.put('attack orc')
		
		
		expected_status , expected_game_status = start_game(user_input , q)
		correct_game_status = 0
		
		self.assertEqual(expected_game_status , correct_game_status)
		
		
	def test_game_win_05(self):
		"""
		to test the end of the game with playing winning
		"""
		
		user_input = 'go'
		q = Queue()
		q.put('attack orc')
		q.put('attack dragon')
		
		expected_status , expected_game_status = start_game(user_input , q)
		correct_game_status = 0
		
		self.assertEqual(expected_game_status , correct_game_status)
		
		
	
		
		
		
if __name__ == '__main__':
    unittest.main()