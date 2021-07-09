Brio& Wu experimemts 
=========================

Here we will report the results of the Brio&Wu experiment


Bifrost Solver 
---------------------
The following input parameters were used for all three directions:

+----------+----------+-----------+
| Quantity |Left state|Right state|
+==========+==========+===========+
| rho      | 1        | 0.125     |
+----------+----------+-----------+
| v_x      |  0       | 0         |
+----------+----------+-----------+
| v_y      |  0       | 0         |
+----------+----------+-----------+
| v_z      |  0       | 0         |
+----------+----------+-----------+
| B_x      |  0.75    | 0.75      |
+----------+----------+-----------+
| B_y      |  1       | -1        |
+----------+----------+-----------+
| B_z      |  0       | 0         |
+----------+----------+-----------+
| P        |  1       | 0.1       |
+----------+----------+-----------+

For the y and z direction the same parameters were used, but with a periodic permutation on the mangetic field parameters. 


           +-------------------------------------+
           |  Simulation direction               |
+----------+-------------+-----------+-----------+
|Quantity  |  x          |    y      | z         |
|          +------+------+-----+-----+-----+-----+
|          |Left  |Right |Left |Right|Left |Right|            
+----------+------+------+-----+-----+-----+-----+
| B_x      | 0.75 | 0.75 | 0   | 0   | 1   | -1  |
+----------+------+------+-----+-----+-----+-----+
| B_y      |  1   | -1   | 0.75|0.75 | 0   | 0   |
+----------+------+------+-----+-----+-----+-----+
| B_z      |  0   | 0    | 1   | -1  | 0.75| 0.75|
+----------+------+------+-----+-----+-----+-----+


initial contidions

different directions
different solvers

references


