#!/usr/bin/env python

import unicornhat as unicorn
import time, colorsys
import numpy as np
import random

unicorn.brightness(0.2)

def light(h,s,v):
	for y in range(8):
		for x in range(8):
			h = h
			s = s
			v = v
			rgb = colorsys.hsv_to_rgb(h, s, v)
			r = int(rgb[0]*255.0)
			g = int(rgb[1]*255.0)
			b = int(rgb[2]*255.0)
			unicorn.set_pixel(x, y, r, g, b)
	unicorn.show()

while True:
	light(0.1,1,1)
	time.sleep(random.random()/random.randint(5,10))
	light(0,0,0)
	time.sleep(random.random()/random.randint(5,10))
