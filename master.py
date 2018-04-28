#!/usr/bin/env python3
from radio import Radio

from edit import Editor

while True:
    print("Making the editor")
    editor = Editor()
    print("Editor has closed you can do something else...")
    editor = None


    print("Making the radio")
    radio = Radio()
    print("Radio closed you do something else ... ")
    radio = None
