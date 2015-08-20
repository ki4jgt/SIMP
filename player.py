#!/usr/bin/env python3

#Please use this to disable advertisements. It's a great way to keep
#from screwing supporters by unintentionally mishandling code. Not to
#mention, it's SUPER easy!

PlayAds = True

from pyglet.gl import *
from os import listdir, system, mkdir
from pyglet.window import key

ver = "SIMP 15.09 ALPHA"

window = pyglet.window.Window(1000, 600, resizable=True, caption = ver)
icon = pyglet.image.load("Resources/icon.png")
buttons = pyglet.image.load("Resources/playerbuttons.png")
play = pyglet.image.load("Resources/play.png")
window.set_icon(icon)
window.push_handlers(pyglet.window.event.WindowEventLogger())
window.set_minimum_size(640, 480)
pyglet.font.add_file("Resources/UbuntuMono-R.ttf")
uMono = pyglet.font.load("Ubuntu Mono")
#=============================Variables=================================
pStatus = False

mode = "PLAYER"

playlists = []

playlist = ""
playlistLocation = 0

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
	playlists = listdir("Playlists")

def npl(name):
	fob = open("Playlists/" + name, "a")
	fob.close()

def nplnameseg():
	global nplname
	if len(nplname) > 16:
		return nplname[-16:]
	else:
		return nplname
		
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
		pyglet.text.Label(entry, font_name = "Ubuntu Mono", font_size = 12, x = 10, y = a, anchor_x = "left", anchor_y = "top").draw()
		a = a - 20
	#New Playlist Button
	glBegin(GL_LINES)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(10, 280)
	glVertex2f(190, 280)
	glEnd()
	glBegin(GL_POLYGON)
	glColor3f(0.18, 0.18, 0.18)
	glVertex2f(5, 250)
	glColor3f(0.0, 0.0, 0.0)
	glVertex2f(5, 279)
	glVertex2f(195, 280)
	glColor3f(0.18, 0.18, 0.18)
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
	global mode, nplname
	if rectCheck([300, window.height - 101], [364, window.height - 37], [x, y]) and mode == "PLAYER":	
		cpStatus()
	if rectCheck([5, 250], [195, 280], [x, y]) and mode == "PLAYER":
		mode = "NPL"
	if mode == "NPL" and rectCheck([(window.width / 2) - 150, (window.height / 2) - 80], [(window.width / 2) + 150, (window.height / 2) - 30], [x, y]):
		if nplname != "":
			npl(nplname)
		nplname = ""
		mode = "PLAYER"

@window.event
def on_text(text):
	global nplname, mode
	if text == " " and mode == "PLAYER":
		cpStatus()
	if mode == "NPL" and text not in ["\r", "/", "\\", "\"", ".", "`", "~", "<", ">", ":", ";", "?"] and len(nplname) != 22:
		nplname = nplname + text
	if text == "\r" and mode == "NPL":
		if nplname != "":
			npl(nplname)
		nplname = ""
		mode = "PLAYER"

@window.event
def on_text_motion(motion):
	global nplname
	if motion == 65288 and mode == "NPL":
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
	print(playlistLocation)
	if rectCheck([5, 280], [195, window.height - 35], [x, y]) and mode == "PLAYER":
		if dy == 1 and retPlaylist()[-1:] != playlists[-1:]:
			playlistLocation = playlistLocation + 1
			if playlistLocation > len(playlists) - 1:
				playlistLocation = len(playlists) - 1
		if dy == -1:
			playlistLocation = playlistLocation - 1
			if playlistLocation < 0:
				playlistLocation = 0
		
def update(dt):
	plRefresh()
		
pyglet.clock.schedule_interval(update, 1.0)
pyglet.app.run()
