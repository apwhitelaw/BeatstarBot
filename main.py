# BeatStarBot v0.1 - work in progress

import cv2
import pyautogui
import os
import glob
from ScreenGrabber import ScreenGrabber
from PatternMatcher import PatternMatcher


class MainApp:
    sg = ScreenGrabber()
    pm = PatternMatcher()

    def main(self):
        self.reset_app()
        if len(self.sg.focus) is 0:
            self.sg.set_focus_region()
        coords = (self.sg.focus[0][0], self.sg.focus[0][1], self.sg.focus[1][0], self.sg.focus[1][1])

        while True:
            beatstar_template = 'images/beatstar_text.png'
            template = 'images/bar.png'
            screen_path = self.sg.get_screen(coords)
            rectangles = self.pm.match(screen_path, template)

            # if len(rectangles) >= 1:
            if len(rectangles) >= 1:
                self.press_keys(rectangles)
            else:
                rectangles = self.pm.match(screen_path, beatstar_template)
                if len(rectangles) >= 1:
                    self.press_keys(rectangles)

        cv2.destroyAllWindows()

    def press_keys(self, rectangles):
        key_dict = {}
        for rect in rectangles:
            if rect[0] < 200:
                key_dict["a"] = True
            if 200 < rect[0] < 350:
                key_dict["s"] = True
            if rect[0] > 350:
                key_dict["d"] = True
        pyautogui.hotkey(*key_dict)

    # removes all screenshots
    def reset_app(self):
        print("removing files")
        files = glob.glob("screencaps/*")
        for f in files:
            try:
                os.remove(f)
            except:
                pass

    def test_match(self, path, template):
        test_img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        rects = self.pm.match(path, template)
        for (x, y, w, h) in rects:
           cv2.rectangle(test_img, (x,y), (x+w, y+h), (0,255,255), 2)
        cv2.imshow('Screen', test_img)
        cv2.waitKey()
        cv2.destroyAllWindows()


app = MainApp()
app.main()
#app.test_match("images/test_beatstar.png", "images/beatstar_text.png")
#pyautogui.hotkey("alt", "prntscrn")