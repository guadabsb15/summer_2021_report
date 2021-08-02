Orszag-Tang vortex
==================

Here we will report the results of the Orszag-Tang experiment. The simulations were performed with the 
 * Branch: Develop
 * Hash: 5e8f853 
 * OMP_NUM_THREADS=4


Simulation parameters
#####################

We will now report the parameters used for the simulation. For the dimensions of the simulation environment we will only report the quantities in the xy-direction, but the other two planes are configured with similar parameters, but the actual number are permutated. 

Output paramaters
*****************

For the output we have 

+----------------------------------+
| out_params                       |
+==================================+
| end_time | out_time | print_time |
+----------+----------+------------+
| 0.5      | 0.1      | 0          | 
+----------+----------+------------+


Initial conditions
******************

For the **xy-plane** we have 

+--------------------------------------------------+
| cartesian_params                                 |
+===========+=======+==========+========+==========+
| size      | dims  | mpi_dims | origin | periodic |
+-----------+-------+----------+--------+----------+
| 1,1,0.005 | 6,6,1 | 2,2,1    | 0,0,0  | t,t,t    |
+-----------+-------+----------+--------+----------+

+----------------------------------------------------+
| patch_params                                       |
+====+=========+==============+==============+=======+
| nt | n       | no_mans_land | do_check_nan | grace |
+----+---------+--------------+--------------+-------+
| 5  | 32,32,1 | t            | t            | 0.1   |
+----+---------+--------------+--------------+-------+

+-----------+
| IC_params |
+===========+
| idirect   | 
+-----------+
| 3         |
+-----------+

For the **xz-plane** the simulation was run by interchanging the second and third value of size, dims, mpi_dims and n, while the **yz-plane** was simulated by interchanging the first and thrid value of the same parameters. For the **xz-plane** we used idirect=2 for the IC_params, while idirect=1 corresponded to the **yz-plane**.


Solver parameters
#################

For the gas, we used a **gamma-law** equation of state with 
 * gamma=5/3 

Bifrost parameters
******************

For the bifrost solver we used 

+--------------------------------------+
| bifrost_params                       |
+======+=====+=====+======+======+=====+
| Ca   | U   | Uv  | d    | e    | E   | 
+------+-----+-----+------+------+-----+
| 0.03 | 0.1 | 0.1 | 0.05 | 0.30 | 0.3 |
+------+-----+-----+------+------+-----+

+--------------------------------------+
| stagger_params                       |
+======+=====+=====+======+======+=====+
| cs   | pa  | ofd | mas  |  kap | eta | 
+------+-----+-----+------+------+-----+
| 0.10 | 1.0 | 1.0 | 0.0  |  1.0 | 1.0 | 
+------+-----+-----+------+------+-----+




Ramses parameters
*****************

For the ramses solver, we used 
 * slope_type=3.5




Bifrost results
##########################

Here we will show the results of the experiment compiled with the bifrost solver. There are four quantities we will report for three different planes, namely density, energy, velocity magnitude and magnetic pressure.


We will plot the final states of the different quantities in all three directions. We will also include a plot of the initial state at t=0s for the xy-direction only. The plot at t=0s for the xy plane will be shown in the upper left panel, while the upper right panel shows the plot in the xy-plane after t=0.5s. The lower left and lower bottom corresponds to the xz-plane and yz-plane at t=0.5s respectively. 

Density
*******

We begin with the density, shown below.  

.. image:: img_ot_bifrost/density_ot_bifrost_xy_0.png
   :width: 48 % 
.. image:: img_ot_bifrost/density_ot_bifrost_xy_5.png
   :width: 48 % 
.. image:: img_ot_bifrost/density_ot_bifrost_xz_5.png 
   :width: 48 % 
.. image:: img_ot_bifrost/density_ot_bifrost_yz_5.png
   :width: 48 % 


Energy
******

We proceed with the energy, shown below

.. image:: img_ot_bifrost/ee_ot_bifrost_xy_0.png
   :width: 48 % 
