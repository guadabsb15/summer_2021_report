import dispatch
import dispatch.select as ds
import dispatch.graphics as dg
import matplotlib
import matplotlib.pyplot as plt

#run outside the python directory inside the experiment
data='data/'

# Names of the data folders 
run_name = ['brio-wu_bifrost_x', 'brio-wu_bifrost_y', 'brio-wu_bifrost_z']
coordinate = ['x', 'y', 'z']
lines = ['--','-.',':']

direction = 0


for run in run_name:
  ss=[]
  #I know the last snapshot number is 10
  s=dispatch.snapshot(10,run=run,data=data, verbose=0)
  ss.append(s)

  #plot density
  plt.figure(1)
  dg.plot_values_along(ss[0],[0.00,0.000,0.000],dir=direction,iv='d', ls=lines[direction], label=coordinate[direction])
  plt.title(r'Brio-wu bifrost: $\rho$')
  plt.xlabel(r'$x/y/z$')
  plt.ylabel(r'$\rho$')
  plt.grid()
  plt.legend()


  direction = direction +1

path_to_figure = '.'
plt.figure(1)
plt.savefig(path_to_figure+'/brio-wu_test_rho.png')
