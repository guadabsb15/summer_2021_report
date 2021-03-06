Brio& Wu experimemts 
=========================

Here we will report the results of the Brio&Wu experiment.
These studies were wone using the develop branch of Dispatch-Bifrost and hash 299c6d5


Bifrost Solver 
---------------------
For the brio-wu experiment we use
        * gamma = 2.0
        * Final time = 0.1 
where the equation of state is a gamma law. 


Below is a table of the input parameters used for simulating the experiment in all three directions. 
These values are used in all verifications for the brio-wu experiment. 

+----------+----------+-----------+
| Quantity |Left state|Right state|
+==========+==========+===========+
| rho      | 1        | 0.125     |
+----------+----------+-----------+
| vx       |  0       | 0         |
+----------+----------+-----------+
| vy       |  0       | 0         |
+----------+----------+-----------+
| vz       |  0       | 0         |
+----------+----------+-----------+
| p        |  1       | 0.1       |
+----------+----------+-----------+

The magnetic field values are different for the three direction, and are listed in the table below. 
These will also be used in all subsequent verification tests. 

           +-------------------------------------+
           |  Simulation direction               |
+----------+-------------+-----------+-----------+
|Quantity  |  x          |    y      | z         |
|          +------+------+-----+-----+-----+-----+
|          |Left  |Right |Left |Right|Left |Right|            
+----------+------+------+-----+-----+-----+-----+
| Bx       | 0.75 | 0.75 | 0   | 0   | 1   | -1  |
+----------+------+------+-----+-----+-----+-----+
| By       |  1   | -1   | 0.75|0.75 | 0   | 0   |
+----------+------+------+-----+-----+-----+-----+
| Bz       |  0   | 0    | 1   | -1  | 0.75| 0.75|
+----------+------+------+-----+-----+-----+-----+

The initial Bifrost parameters used in the experiment are:

+-----------------------------+
| Initial Bifrost Parameters: |
+=====+===+====+====+===+=====+
| Ca  | U | Uv | d  | e |   E |
+-----+---+----+----+---+-----+ 
| 0.01|0.3|0.1 | 0.5|0.5|0.9  |
+-----+---+----+----+---+-----+


Comparing densities in the x/y/z direction
------------------------------------------

The figure below shows the result of the denisties computed in each direction from the three input files.
These were configured with the initial Bifrost Parameters listed in the above table. 

.. image:: images_brio-wu_bifrost/brio-wu_density_all.png

All density profiles overlap.  



Initial adjustments of the individual bifrost parameters
--------------------------------------------------------
We adjust the bifrost parameters one by one while the remaining five parameters are held fixed. Initially, each parameter is increased by a factor 10 except from E, since E=9.0 led to an error while running. E is therefore increased by a factor of 5 initially. We also reduce each parameter by a factor of 10, and compare with the original results. The figures below we plot the resulting densities, the x-components of the velocity and the y-components of the magnetic field. The figures on the left shows the result of parameter increase, while the figures on the right shows the parameter reductions. Each figure has a legend indicating which parameter has been adjusted, includnig its corresponding value. The original parameter result is included in all plots. 

We start with the density, shown below. 

.. image:: images_brio-wu_bifrost/brio-wu_init_adjust_rho.png  
        :width: 45 %
.. image:: images_brio-wu_bifrost/brio-wu_init_reduced_rho.png 
        :width: 45 %

Image below shows the resulting velocities in x-direction from the parameter adjustments. 

.. image:: images_brio-wu_bifrost/brio-wu_init_adjust_ux.png
        :width: 45 %
.. image:: images_brio-wu_bifrost/brio-wu_init_reduced_ux.png
        :width: 45 %

Below shows the y-component of the Magnetic field in the x-direction from the parameter adjustments. 

.. image:: images_brio-wu_bifrost/brio-wu_init_adjust_by.png
        :width: 45 %
.. image:: images_brio-wu_bifrost/brio-wu_init_reduced_by.png
        :width: 45 %

