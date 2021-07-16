import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import matplotlib
import matplotlib.pyplot as plt

#run outside the python directory inside the experiment
data='data/'

run_name = ['brio-wu_ramses_x',
            'brio-wu_ramses_x_slope3',
            'brio-wu_ramses_x_slope2',
            'brio-wu_ramses_x_slope1']


run_adjustments = ['3.5 (original)', '3', '2', '1']
# run_adjustments = ['U=0.1', 'U=0.2', 'U=0.3 (original)', 'U=0.4', 'U=0.5']
# run_adjustments = ['d=0.5 (original)', 'd=2.0', 'd=3.5', 'd=5.0', 'd=6.5']
lines = ['solid', '-.', '-.', ':']
labels = [r'$\rho$', 'v_x', '$B_x$']

def plot_params(param=['d', 'ux', 'by']):

    fig_number = 1

    for p in param:

        fig_titles = [r'Brio-wu ramses/mhd_eos: $\rho$',
                    'Brio-wu ramses/mhd_eos: x-velocities',
                    'Brio-wu ramses/mhd_eos: $B_y$',]

        fig_names = ['rho', 'ux', 'by']

        run_number = 0

        for run in run_name:
            ss=[]

            #load data from all plot files
            for i in range(0,11):
              s=dispatch.snapshot(i,run=run,data=data, verbose=0)
              ss.append(s)


                #plot density
            plt.figure(fig_number)
            dg.plot_values_along(ss[10],[0.00,0.000,0.000],dir=0,iv=p, ls=lines[run_number], \
                                label='slope=' + run_adjustments[run_number])
            run_number += 1

        plt.title(fig_titles[fig_number-1])
        plt.xlabel('x')
        plt.ylabel(labels[fig_number-1])
        plt.grid()
        plt.legend()


        path_to_figure = '.'
        plt.figure(fig_number)
        plt.savefig(path_to_figure+'/brio-wu_ramses_x-slopes_'+fig_names[fig_number-1]+'.png')

        fig_number += 1

plot_params()
