#!/usr/bin/python
#messages max out at 16 characters
#===============================================================================
from baseticker.client import SignClient
import os
import time
import get_scores
#-------------------------------------------------------------------------------
def start_msg():
    from baseticker.client import SignClient; print

    pwd = os.path.dirname(os.path.realpath(__file__))
    led_sign_path = '/'.join([pwd, 'baseticker']) 
    glyphs_path = '/'.join([led_sign_path, 'glyphs'])
    start = [
            "Starting Kevin's",
            "Sport Ticker..."
            ]
    SignClient(glyphs_path, led_sign_path).send_text_to_sign(start);
#---------------------------------------------------------------------------
def send_msg(entry):
    # New client to write to led sign
    pwd = os.path.dirname(os.path.realpath(__file__))
<<<<<<< HEAD
    led_sign_path = '/'.join([pwd, 'baseticker']) 
=======
    led_sign_path = '/'.join([pwd, 'led_sign']) 
>>>>>>> origin/master
    glyphs_path = '/'.join([led_sign_path, 'glyphs'])

    sign_client = SignClient(glyphs_path, led_sign_path)
    sign_client.send_text_to_sign(entry)
    time.sleep(6)

if __name__ == "__main__":
    start_msg()
    time.sleep(6)
    scores = []

    while True:
<<<<<<< HEAD
        del scores[:]
        scores = get_scores.main()
        scores.append("['Refreshing Scores'],['Please Wait...']")
        for line in scores:
            send_msg(line)
        time.sleep(6)
=======
        scores = get_scores.main()
        for line in scores:
            send_msg(line)
>>>>>>> origin/master
#===============================================================================
