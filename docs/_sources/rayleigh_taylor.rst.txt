Rayleigh Taylor instability
======

Results from RT experiments run with different parameters
----
In these experiments, we change various parameters and study the effects in resultant density. The Ramses solver is used to simulate the experiment, and simulation snapshot are taken after 5 seconds. At this time we can compare results from different runs. 

Initially, experimental parameters follow Abel. T (2011)

+-----------------------+
| Experiment Parameters |
+----------+------------+
| Quantity |   Value    |
+==========+============+
|    y0    |    0.5     |
+----------+------------+
|    d1    |     1      |
+----------+------------+
|    d2    |     2      |
+----------+------------+
|  deltay  |   0.025    |
+----------+------------+
| deltavy  |   0.025    |
+----------+------------+
|  dymin   |    0.3     |
+----------+------------+
|  dymax   |    0.7     |
+----------+------------+

with gas constant gamma = 1.4

Varying Ramses slope type
----

Type of slope limiter used in the Godunov scheme for the piecewise linear reconstruction, see the `Ramses docs <https://bitbucket.org/rteyssie/ramses/wiki/Hydro%20Parameters>`_ for further explanation.

.. image:: img_rayleigh_taylor/density_slope_2_50.png
       :width: 48 %
.. image:: img_rayleigh_taylor/density_slope_1_50.png
       :width: 48 %
.. image:: img_rayleigh_taylor/density_run_3_50.png
          :width: 48 %




