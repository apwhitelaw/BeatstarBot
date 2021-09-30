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

            if len(rectangles) >= 1:
                self.press_keys(rectangles)

            # TODO: Improve beatstar note match speed
            # Beatstar note comes at the end of a set.
            # If no note found, check for beatstar.
            # Since Beatstar match runs after regular note, the tap
            # is always a bit late (still within game's hit window).
            else:
                rectangles = self.pm.match(screen_path, beatstar_template)
                if len(rectangles) >= 1:
                    self.press_keys(rectangles)

        cv2.destroyAllWindows()

    # TODO: Only press 2 keys when vertically aligned
    # Sometimes when a note is followed closely by another note
    # a double press occurs, and one is too early (causes song failure)
    def press_keys(self, rectangles):
        key_dict = {}
        for rect in rectangles:
            if rect[0] < 200:
                key_dict["a"] = True
            if 200 < rect[0] < 350:
                key_dict["s"] = True
            if rect[0] > 350:
                key_dict["d"] = True
        key_string = ""
        for key in key_dict:
            key_string += key

        print(f"pressing {key_string}")
        pyautogui.hotkey(*key_dict)

    # TODO: Implement hold notes
    # Hold notes usually get detected as regular notes
    # Func should keyDown() when hold note detected and
    # then keyUp() when end of note detected.
    def hold_key(self, rectangles):
        pass

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