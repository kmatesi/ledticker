#!/usr/bin/python
#===============================================================================
from led_sign.client import SignClient
import os
import time
import utils
import get_scores
import display_scores
#-------------------------------------------------------------------------------
def start_msg():
    from led_sign.client import SignClient; print

    pwd = os.path.dirname(os.path.realpath(__file__))
    led_sign_path = '/'.join([pwd, 'led_sign']) 
    glyphs_path = '/'.join([led_sign_path, 'glyphs'])

    start = ['Starting', 'Sports Ticker']
    SignClient(glyphs_path, led_sign_path).send_text_to_sign(start);
#---------------------------------------------------------------------------
if __name__ == "__main__":
    start_msg()

    while True:
        get_scores.main()
        display_scores.main()
#===============================================================================
