import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import matplotlib
import matplotlib.pyplot as plt

#run outside the python directory inside the experiment
data='data/'

run_name = ['brio-wu_bifrost_x_n50', 'brio-wu_bifrost_x']
quantites = ['d', 'ux', 'by']
labels = [r'$\rho$', 'v_x', '$B_y$']
fig_names = ['rho', 'ux', 'by']


run_number = 0



ss_50=[]
ss_100=[]
#load data from all plot files
for i in range(0,11):
    s_50=dispatch.snapshot(i,run=run_name[0], data=data, verbose=0)
    s_100=dispatch.snapshot(i,run=run_name[1], data=data, verbose=0)
    ss_50.append(s_50)
    ss_100.append(s_100)

for q in quantites:
    #plot density
    plt.figure(run_number+1)

    dg.plot_values_along(ss_50[10], [0.00,0.000,0.000],dir=0,iv=q, ls='solid', label='n=50')
    dg.plot_values_along(ss_100[10],[0.00,0.000,0.000],dir=0,iv=q, ls='solid', label='n=100')

    plt.title(r'Brio-wu bifrost, compare resolution: ' + labels[run_number])
    plt.xlabel('x')
    plt.ylabel(labels[run_number])
    plt.grid()
    plt.legend()
    path_to_figure = '.'
    plt.figure(run_number + 1)
    plt.savefig(path_to_figure+'/brio-wu_bifrost_n50_' + fig_names[run_number] + '.png')

    run_number += 1
