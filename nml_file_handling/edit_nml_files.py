import f90nml
import sys


class nml_params:
    """
    Edit nml-file parameters.
    Options available:
      - Change initial bifrost parameters subsequently
      - Make multiple changes to a single bifrost parameter
      - Reduce box resolution
    """

    def __init__(self, filename):
        self.filename = filename
        self.nml = f90nml.read(filename) # Contains the entire nml file
        self.bf_params = self.nml['bifrost_params']['nu'] # List of Paramters to adjust
        self.box_size = self.nml['patch_params']['n'] # Resolution of experiment


    def patch_bifrost_params(self, param_list, name):
        """
        Generates the new nml file with updated bifrost_params.
        Everything but the relevant parameters are left unchanged
        """
        patch_nml = {'bifrost_params': {'nu': param_list}} # the updated parameter values
        mod_name = self.filename[:-4] + name + '.nml' # name of the output file

        f90nml.patch(self.filename, patch_nml, mod_name) # Create the new nml file

    def decrease_resolution(self, name):
        """
        Create file with reduced box_size
        """
        new_box_size = [50, 1, 1] # New box size
        patch_nml = {'patch_params': {'n': new_box_size}}
        mod_name = self.filename[:-4] + name + '.nml'
        f90nml.patch(self.filename, patch_nml, mod_name)


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


brio_wu = nml_params('brio-wu_bifrost_x.nml')
brio_wu.decrease_resolution(name='_n50')
