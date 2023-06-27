import time

from BrowserHelper import BrowserHelper


bh = BrowserHelper("firefox", False)
bh.input_guess("la")
bh.get_article()
while True:
    # bh.input_guess("test")

    time.sleep(1)