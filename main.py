#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blink

if __name__ == '__main__':
    led = blink.Blink()
    led.blink((11, 0, 0), 0.1)
