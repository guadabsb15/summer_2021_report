Sod experimemts 
================

Here we will report the results of the Sod experiment 


Initial conditions
------------------
For the Sod problem we use
       * gamma = 1.4
       * Final time = 0,2 
Below shows a table of the inital conditions for the left state and right state. These values will be used in all verifications for the Sod problem.

+--------------+--------------+----------------+
|  Quantities  |  Left state  |  Right state   |
+==============+==============+================+
|     rho      |      1       |    0.125       |
+--------------+--------------+----------------+
|      p       |      1       |     0.1        |
+--------------+--------------+----------------+
|     vx       |      0       |      0         |
+--------------+--------------+----------------+
|     vy       |      0       |      0         |
+--------------+--------------+----------------+
|     vz       |      0       |      0         |
+--------------+--------------+----------------+
|     bx       |      0       |      0         |
+--------------+--------------+----------------+
|     by       |      0       |      0         |
+--------------+--------------+----------------+
|     bz       |      0       |      0         |
+--------------+--------------+----------------+


The initial Bifrost parameters for the Sod-problem are presented in the table below. During test verifications we are going to change these parameters one at a time, while holding the other parameters constant.
+------------------------------------+
|     Initial Bifrost parameters:    |
+======+=====+=====+=====+=====+=====+
|  Ca  |  U  |  Uv |  d  |  e  |  E  |
+------+-----+-----+-----+-----+-----+
| 0.01 | 0.3 | 0.1 | 0.5 | 0.5 | 0.9 |
+------+-----+-----+-----+-----+-----+


Density for all directions
--------------------------
.. figure:: images_sod_bifrost/sod_bifrost_xyz_rho.png
   :scale: 70 %
   :align: center

   Plot showing the density rho for every direction x,y and z. Here we have used the initial Bifrost parameters which are presented above.





different directions
different solvers

references



