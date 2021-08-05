#!/usr/bin/env python

"""
create_mf_snap.py

Created by Mikolaj Szydlarski on 2014-04-29.
Copyright (c) 2018, ITA UiO - All rights reserved.
"""
import numpy as np
import pylab as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['font.size'] = 11

colours = {1:'b',3:'g',5:'r'}

# ### Set number of snaps

nsnap    = 1
with_aux = True
with_mhd = True

# ### Read params ###########################################################################################

def read_params(filename):
    ''' Reads params file into dictionary '''

    params = {}

    # go through the file, add stuff to dictionary
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if len(line) <= 1:
                continue
            if line[0] == ';':
                continue

            line = line.split(';')[0].split('=')

            key   = line[0].strip().lower() # force lowercase because IDL is case-insensitive
            value = line[1].strip()

            if (value.find('"') >= 0):
                value = value.strip('"')
            elif (value.find('[') >= 0 and value.find(']') >= 0):
                value = eval(value)
            elif (value.find("'") >= 0):
                value = value.strip("'")
            elif (value.lower() in ['.false.', '.true.']):
                value = False if value.lower() == '.false.' else True
            elif ((value.upper().find('E') >= 0) or (value.find('.') >= 0 )):
                value = float(value)
            else:
                try:
                    value = int(value)
                except:
                    print('Value exception')
                    continue
            params[key] = value

        return params

def make_plot(snap):
  #### Read mhd for init parameters

  if snap == "rt_final":
    params = read_params('./rt.idl.scr')
  else:
    params = read_params(snap+".idl")

  base_name   = params['snapname']
  nx          = params['mx']
  ny          = params['my']
  nz          = params['mz']

  snap_shape = (nx,ny,nz,8)
  if snap == "rt_final":
    snap_data   = np.memmap('rt.snap.scr', dtype='float32', mode='r',order='f',shape= snap_shape)
  else:
    snap_data   = np.memmap(snap+".snap", dtype='float32', mode='r',order='f',shape= snap_shape)

  r    = [0.0,0.5,0.0,1.0]

  # Density plot
  rho = np.transpose(snap_data[0,:,:,0])
  uz = np.transpose(snap_data[0,:,:,3])
  e  = np.transpose(snap_data[0,:,:,4])

  fig, ax = plt.subplots()

  ax.set_title('density for t = %.2f' % params['t'])
  ax.set_xlabel('y-axis')
  ax.set_ylabel('z-axis')

  im = ax.imshow(
      np.squeeze(rho),
      origin='lower',
      extent=r,
      #norm=colors.Normalize(vmin=rho.min(),vmax=rho.max()),
      vmin=0.5, vmax=2.5,
      interpolation='none',
      cmap='jet')
  ax.set_xlim([0.0,0.5])
  ax.set_ylim([0.0,1.0])
  ax.grid(False)

  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="5%", pad=0.05)
  rt = np.linspace(0.5,2.5,9,endpoint=True)
  plt.colorbar(im, cax=cax, ticks=rt)
  plt.savefig('rho{}.png'.format(snap.strip("rt")),dpi=150)
  plt.close()

  #velocity in z
  fig, ax = plt.subplots()

  ax.set_title('uz for t = %.2f' % params['t'])
  ax.set_xlabel('y-axis')
  ax.set_ylabel('z-axis')

  im = ax.imshow(
      np.squeeze(uz),
      origin='lower',
      extent=r,
      norm=colors.Normalize(vmin=uz.min(),vmax=uz.max()),
      interpolation='none',
      cmap='jet')
  ax.set_xlim([0.0,0.5])
  ax.set_ylim([0.0,1.0])
  ax.grid(False)

  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="5%", pad=0.05)
  rt = np.linspace(uz.min(),uz.max(),10,endpoint=True)
  plt.colorbar(im, cax=cax, ticks=rt)
  plt.savefig('uz{}.png'.format(snap.strip("rt")),dpi=150)
  plt.close()

  #energy
  fig, ax = plt.subplots()

  ax.set_title('e for t = %.2f' % params['t'])
  ax.set_xlabel('y-axis')
  ax.set_ylabel('z-axis')

  im = ax.imshow(
      np.squeeze(e),
      origin='lower',
      extent=r,
      norm=colors.Normalize(vmin=e.min(),vmax=e.max()),
      interpolation='none',
      cmap='jet')
  ax.set_xlim([0.0,0.5])
  ax.set_ylim([0.0,1.0])
  ax.grid(False)

  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="5%", pad=0.05)
  rt = np.linspace(e.min(),e.max(),10,endpoint=True)
  plt.colorbar(im, cax=cax, ticks=rt)
  plt.savefig('e{}.png'.format(snap.strip("rt")),dpi=150)
  plt.close()

make_plot("rt_final")

# to view time evolution, gives several figures
#snaps = ["rt_001",
#         "rt_002",
#         "rt_003",
#         "rt_004",
#         "rt_005",
#         "rt_006",
#         "rt_007",
#         "rt_008",
#         "rt_009",
#         "rt_final"]

#for snap in snaps:
#  make_plot(snap)
