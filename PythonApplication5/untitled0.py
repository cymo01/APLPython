# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:50:43 2022
 I created this little program based on a Youtube video. The point was to exercise the Python debugger ipdb.
 Set 2 breakpoints: 1 on line 10 and one on line 19. Start debugging. Then use the 'step into' button to execute
 The code.

@author: whitedk1
"""

def hello_world(firstname, lastname):
    var=12
    print("My name is {} {}".format(firstname, lastname))
    var=24
    sum1=var+250
    print(sum1)
    
    
    
hello_world('Kem', 'White')