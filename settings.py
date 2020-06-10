#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Settings():
	"""docstring for Settings"""
	def __init__(self):
		
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 18.5

		self.bullet_speed_factor = 15
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 300
		self.alien_speed_factor = 1

		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		self.ship_limit = 3

