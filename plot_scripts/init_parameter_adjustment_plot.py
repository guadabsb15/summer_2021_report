import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import matplotlib
import matplotlib.pyplot as plt

#run outside the python directory inside the experiment
data='data/'

run_name = ['brio-wu_bifrost_x',
            'brio-wu_bifrost_mod_x1',
            'brio-wu_bifrost_mod_x2',
            'brio-wu_bifrost_mod_x3',
            'brio-wu_bifrost_mod_x4',
            'brio-wu_bifrost_mod_x5',
            'brio-wu_bifrost_mod_x6']

run_adjustments = ['Unadjusted', 'Ca=0.1', 'U=3.0', 'Uv=1.0', 'd=5.0', 'e=5.0', 'E=5.0']
lines = ['solid','--','--','-.','-.',':',':']

run_number = 0

for run in run_name:
    ss=[]

    #load data from all plot files
    for i in range(0,11):
      s=dispatch.snapshot(i,run=run,data=data, verbose=0)
      ss.append(s)

    #plot density
    plt.figure(1)
    if run_number==0:
        for i in (0, 10):
            dg.plot_values_along(ss[i],[0.00,0.000,0.000],dir=0,iv='d', ls=lines[run_number], label=run_adjustments[run_number])

    else:
        dg.plot_values_along(ss[10],[0.00,0.000,0.000],dir=0,iv='d', ls=lines[run_number], label=run_adjustments[run_number])

    plt.title(r'Brio-wu bifrost: Densities with each bifrost_params adjusted')
    plt.xlabel('x')
    plt.ylabel(r'$\rho$')
    plt.grid()
    plt.legend()

    run_number += 1

path_to_figure = '.'
plt.figure(1)
plt.savefig(path_to_figure+'/brio-wu_init_adjust_rho.png')
