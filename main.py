#!/usr/bin/env python
# -*- coding: utf-8 -*-

from arthurGui import ArthurGui

if __name__ == '__main__':
    arthurGui = ArthurGui()
    arthurGui.run()
    print("coucou")
    #arthurGui.eyes.window.mainloop()
    arthurGui.eyes.window.destroy()
