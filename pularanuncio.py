import pyautogui
pyautogui.FAILSAFE = True

def pularanuncio():
    while True:
        videoAscords = pyautogui.locateOnScreen("play.png")
        Banecords = pyautogui.locateAllOnScreen("bannerad.png")
        Blackbanner = pyautogui.locateAllOnScreen("black banner.png")
        if videoAscords or Banecords or Blackbanner is not None:
            break
        if videoAscords is not None:
            pyautogui.click(videoAscords)
        elif Banecords is not None:
               pyautogui.click(Banecords)
        if Blackbanner is not None:
                pyautogui.click(Blackbanner)
        pularanuncio()
pularanuncio()