from PIL import ImageGrab
import uuid
import pyWinhook
import pythoncom
import win32gui


class ScreenGrabber:
    hm = pyWinhook.HookManager()
    template = []
    focus = []

    def get_screen(self, coords=(0,0,100,100)):
        screen = ImageGrab.grab(coords)
        name = uuid.uuid4()
        path = f"screencaps/{name}.png"
        screen.save(path, "PNG")
        return path

    def set_focus_region(self):
        self.hm.SubscribeMouseAllButtonsDown(self.onclick)
    #    self.hm.SubscribeMouseMove(onmove) currently unused
        self.hm.HookMouse()
        print("hooked")
        pythoncom.PumpMessages()

    def onclick(self, event):
        print(event.Position)
        self.focus.append(event.Position)
        if len(self.focus) is 2:
            win32gui.PostQuitMessage(0)
            self.hm.UnhookMouse()
            print("unhooked")
        return True

    # currently unused
    def onmove(self, event):
        print(self.event.Position)
        #win32gui.DrawEdge
        return True