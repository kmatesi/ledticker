#!/usr/bin/python
#===============================================================================
from baseticker.client import SignClient
import os
import time
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
def send_msg(entry):
    # New client to write to led sign
    pwd = os.path.dirname(os.path.realpath(__file__))
    led_sign_path = '/'.join([pwd, 'led_sign']) 
    glyphs_path = '/'.join([led_sign_path, 'glyphs'])

    sign_client = SignClient(glyphs_path, led_sign_path)
    sign_client.send_text_to_sign(entry)
    time.sleep(6)

if __name__ == "__main__":
    start_msg()

    #while True:
    #    scores = get_scores.main()
    #    for line in scores:
    #        send_msg(line)
#===============================================================================
