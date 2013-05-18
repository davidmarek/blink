import usb.core
import random


class Blink(object):

    colors = {
        'off': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'violet': (255, 0, 255),
        'orange': (255, 40, 0),
        'yellow': (255, 100, 0),
    }

    def __init__(self):
        self.dev = usb.core.find(idVendor=0x16c0, idProduct=0x05df)

        if self.dev is None:
            raise ValueError('Device not found.')

    def set_color_name(self, color):
        self.set_color(*self.colors[color])

    def set_color(self, r, g, b):
        self.dev.ctrl_transfer(0x01 << 5, 0x09, 0, r)
        self.dev.ctrl_transfer(0x01 << 5, 0x09, 0, g)
        self.dev.ctrl_transfer(0x01 << 5, 0x09, 0, b)
        self.dev.ctrl_transfer(0x01 << 5, 0x09, 0, ord('\n'))
        self.read()

    def read(self):
        arr = self.dev.ctrl_transfer((0x01 << 5) | 0x80, 0x01, 0, 0, 1000)
        msg = []
        while arr:
            msg.append(arr[0])
            arr = self.dev.ctrl_transfer((0x01 << 5) | 0x80, 0x01, 0, 0, 1000)

        return ''.join(map(chr, msg))

    @staticmethod
    def random_color():
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))
