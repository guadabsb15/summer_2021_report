import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import matplotlib
import matplotlib.pyplot as plt

#run outside the python directory inside the experiment
data='data/'

run_name = ['brio-wu_bifrost_x', 'brio-wu_bifrost_y', 'brio-wu_bifrost_z']
coordinate = ['x', 'y', 'z']
lines = ['--','-.',':']

direction = 0

for run in run_name:
    ss=[]

    #load data from all plot files
    for i in range(0,11):
      s=dispatch.snapshot(i,run=run,data=data, verbose=0)
      ss.append(s)

    #plot density
    plt.figure(1)

    if direction == 0:
        dg.plot_values_along(ss[0],[0.00,0.000,0.000],dir=direction,iv='d', ls='solid', label='Initial condition x/y/z')



    dg.plot_values_along(ss[10],[0.00,0.000,0.000],dir=direction,iv='d', ls=lines[direction], label=coordinate[direction])

    plt.title(r'Brio-wu bifrost: $\rho$')
    plt.xlabel('x/y/z')
    plt.ylabel(r'$\rho$')
    plt.grid()
    plt.legend()

    direction += 1

path_to_figure = '.'
plt.figure(1)
plt.savefig(path_to_figure+'/brio-wu_test_rho.png')
