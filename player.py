#!/usr/bin/env python3

#Please use this to disable advertisements. It's a great way to keep
#from screwing supporters by unintentionally mishandling code. Not to
#mention, it's SUPER easy!

PlayAds = True

import pyglet
pyglet.options["debug_gl"] = False
pyglet.options["shadow_window"] = False
from pyglet.gl import *
from os import listdir, system, mkdir
from os.path import dirname
from pyglet.window import key
from json import dumps, loads

ver = "SIMP 15.09 ALPHA"

window = pyglet.window.Window(1000, 600, resizable = True, caption = ver, vsync = False)
window.push_handlers(pyglet.window.event.WindowEventLogger())
# ^ Uncomment for testing
icon = pyglet.image.load("Resources/icon.png")
buttons = pyglet.image.load("Resources/playerbuttons.png")
play = pyglet.image.load("Resources/play.png")
window.set_icon(icon)
window.push_handlers()
window.set_minimum_size(640, 480)
pyglet.font.add_file("Resources/UbuntuMono-R.ttf")
uMono = pyglet.font.load("Ubuntu Mono")
ClickClock = pyglet.clock.Clock()
ClickClock.update_time()
#=============================Variables=================================
pStatus = False

mode = "PLAYER"

playlists = []
playlistLocation = 0

plSelected = ""
plCurrent = ""

nplname = ""
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

def plRefresh():
	global playlists
	if "Playlists" not in listdir():
		mkdir("Playlists")
	if "Cache" not in listdir():
		mkdir("Cache")
	playlists = sorted(listdir("Playlists"))

def npl(name):
	fob = open("Playlists/" + name, "a")
	fob.close()

def nplnameseg():
	global nplname
	if len(nplname) > 16:
		return nplname[-16:]
	else:
		return nplname

def menItem(y1, y2, y3, step):
	y2 -= y1
	y3 -= y1
	count = -1
	while y2 > 0:
		if y3 < y2:
			count += 1
		y2 -= step
	return count
			
#-----------------------------Lists' Functions--------------------------
def retPlaylist():
	global playlistLocation
	return playlists[playlistLocation:playlistLocation + int(((window.height - 315) / 20))]
#-----------------------------Bittorrent Functions----------------------
def download(magnet):
	system("transmission-cli -er -m -w cache " + magnet)
#=============================Code======================================
plRefresh()

@window.event
def on_draw():
	global mode, nplname
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
	buttons.blit(220, window.height - 100)
	if pStatus == True:
		play.blit(268, window.height - 100)
	#Player Time
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glVertex2f(400, window.height - 70)
	glVertex2f(window.width - 20, window.height - 70)
	glEnd()
	glColor3f(0.0, 0.2, 1.0)
	glLineWidth(3.0)
	glBegin(GL_LINES)
	glVertex2f(399, window.height - 70)
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
	#playlists' Menu
	glBegin(GL_POLYGON)
	glColor3f(0.0, 0.0, 0.05)
	glVertex2f(5, 250)
	glVertex2f(5, window.height - 35)
	glVertex2f(195, window.height - 35)
	glVertex2f(195, 250)
	glEnd()
	#Playlists Items
	a = window.height - 40
	for entry in retPlaylist():
		if entry == plSelected:
			glBegin(GL_POLYGON)
			glColor3f(0.0, 0.0, 0.8)
			glVertex2f(5, a - 19)
			glVertex2f(5, a + 1)
			glVertex2f(195, a + 1)
			glVertex2f(195, a - 19)
			glEnd()
		pyglet.text.Label(entry, font_name = "Ubuntu Mono", font_size = 12, x = 10, y = a, anchor_x = "left", anchor_y = "top").draw()
		a -= 20
	#New Playlist Button
	glBegin(GL_LINES)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(10, 275)
	glVertex2f(190, 275)
	glEnd()
	glBegin(GL_POLYGON)
	glColor3f(0.18, 0.18, 0.18)
	glVertex2f(5, 245)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(5, 274)
	glVertex2f(195, 275)
	glColor3f(0.18, 0.18, 0.18)
	glVertex2f(195, 245)
	glEnd()
	#New Playlist Label
	pyglet.text.Label("New Playlist", font_name = "Times New Roman", font_size = 10, x = 65, y = 255).draw()
	#Playlists Label
	pyglet.text.Label("Playlists", font_name="Times New Roman", font_size = 14, x = 70, y = window.height - 22).draw()
	#Playlist
	glLineWidth(2.0)
	a = window.height - 150
	while a >= 40:
		a -= 40
		glBegin(GL_LINES)
		glColor3f(0.01, 0.01, 0.01)
		glVertex2f(220, a)
		glColor3f(0.02, 0.02, 0.02)
		glVertex2f(window.width - 20, a)
		glEnd()
	#NPL Box
	if mode == "NPL":
		glBegin(GL_POLYGON)
		glColor3f(0.0, 0.0, 0.0)
		glVertex2f((window.width / 2) - 163, (window.height / 2) - 103)
		glVertex2f((window.width / 2) - 163, (window.height / 2) + 103)
		glVertex2f((window.width / 2) + 163, (window.height / 2) + 103)
		glVertex2f((window.width / 2) + 163, (window.height / 2) - 103)
		glEnd()
		glBegin(GL_POLYGON)
		glColor3f(0.0, 0.0, 0.3)
		glVertex2f((window.width / 2) - 160, (window.height / 2) - 100)
		glVertex2f((window.width / 2) - 160, (window.height / 2) + 100)
		glVertex2f((window.width / 2) + 160, (window.height / 2) + 100)
		glColor3f(0.0, 0.0, 0.1)
		glVertex2f((window.width / 2) + 160, (window.height / 2) - 100)
		glEnd()
		#NPL Name Box
		glBegin(GL_POLYGON)
		glColor3f(0.0, 0.0, 0.0)
		glVertex2f((window.width / 2) - 152, (window.height / 2) + 20)
		glVertex2f((window.width / 2) - 152, (window.height / 2) + 62)
		glVertex2f((window.width / 2) + 152, (window.height / 2) + 62)
		glVertex2f((window.width / 2) + 152, (window.height / 2) + 20)
		glEnd()
		glBegin(GL_POLYGON)
		glColor3f(0.04, 0.04, 0.04)
		glVertex2f((window.width / 2) - 150, (window.height / 2) + 20)
		glVertex2f((window.width / 2) - 150, (window.height / 2) + 60)
		glVertex2f((window.width / 2) + 150, (window.height / 2) + 60)
		glVertex2f((window.width / 2) + 150, (window.height / 2) + 20)
		glEnd()
		glBegin(GL_POLYGON)
		glColor3f(0.1, 0.1, 0.1)
		glVertex2f((window.width / 2) - 150, (window.height / 2) - 80)
		glColor3f(0.0, 0.0, 0.0)
		glVertex2f((window.width / 2) - 150, (window.height / 2) - 30)
		glVertex2f((window.width / 2) + 150, (window.height / 2) - 30)
		glColor3f(0.18, 0.18, 0.18)
		glVertex2f((window.width / 2) + 150, (window.height / 2) - 80)
		glEnd()
		pyglet.text.Label(nplnameseg(), font_name="Times New Roman", font_size = 20, x = (window.width / 2) - 145, y = (window.height / 2) + 25, anchor_x = "left", anchor_y = "bottom").draw()
		pyglet.text.Label(str(len(nplname)) + "/22", font_name="Times New Roman", font_size = 8, x = (window.width / 2) + 145, y = (window.height / 2) - 10, anchor_x = "right", anchor_y = "bottom").draw()
		pyglet.text.Label("OK", font_name="Times New Roman", font_size = 20, x = (window.width / 2), y = (window.height / 2) - 55, anchor_x = "center", anchor_y = "center").draw()
	#Flush
	glFlush()

