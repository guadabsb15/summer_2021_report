Site for Isak to do practice excercise
=======================================
In this excericise I wil study some various animals living inthe world.

Describing animals
--------------------
- Everyone knows that pigs are fat.
- You never know when that bear is going to attack.
- I always wonder why squirrels are so good at climbing. 

Are bears related to pigs, the following website_ 

.. _website: https://bear.org/are-bears-related-to-pigs/

explains this in more detail.


Comparing animals
------------------
This is my animal table, camparing color and size for Pigs, Bears and squirrels:

+---------+--------+--------+
|  Animal |  color |  size  |
+---------+--------+--------+
|   Pig   |  pink  | medium |
+---------+--------+--------+
|   Bear  |  brown |  big   |
+---------+--------+--------+
| Squirrel|  brown | small  |
+---------+--------+--------+

Deaths caused by bear attack
-----------------------------------
Below shows python code for plotting age-distribution of bears:

::

    import numpy as np
    import matplotlib.pyplot as plt
    
    years = np.linspace(0,10,11)
    deaths = np.array([2,5,10,20,80,300,1000,7800,43000,38000    0,3000000])
    
    plt.plot(years,deaths, label = 'Killed by bear')
    plt.xlabel('year')
    plt.ylabel("Number of deaths")
    plt.title("Number of human deaths, caused by bear attack"    )
    plt.legend()
    plt.show()
   



