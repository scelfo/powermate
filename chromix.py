#!/usr/bin/python

import subprocess
import sys

class ChromixController:
  def next_track(self):
    print ('next track')
    #self.click_on_element_google_play('forward')
    self.click_on_element_rhapsody('div.player-advance-button')
    #self.click_on_element_spotify('button[id=next]');

  def play_pause(self):
    print ('play/pause')
    #self.click_on_element_google_play('play-pause')
    self.click_on_element_rhapsody('div.player-play-button > div')
    #self.click_on_element_spotify('button[id=play-pause]');

  def previous_track(self):
    print ('previous track')
    #self.click_on_element_google_play('rewind')
    self.click_on_element_rhapsody('div.player-rewind-button')
    #self.click_on_element_spotify('button[id=previous]');

  def click_on_element_spotify(self, data_id):
    command = (
        '/usr/local/bin/chromix with https://play.spotify.com '
        'goto "javascript:document.getElementById(\'app-player\')'
        '.contentWindow.document.querySelector(\'%s\').click();"'
        % data_id)
    subprocess.call(command, shell=True)

  def click_on_element_rhapsody(self, data_id):
    command = (
        '/usr/local/bin/chromix with https://app.rhapsody.com '
        'goto "javascript:document.querySelector(\'%s\').click();"'
        % data_id)
    subprocess.call(command, shell=True)

  def click_on_element_google_play(self, data_id):
    command = (
        '/usr/local/bin/chromix with https://play.google.com/music/listen '
        'goto "javascript:document.querySelector(\'[data-id=%s]\').click();"'
        % data_id)
    subprocess.call(command, shell=True)


if __name__ == '__main__':
  chromix_controller = ChromixController()
  for arg in sys.argv:
    if arg == 'next':
      chromix_controller.next_track()
      break
    if arg == 'previous':
      chromix_controller.previous_track()
      break
    if arg == 'play-pause':
      chromix_controller.play_pause()
      break