@window.event
def on_mouse_press(x, y, button, mods):
	global mode, nplname, plSelected, plCurrent
	c = ClickClock.update_time()
	if mode == "PLAYER":
		if rectCheck([270, window.height - 100], [330, window.height - 36], [x, y]):	
			cpStatus()
		if rectCheck([5, 250], [195, 280], [x, y]):
			mode = "NPL"
		if rectCheck([5, 280], [195, window.height - 35], [x, y]):
			plSelected = retPlaylist()[menItem(280, window.height - 35, y, 20)]
			if c < .5:
				plCurrent = plSelected
				if pStatus == False:
					cpStatus()
	if mode == "NPL":
		if rectCheck([(window.width / 2) - 150, (window.height / 2) - 80], [(window.width / 2) + 150, (window.height / 2) - 30], [x, y]):
			if nplname != "":
				npl(nplname)
			nplname = ""
			mode = "PLAYER"

@window.event
def on_text(text):
	global nplname, mode
	if mode == "PLAYER":
		if text == " ":
			cpStatus()
	if mode == "NPL":
		if text not in ["\r", "/", "\\", "\"", ".", "`", "~", "<", ">", ":", ";", "?"] and len(nplname) != 22:
			nplname += text
		if text == "\r":
			if nplname != "":
				npl(nplname)
			nplname = ""
			mode = "PLAYER"

@window.event
def on_text_motion(motion):
	global nplname
	if motion == key.BACKSPACE and mode == "NPL":
		nplname = nplname[:len(nplname) - 1]

@window.event
def on_key_press(symbol, modifiers):
	global mode
	if symbol == key.ESCAPE:
		if mode == "NPL":
			mode = "PLAYER"
		return True

@window.event
def on_mouse_scroll(x, y, dx, dy):
	global playlistLocation
	if mode == "PLAYER":
		if rectCheck([5, 280], [195, window.height - 35], [x, y]):
			if dy == 1 and retPlaylist()[-1:] != playlists[-1:]:
				playlistLocation += 1
				if playlistLocation > len(playlists) - 1:
					playlistLocation = len(playlists) - 1
			if dy == -1:
				playlistLocation -= 1
				if playlistLocation < 0:
					playlistLocation = 0
		
def update(dt):
	plRefresh()

uDate = pyglet.clock.get_default()		
uDate.schedule_interval(update, 1.0)
pyglet.app.run()
