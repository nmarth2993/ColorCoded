"""
Author: Nicholas Marthinuss
12/1/2020
This program takes a user-entered phrase and displays
the hex colors the phrase can be represented as
"""

import tkinter as tk

HEX_COLOR_LEN = 6


def convert(phrase: str) -> list:
    """
    Takes user input of a phrase and converts it to a list
    of hex bytes as strings

    :return: list of strings with corresponding hex bytes (0 filled)
    """
    hex_values = []
    for char in phrase:
        # add each character's hex representation to the list
        hex_values.append(str(hex(ord(char))))

    color_list = []
    count = 0
    color = "#"  # we add the '#' because hex color tags have this at the front
    for byte in hex_values:

        color += byte[2:]  # strip off the "0x" prefix
        count += 1
        if count == 3:
            color_list.append(color)
            count = 0
            color = "#"
    # if we have remaining bits, add them on
    if color != "#":  # check to make sure the string isn't empty
        while len(color) < HEX_COLOR_LEN + 1:  # + 1 becuase of the # symbol
            color += '0'  # 0 fill
        color_list.append(color)

    print("size:", len(color_list))
    for code in color_list:
        print(code)
    return color_list


class Window(tk.Tk):
    HEIGHT = 800
    WIDTH = 800

    def __init__(self, colors: list):
        tk.Tk.__init__(self)
        self.title("Color Coded")
        self.geometry(str(Window.WIDTH) + 'x' + str(Window.HEIGHT))
        self.canvas = tk.Canvas(self, width=Window.WIDTH, height=Window.HEIGHT,
                                borderwidth=0, highlightthickness=0, background="black")
        self.canvas.pack()
        self.colors = colors
        # make n equal regions
        self.region_width = Window.WIDTH / len(colors)
        for i in range(int(Window.WIDTH / self.region_width)):
            # draw each rectangle
            self.canvas.create_rectangle(
                i * self.region_width, 0, (i + 1) * self.region_width, Window.HEIGHT, fill=colors[i])


if __name__ == "__main__":
    colors = Window(convert(input("enter the phrase to encode: ")))
    colors.mainloop()
