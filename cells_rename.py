# -*- coding: utf-8 -*-


import os
from pathlib import Path
import numpy as np

dictfront = {"Fifth": 4, "First": 0, "Fourth": 3, "Second": 1, "Third": 2}

dictlast = {"one": 7, "second": 6, "third": 5}

mappingArray = np.array(
    [
        [38, 26, 40, 28, 66, 78, 68, 80, 100, 94],
        [92, 98, 76, 64, 74, 62, 24, 36, 22, 34],
        [30, 18, 32, 20, 58, 70, 60, 72, 96, 90],
        [91, 97, 75, 63, 73, 61, 23, 35, 21, 33],
        [29, 17, 31, 19, 57, 69, 59, 71, 95, 89],
        [6, 14, 8, 16, 46, 54, 48, 56, 88, 84],
        [82, 86, 52, 44, 50, 42, 12, 4, 10, 2],
        [5, 13, 7, 15, 45, 53, 47, 55, 87, 83],
        [81, 85, 51, 43, 49, 41, 11, 3, 9, 1],
    ]
)

valuesInUse ={93:1,99:1,79:1,67:1,77:1,65:1,27:1,39:1,25:1,37:1}
def testmap():
    for lines in mappingArray:
        for val in lines:
            if val in valuesInUse:
                print(f"error: collision at: {val}")
            else:
                valuesInUse[val] = 1

    print("all done ")

orientationDict = {0: "", 1: "_12", 2: "_4", 3: "_8"}


def walkdir(root_dir):
    for (dirpath, dirs, files) in os.walk(root_dir):
        for filename in files:
            name = Path(filename).stem
            parts = name.split("_")
            if len(parts) > 2:

                row = 10
                if parts[0] == "Last" or parts[0] == "last":
                    if len(parts) > 3:
                        row = dictlast[parts[2]]
                    else:
                        row = 8
                else:
                    row = dictfront[parts[0]]
                idx = int(parts[-1])
                realid = idx // 4 * 2
                if row in [1, 3, 6, 8]:
                    if (idx % 4) == 3:
                        realid = realid + 1
                else:
                    if (idx % 4) > 0:
                        realid = realid + 1
                orientation = ""
                if row in [1, 3, 6, 8]:
                    orientation = str(orientationDict[(idx + 1) % 4])
                else:
                    orientation = str(orientationDict[(idx) % 4])
                try:
                    os.rename(
                        os.path.join(dirpath, filename),
                        os.path.join(
                            dirpath,
                            "Cell"
                            + str(mappingArray[row][realid])
                            + orientation
                            + ".png",
                        ),
                    ),

                except:
                    print("error")
            else:
                print(parts)
    print("dones")


if __name__ == "__main__":
    walkdir(" ")
