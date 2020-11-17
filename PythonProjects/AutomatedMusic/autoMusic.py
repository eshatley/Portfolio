from selenium.webdriver import Firefox
from slenium.webdriver.firefox.options import Options
from time import sleep, ctime
from collections import Thread
from os.path import isfile
import csv

#Websites to play music from
BANDCAMP_HOME = 'https://bandcamp.com/'

class musicPlayer():
		#Create a headless browser
    def __init__(self)
        opt = Options()
        opt.set_headless()
        self.browser = Firefox(options = opt)
        self.browser.get(BANDCAMP_HOME) #Come back and add functionality to select different websites

        #Track list state
        self.currentTrackNumber = 1
        self.trackList = []
        self.tracks()
        
    def tracks(self):
        #Sleep to give the browser time to finish any animations
        sleep(1)
        
        #Get container for track list from the 'Discover' section
        discover_selection = self.browser.find_element_by_class_name('discover-results')
        left_x = discover_selection.location['x']
        right_x = left_x + discover_section.size['width']
        
        #Make sure the list only includes things we could click on
        discover_items = self.browser.find_elements_by_class_name('discover-item')
        self.trackList = [t for t in discover_items
                            if t.location['x'] >= left_x and t.location['x'] < right_x]
                            
        #Print tracks to screen
        for (i, track) in enumerate(self.trackList):
            print('[{}]'.format(i+1))
            lines = track.text.split('\n')
            print('Album : {}'.format(lines[0]))
            print(Artist : {}'.format(lines[1]))
            if len(lines) > 2:
                print('Genre : {}'.format(lines[2]))
                
    def cataloguePages(self):
        #Print accessible pages
        print('PAGES')
        for e in self.browser.find_elements_by_class_name('item-page'):
            print(e.text)
        print('')
        
    def moreTracks(self,page='next'):
        #Advance the catalogue and repop the track list
        next_button = [e for e in self.browser.find_elements_by_class_name('item-page')
                      if e.text.lower().strip() == str(page)]
                 
        if nextButton:
            nextButton[0].click()
            self.tracks()

    def play(self, track=None):
      	#Play track. If no number given, play selected track
      	if track is None:
          	self.browser.find_element_by_class_name('playbutton').click()
      	elif type(track) is int and track <= len(self.trackList) and track >= 1:
            self.currentTrackNumber = track
            self.trackList[self.currentTrackNumber - 1].click()
            
    def playNext(self):
       #Play next track
       if self.currentTrackNumber < len(self.trackList):
          self.play(self.currentTrackNumber+1)
       else:
          self.moreTracks()
          self.play(1)
          
    def pause(self):
        #Pause playback
        self.play()
     



