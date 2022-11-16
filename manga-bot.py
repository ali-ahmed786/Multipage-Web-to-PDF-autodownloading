import pyautogui
import time

chapter = 1 
def nextChapter(chapter):
    nextLocation = pyautogui.locateOnScreen('next.png', confidence=0.7)
    if (pyautogui.locateOnScreen('next.png', confidence=0.5) is not None):
        menuLocation = pyautogui.locateOnScreen('menu.png', confidence=0.7)
        pyautogui.click(menuLocation)
        printOptionLocation = pyautogui.locateOnScreen('print.png', confidence=0.7)
        pyautogui.click(printOptionLocation)
        time.sleep(1)
        pagesOptionLocation = pyautogui.locateOnScreen('pages.png', confidence=0.7)
        pyautogui.click(pagesOptionLocation)
        time.sleep(1)
        customPagesOptionLocation = pyautogui.locateOnScreen('customised.png', confidence=0.7)
        if(pyautogui.locateOnScreen('customised.png', confidence=0.7) is not None):
            pyautogui.click(customPagesOptionLocation)
            time.sleep(1)
            pyautogui.write('1-20') #customising the pages being downloaded as pdf
            printBtnLocation = pyautogui.locateOnScreen('printbtn.png', confidence=0.7)
            pyautogui.click(printBtnLocation)
            time.sleep(3)
            if(pyautogui.locateOnScreen('filename.png', confidence=0.7) is not None):
                fileNameLocation = pyautogui.locateOnScreen('filename.png', confidence=0.7)
                pyautogui.click(fileNameLocation)
                time.sleep(3)
                pyautogui.typewrite('chapter ' + str(chapter))
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(3)
                findnext(chapter)
            else:
                time.sleep(20)
                fileNameLocation = pyautogui.locateOnScreen('filename.png', confidence=0.7)
                pyautogui.click(fileNameLocation)
                time.sleep(3)
                pyautogui.typewrite('chapter ' + str(chapter))
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(3)
                findnext(chapter)


def findnext(chapter):
    condition = False
    nextLocation = pyautogui.locateOnScreen('next.png', confidence=0.7)
    while (pyautogui.locateOnScreen('next.png', confidence=0.7) is None):
        scroll()
        findnext(chapter)
    pyautogui.click(nextLocation)
    time.sleep(3)
    chapter+=1
    time.sleep(1)
    scrollAndPrint(chapter)
            
    
def scrollAndPrint(chapter): #scroll again to move to the next chapter
    condition = False
    while (pyautogui.locateOnScreen('next.png', confidence=0.7) is None):
        scroll()
    nextChapter(chapter)
            
    
    
def scroll(): #function to scrol so the all the manga panels are loaded so the pdf does not have any blank pages due to unloaded image panels
    time.sleep(0.5)
    pyautogui.scroll(-800)

scrollAndPrint(chapter)
