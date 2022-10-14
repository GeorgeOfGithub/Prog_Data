import numpy as np
import pandas as pd


def textToNato(plainText):
    to_print = np.zeros(0)
    converter =  {
        'a': 'Alpha',  'b': 'Bravo',   'c': 'Charlie',
        'd': 'Delta',  'e': 'Echo',    'f': 'Foxtrot',
        'g': 'Golf',   'h': 'Hotel',   'i': 'India',
        'j': 'Juliet','k': 'Kilo',    'l': 'Lima',
        'm': 'Mike',   'n': 'November','o': 'Oscar',
        'p': 'Papa',   'q': 'Quebec',  'r': 'Romeo',
        's': 'Sierra', 't': 'Tango',   'u': 'Uniform',
        'v': 'Victor', 'w': 'Whiskey', 'x': 'Xray',
        'y': 'Yankee', 'z': 'Zulu'}
    for i in range(len(plainText)):
        to_print = np.append(to_print, converter[plainText[i].lower()])
    printing = str.join("-",to_print)
    return printing

