import f90nml
import numpy as np
import sys


class nml_params:
    """
    Edit nml-files for verification tests. Creates copy of input file.
    Includes option for editing environment paramaters,
    bifrost parameters and ramses parameters
    """

    def __init__(self, filename):
        self.filename = filename
        self.nml = f90nml.read(filename) # Contains the nml file. Dictionary
        self.bf_params = self.nml['bifrost_params']['nu'] # List of Bifrost paramters
        self.ramses_params = self.nml['ramses_params']['slope_type'] # Value of slope_type, default=3.5
        self.box_size = self.nml['patch_params']['n'] # [x,y,z] number of points in grid cells
        self.IC = self.nml['IC_params'] # Physical parameters, density, velocities etc.


    def patch_bifrost_params(self, param_list, name):
        # Generates new nml file with updated bifrost_params.

        patch_nml = {'bifrost_params': {'nu': param_list}} # the updated parameter values
        mod_name = self.filename[:-4] + name + '.nml' # name of the output file

        f90nml.patch(self.filename, patch_nml, mod_name) # Create the new nml file

    def decrease_resolution(self, name):
        # Create file with reduced box_size in x-direction

        new_box_size = [50, 1, 1] # [x,y,z]
        patch_nml = {'patch_params': {'n': new_box_size}}
        mod_name = self.filename[:-4] + name + '.nml'

        f90nml.patch(self.filename, patch_nml, mod_name)

    def mag_field(self):
        # Permutation of magnetic field components
        # For generating the corresponding nml-files in y and z direction

        IC = self.IC
        IC_y = IC.copy()
        IC_z = IC.copy()

        mag_x = ['Bx_l', 'By_l', 'Bz_l', 'Bx_r', 'By_r', 'Bz_r']
        mag_y = ['Bz_l', 'Bx_l', 'By_l', 'Bz_r', 'Bx_r', 'By_r']
        mag_z = ['By_l', 'Bz_l', 'Bx_l', 'By_r', 'Bz_r', 'Bx_r']


        for i in range(len(mag_x)):
            IC_y[mag_x[i]] = IC[mag_y[i]]
            IC_z[mag_x[i]] = IC[mag_z[i]]

        return IC_y, IC_z


    def create_yz(self, magnetic_field=True):
        # Create y and z copies of nml file
        # Includes option for permutating magnetic field

        cart_params = self.nml['cartesian_params']
        p_params    = self.nml['patch_params']

        size_y  = [0.003, 1, 0.003]
        dims_y  = [1, 5, 1]
        n_y     = [1, 100, 1]
        periodic_y = [True, False, True]

        size_z  = [0.003, 0.003, 1]
        dims_z  = [1, 1, 5]
        n_z     = [1, 1, 100]
        periodic_z = [True, True, False]


        if magnetic_field==True:
            # Permutates the magnetic field values
            IC_y, IC_z = self.mag_field()
        else:
            IC_y = self.IC.copy()
            IC_z = self.IC.copy()

        IC_y['idir'] = 2
        IC_z['idir'] = 3

        patch_y = {'cartesian_params': {'size': size_y,
                                        'dims': dims_y,
                                        'periodic': periodic_y},
                    'patch_params': {'n': n_y},
                    'IC_params': IC_y}



        patch_z = {'cartesian_params': {'size': size_z,
                                        'dims': dims_z,
                                        'periodic': periodic_z},
                    'patch_params': {'n': n_z},
                    'IC_params': IC_z}

        y_name = self.filename[:-5] + 'y.nml'
        z_name = self.filename[:-5] + 'z.nml'

        f90nml.patch(self.filename, patch_y, y_name)
        f90nml.patch(self.filename, patch_z, z_name)


    def increase_all_bifrost_params(self, factor=10, five_idx=[]):
        """
        Create six nml files with each bifrost_param adjusted individually
        Option for increasing certain parameters by a factor of 5 only
        Useful when factor 10 increments causes experiment to crash
        """

        factors = [factor]*6

        for idx in five_idx:
            ### use factor of 5 for a given parameter
            factors[idx] /= 2

        for i in range(6):
            ### Scale each parameter and create a new nml file for each adjustment
            params = self.bf_params.copy()

            params[i] *= factors[i]
            name = '_mod_reduced' + str(i+1)

            self.patch_bifrost_params(params, name)


    def single_bifrost_param_adjustment(self, idx, values = []):
        """
        Create individual nml file for subsequent adjustments of one bifrost_param
        """
        param_name = ['Ca', 'U', 'Uv', 'd', 'e', 'E']

        mod_no = 0 # For naming the file(s)
        for val in values:
            params = self.bf_params.copy()

            params[idx] = val
            name = '_mod_' + param_name[idx] + '_' + str(mod_no+1)

            self.patch_bifrost_params(params, name)

            mod_no += 1


    def ramses_slopes(self):
        # Create nml-files for all slope_type values available
        # slope_type=-1 may cause crash
        slopes = self.ramses_params
        new_slopes = [3, 2, 1, -1]
        for val in new_slopes:

            patch = {'ramses_params': {'slope_type': val}}
            name = self.filename[:-4] + '_slope' + str(val) + '.nml'

            f90nml.patch(self.filename, patch, name)


brio_wu = nml_params('brio-wu_ramses_x.nml')
# brio_wu.create_yz()
brio_wu.ramses_slopes()
# brio_wu.mag_field()
# brio_wu.decrease_resolution(name='_n50')
# brio_wu.increase_all_bifrost_params(factor=0.1, five_idx=[5])
# E_values = [0.4, 0.9, 1.4, 1.9]
# U_values = [0.1, 0.2, 0.3, 0.4, 0.5]
# d_values = [0.5, 2, 3.5, 5, 6.5]
# brio_wu.single_bifrost_param_adjustment(idx=5, values=E_values)
# brio_wu.single_bifrost_param_adjustment(idx=1, values=U_values)
# brio_wu.single_bifrost_param_adjustment(idx=3, values=d_values)
