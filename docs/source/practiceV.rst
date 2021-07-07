Site for Vetle to do practice excercise
=======================================

This is the paragraph for the practice of Vetle. Let's hope Denmark beats England in the Euros tonight. 


Advantages of Denmark:
----------------------
- Kasper Schmeichel is a better goalkeeper than Jordan Pickford 
- Football has never come home to England 
- The British people are afraid of penalties 

The danes celebrate goals by throwing beers in the air. This celebration can be seen in this video_.

.. _video: https://www.youtube.com/watch?v=PU0sCWmEQZU/


if you want to plot the heart rate of the british people during a penalty shootout, it can be done like this:
:: 
 
   import numpy as np 
   import matplotlib.pyplot as plt 
   
   time = np.linspace(0,5,1000) # Duration of penalty shootout [minutes]
   heartbeat = np.ones(1000)*100 + 15 * np.sin(time) # Heartbeat

   plt.plot(time, heartbeat)
   plt.show()


Having looked at physiology, let's look at a table showing a possible outcome of a penalty shootout. 

+-----------+-------+-------+
|Shot number|England|Denmark|
+===========+=======+=======+
|     1     |   x   |   1   |
+-----------+-------+-------+
|     2     |   x   |   2   |
+-----------+-------+-------+
|     3     |   x   |   3   |
+-----------+-------+-------+

It's evident from the above table that the penalty abilities of the british players are quite subpar. Denmark won 3-0, and the shooutout ended after three consecutive misses from England, while Denmark scored on the first three. 

A related image will appear shortly 
