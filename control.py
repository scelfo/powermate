#!/usr/bin/python

import glob
import sys
from powermate import FileEventSource, LedEvent

class ExamplePowerMate(FileEventSource):
  def on(self):
    self.send(LedEvent.max())
  def off(self):
    self.send(LedEvent.off())
  def pulse(self):
    self.send(LedEvent.pulse())

if __name__ == '__main__':
  pm = ExamplePowerMate(glob.glob('/dev/input/by-id/*PowerMate*')[0], 0)
  for arg in sys.argv:
    if arg == 'on':
      pm.on()
      break
    if arg == 'pulse':
      pm.pulse()
      break
    if arg == 'off':
      pm.off()
      break