.. image:: img_ot_bifrost/ee_ot_bifrost_xy_5.png
   :width: 48 % 
.. image:: img_ot_bifrost/ee_ot_bifrost_xz_5.png 
   :width: 48 % 
.. image:: img_ot_bifrost/ee_ot_bifrost_yz_5.png 
   :width: 48 %


Velocity magnitude
******************

Below are the images of the velocity magnitude

.. image:: img_ot_bifrost/velocity_magnitude_ot_bifrost_xy_0.png
   :width: 48 % 
.. image:: img_ot_bifrost/velocity_magnitude_ot_bifrost_xy_5.png
   :width: 48 % 
.. image:: img_ot_bifrost/velocity_magnitude_ot_bifrost_xz_5.png 
   :width: 48 % 
.. image:: img_ot_bifrost/velocity_magnitude_ot_bifrost_yz_5.png 
   :width: 48 %


Magnetic pressure
*****************

Finally, we plot the magnetic pressure

.. image:: img_ot_bifrost/magnetic_pressure_ot_bifrost_xy_0.png
   :width: 48 % 
.. image:: img_ot_bifrost/magnetic_pressure_ot_bifrost_xy_5.png
   :width: 48 % 
.. image:: img_ot_bifrost/magnetic_pressure_ot_bifrost_xz_5.png 
   :width: 48 % 
.. image:: img_ot_bifrost/magnetic_pressure_ot_bifrost_yz_5.png 
   :width: 48 %



Ramses results
#########################


We will now report the results obtained compiled with the ramses/mhd_eos solver, where we plot the same quantities as we did for the bifrost solver. 

The plots are the same as we did with bifrost, where each quantity is shown for the xy-plane, xz-plane and yz-plane. For the xy-plane we will include the result at t=0s, but for all three directions we will report the result after t=0.5s. Similarly to the bifrost plots, the upper left and upper right plots corresponds to the xy-plane at t=0s and t=0.5s repsectively. The lower left and lower right plots correspond to the xz-plane and yz-plane, respectively.  


Density
*******

We begin with the density, shown below.  

.. image:: img_ot_ramses/density_ot_ramses_xy_0.png
   :width: 48 % 
.. image:: img_ot_ramses/density_ot_ramses_xy_5.png
   :width: 48 % 
.. image:: img_ot_ramses/density_ot_ramses_xz_5.png 
   :width: 48 % 
.. image:: img_ot_ramses/density_ot_ramses_yz_5.png 
   :width: 48 %


Energy
******

Then we plot the energy, shown below

.. image:: img_ot_ramses/ee_ot_ramses_xy_0.png
   :width: 48 % 
.. image:: img_ot_ramses/ee_ot_ramses_xy_5.png
   :width: 48 % 
.. image:: img_ot_ramses/ee_ot_ramses_xz_5.png 
   :width: 48 % 
.. image:: img_ot_ramses/ee_ot_ramses_yz_5.png 
   :width: 48 %


Velocity magnitude
******************

The resulting velocity magnitude is shown below

.. image:: img_ot_ramses/velocity_magnitude_ot_ramses_xy_0.png
   :width: 48 % 
.. image:: img_ot_ramses/velocity_magnitude_ot_ramses_xy_5.png
   :width: 48 % 
.. image:: img_ot_ramses/velocity_magnitude_ot_ramses_xz_5.png 
   :width: 48 % 
.. image:: img_ot_ramses/velocity_magnitude_ot_ramses_yz_5.png 
   :width: 48 %


Magnetic pressure
*****************

Finally, we plot the magnetic pressure, shown below.

.. image:: img_ot_ramses/magnetic_pressure_ot_ramses_xy_0.png
   :width: 48 % 
.. image:: img_ot_ramses/magnetic_pressure_ot_ramses_xy_5.png
   :width: 48 % 
.. image:: img_ot_ramses/magnetic_pressure_ot_ramses_xz_5.png 
   :width: 48 % 
.. image:: img_ot_ramses/magnetic_pressure_ot_ramses_yz_5.png 
   :width: 48 %




