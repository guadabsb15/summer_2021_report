Rayleigh Taylor instability
============================

Results from RT experiments run with different parameters
---------------------------------------------------------
In these experiments, we change various parameters and study the effects in resultant density.
We use both the Ramses solver (ramses/mhd_eos from the `Dispatch-Bifrost <https://github.com/ITA-Solar/Dispatch-Bifrost>`_ repository) and Bifrost (ideal_mhd from the `Bifrost <https://github.com/ITA-Solar/Bifrost>_` repository) to simulate the experiment.
Simulation snapshot are taken after 5 seconds, and at this time we can compare results from different runs.

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

Ramses
---------------------------------------------------------

First, we study the Ramses solver

Varying Ramses slope type
******************************************************************

``slope_type`` is a parameter for the ramses solver. We tried the different values 1, 2, and 3.5

The following simulations are run on grids with resolution 128x256 in x, y.

.. list-table::

    * - .. figure:: img_rayleigh_taylor/density_slope_1_50.png

           ``slope_type = 1.0``

      - .. figure:: img_rayleigh_taylor/density_slope_2_50.png

           ``slope_type = 2.0``

      - .. figure:: img_rayleigh_taylor/density_run3_50.png

           ``slope_type = 3.5``

Some details in the results are clearly dependent on the ``slope_type`` variable.
Larger values of this parameter gives the results finer/smaller scale patterns.
Larger ``slope_type`` also introduces more non-linearity, and the flow becomes more turbulent.


Effects of grid in Ramses
******************************************************************

Falling back to the default ``slope_type=3.5``, we study how grid resolution affects results.


.. list-table::

    * - .. figure:: img_rayleigh_taylor/density_ramses_small_50.png

           nx=64, ny=128

      - .. figure:: img_rayleigh_taylor/density_run3_50.png

           nx=128, ny=256

    * - .. figure:: img_rayleigh_taylor/density_ramses_medium_20.png

           nx=256, ny=512

      - .. figure:: img_rayleigh_taylor/density_ramses_large_20.png

           nx=512, ny=1024


Finer resolution gives more details to the results, and patterns exists on smaller scales.
It also makes the density profiles less symmetric and more chaotic.

Bifrost
---------------------------------------------------------

Now, we move on to the Bifrost solver. We have the same intial conditions, and the Bifrost parameters are by default

.. code-block::

    mhd_template['nu1'] = 0.1
    mhd_template['nu2'] = 0.1
    mhd_template['nu3'] = 0.5
    mhd_template['nu_r'] = 0.3

The default grid is `nx=128, ny=256`.

Effects of grid in Bifrost
******************************************************************

.. list-table::

  * - .. figure:: img_rayleigh_taylor/rho_bifrost_64x128.png

         nx=64, ny=128

    - .. figure:: img_rayleigh_taylor/rho_bifrost_128x256.png

         nx=128, ny=256

  * - .. figure:: img_rayleigh_taylor/rho_bifrost_256x512.png

         nx=256, ny=512

    - .. figure:: img_rayleigh_taylor/rho_bifrost_512x1024.png

         nx=512, ny=1024



With Bifrost, the solution does not posess the same details as the Ramses solver.
There are less whirls and non-linearity in these solutions.




