#!/usr/bin/env python3
from pyglet.gl import *

ShowAds = True
pStatus = False

ver = "SIMP 15.07 ALPHA"

window = pyglet.window.Window(1000, 600, resizable=True, caption = ver)
icon = pyglet.image.load("Resources/icon.png")
buttons = pyglet.image.load("Resources/playerbuttons.png")
play = pyglet.image.load("Resources/play.png")
window.set_icon(icon)
window.push_handlers(pyglet.window.event.WindowEventLogger())
window.set_minimum_size(640, 480)

#=============================Functions=================================
def cpStatus():
	global pStatus
	if pStatus == True:
			pStatus2 = False
	if pStatus == False:
		pStatus2 = True
	pStatus = pStatus2

def rectCheck(lista, listb, listc):
	if listc[0] >= lista[0] and listc[0] <= listb[0] and listc[1] >= lista[1] and listc[1] <= listb[1]:
		return True
	else:
		return False

#=============================Code======================================
@window.event
def on_draw():
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) 
	glClearColor(0.04, 0.04, 0.04, 0.0)
	window.clear()
	glLoadIdentity()
	glShadeModel(GL_SMOOTH)
	#Player
	glBegin(GL_POLYGON)
	glColor3f(0.02, 0.02, 0.02)
	glVertex2f(150, window.height - 150)
	glVertex2f(150, window.height)
	glVertex2f(window.width, window.height)
	glVertex2f(window.width, window.height - 150)
	glEnd()
	glBegin(GL_POLYGON)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(150, window.height - 120)
	glVertex2f(150, window.height)
	glColor3f(0.0, 0.0, 0.8)
	glVertex2f(window.width, window.height)
	glVertex2f(window.width, window.height - 120)
	glEnd()
	pyglet.text.Label(ver, font_name='Times New Roman', anchor_x = "right", font_size=8, x=window.width - 2, y=window.height - 115).draw()
	#Player Buttons
	glColor3f(1.0, 1.0, 1.0)
	buttons.blit(250, window.height - 100)
	if pStatus == True:
		play.blit(298, window.height - 100)
	#Player Time
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glVertex2f(425, window.height - 70)
	glVertex2f(window.width - 20, window.height - 70)
	glEnd()
	glColor3f(0.0, 0.2, 1.0)
	glLineWidth(3.0)
	glBegin(GL_LINES)
	glVertex2f(423, window.height - 70)
	glVertex2f(window.width - 120, window.height - 70)
	glEnd()
	#Playlists Bar
	glBegin(GL_POLYGON)
	glColor3f(0.0, 0.0, 0.6)
	glVertex2f(0, 0)
	glVertex2f(0, window.height)
	glColor3f(0.2, 0.2, 0.2)
	glVertex2f(200, window.height)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(200, 0)
	glEnd()
	#Playlists Header
	glBegin(GL_POLYGON)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(0, window.height - 30)
	glVertex2f(0, window.height)
	glVertex2f(200, window.height)
	glVertex2f(200, window.height - 30)
	glEnd()
	#playlists Menu
	glBegin(GL_POLYGON)
	glColor3f(0.0, 0.0, 0.1)
	glVertex2f(5, 250)
	glVertex2f(5, window.height - 35)
	glVertex2f(195, window.height - 35)
	glVertex2f(195, 250)
	glEnd()
	glBegin(GL_LINES)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(10, 280)
	glVertex2f(190, 280)
	glEnd()
	glBegin(GL_POLYGON)
	glColor4f(0.0, 0.0, 0.0, 0.5)
	glVertex2f(5, 250)
	glVertex2f(5, 279)
	glVertex2f(195, 280)
	glVertex2f(195, 250)
	glEnd()
	#New Playlist Label
	pyglet.text.Label("New Playlist", font_name = "Times New Roman", font_size = 10, x = 65, y = 260).draw()
	#Playlists Label
	pyglet.text.Label("Playlists", font_name="Times New Roman", font_size = 14, x = 70, y = window.height - 22).draw()
	#Playlist
	glLineWidth(2.0)
	a = window.height - 150
	while a >= 40:
		a = a - 40
		glBegin(GL_LINES)
		glColor3f(0.01, 0.01, 0.01)
		glVertex2f(220, a)
		glColor3f(0.02, 0.02, 0.02)
		glVertex2f(window.width - 20, a)
		glEnd()
	#Flush
	glFlush()

@window.event
def on_mouse_press(x, y, button, mods):
	if rectCheck([300, window.height - 101], [364, window.height - 37], [x, y]) == True:	
		cpStatus()

@window.event
def on_text(text):
	if text == " ":
		cpStatus()

pyglet.app.run()
