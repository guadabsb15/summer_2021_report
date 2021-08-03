Rayleigh Taylor instability
======

Results from RT experiments run with different parameters
----
In these experiments, we change various parameters and study the effects in resultant density. The Ramses solver (ramses/mhd_eos) is used to simulate the experiment, and simulation snapshot are taken after 5 seconds. At this time we can compare results from different runs. 

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

slope_type is a parameter for the ramses solver. We tried the different values 1, 2, and 3.5

.. list-table:: 

    * - .. figure:: img_rayleigh_taylor/density_slope_1_50.png
           Fig 1. slope_type = 1.0

      - .. figure:: img_rayleigh_taylor/density_slope_2_50.png
           Fig 2. slope_type = 2.0

      - .. figure:: img_rayleigh_taylor/density_run3_50.png
           Fig 3. slope_type = 3.5