The increase of the bifrost parameter E visibly affects all quantities. Another noticeable quantity is U, which is evident in all plots where it has been decreased. Another parameter affecting the result is the increased d. This is easiest to see in the plot of the x-velocity, where it lies above the other lines for 0.7<x<0.8. We adjust these parameters further to study their behaviour individually. 


Single parameter adjustments
............................

Adjusting U-parameter:

.. image:: images_brio-wu_bifrost/U-adjust_initial/brio-wu_U-adjust_rho.png

.. image:: images_brio-wu_bifrost/U-adjust_initial/brio-wu_U-adjust_ux.png

.. image:: images_brio-wu_bifrost/U-adjust_initial/brio-wu_U-adjust_by.png


Adjusting d-parameter:

.. image:: images_brio-wu_bifrost/d-adjust_initial/brio-wu_d-adjust_rho.png

.. image:: images_brio-wu_bifrost/d-adjust_initial/brio-wu_d-adjust_ux.png

.. image:: images_brio-wu_bifrost/d-adjust_initial/brio-wu_d-adjust_by.png


Adjusting E-parameter:

.. image:: images_brio-wu_bifrost/E-adjust_initial/brio-wu_E-adjust_rho.png

.. image:: images_brio-wu_bifrost/E-adjust_initial/brio-wu_E-adjust_ux.png

.. image:: images_brio-wu_bifrost/E-adjust_initial/brio-wu_E-adjust_by.png


Reduced resolution
------------------
In the cartesian_params we use size=1 in the x-direction with dims=5. All previous runs have used n=[100,1,1] in the patch_params. We now make plots with half the original resolution, using n=[50,1,1]. The plots below shows the resulting density, x-velocity and y-component of the Magnetic field, respectively. 

.. image:: images_brio-wu_bifrost/resolution_decrease/brio-wu_bifrost_n50_rho.png 

.. image:: images_brio-wu_bifrost/resolution_decrease/brio-wu_bifrost_n50_ux.png 

.. image:: images_brio-wu_bifrost/resolution_decrease/brio-wu_bifrost_n50_by.png 



Ramses/mhd_eos results
----------------------

We run the same experiment with the solver ramses/mhd_eos. The quantities listed in the tables above are unchanged. 
For this solver we set the ramses_params initially as:
        * slope_type = 3.5

Below is the density in all directions. 

.. image:: images_ramses_brio-wu/brio-wu_ramses_xyz_rho.png

After the above image were produced, an error in the solver was discovered and fixed. We update the solver before continuing testing. The following studies are completed with:
        * Branch: develop
        * hash: 5e8f853


Densities with updated solver:
-----------------------------
The density in the x/y/z direction with the updated solver is plotted below. 

.. image:: images_ramses_brio-wu/brio-wu_ramses_xyz_rho_updated.png



Adjusting the ramses_params
--------------------------
We now plot the density, x-velocity and y-component of the magnetic field in the x direction respectiely. In each plot we test different values of slope_types. The parameter option slope_types=-1 is omitted, as the program was unable to finish for this particular parameter. 

The density is shown in the figure below 

.. image:: images_ramses_brio-wu/brio-wu_ramses_x-slopes_rho.png

Below is the x-component of the velocity 

.. image:: images_ramses_brio-wu/brio-wu_ramses_x-slopes_ux.png

The y-component of the mangetic field is shown below 

.. image:: images_ramses_brio-wu/brio-wu_ramses_x-slopes_by.png


Comparing resolution with ramses/mhd_eos solver 
---------------------------------------
Having used n=100 with dims=5 in the x-direction for the previous plots, we will compare these results with the ones we get from setting n=50.
During the comparison tests we will continue to use slope_type=3.5. We begin by comparing the resulting densities, shown in the figure below. 

.. image:: images_ramses_brio-wu/brio-wu_ramses_n50_rho.png


Now we compare the velocity in the x-direction

.. image:: images_ramses_brio-wu/brio-wu_ramses_n50_ux.png

Finally, we compare the y-component of the magnetic field

.. image:: images_ramses_brio-wu/brio-wu_ramses_n50_by.png


references


