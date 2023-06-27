import time

from BrowserHelper import BrowserHelper


bh = BrowserHelper("firefox", False)
bh.input_guess("la")
content = bh.get_article()
print(content[0])
while True:
    # bh.input_guess("test")

    time.sleep(1)