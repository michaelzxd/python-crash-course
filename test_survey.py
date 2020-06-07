#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""docstring for TestAnonymousSurvey"""
	def setUp(self):
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Chinese','French']
		

	def test_store_single_response(self):
		
		
		self.my_survey.store_response(self.responses[0])

		self.assertIn(self.responses[0],self.my_survey.responses)

	def test_store_three_responses(self):
		
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)

unittest.main()
