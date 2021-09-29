import cv2
import numpy as np

class PatternMatcher:
    def match(self, path, template):
        screen_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        bar_img = cv2.imread(template, cv2.IMREAD_GRAYSCALE)

        result = cv2.matchTemplate(screen_img, bar_img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print(f"min/max: {min_val}, {max_val}, {min_loc}, {max_loc}")

        w = bar_img.shape[1]
        h = bar_img.shape[0]

        threshold = 0.90
        yloc, xloc = np.where(result >= threshold)

        for (x, y) in zip(xloc, yloc):
            cv2.rectangle(screen_img, (x, y), (x + w, y + h), (0, 255, 255), 1)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        print(f"{len(rectangles)} found")
        if len(rectangles) > 0: print(rectangles)

        return rectangles
