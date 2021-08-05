"""
create_snaps.py

Created by Mikolaj Szydlarski on 2019-06-03
Copyright (c) 2019, ITA UiO - All rights reserved.
"""

import numpy as np

N_x     = 1 # number of grid points ( for N x N domain )
N_y     = 128
N_z     = 256


def get_faces(f):
   '''
   [Stagger] f is centered on (i-.5,j,k)
   '''

   # expand x on both ends with nm cels

   nb = 5
   fp = np.hstack((np.zeros(nb),f,np.zeros(nb)))

   # interpolate edges

   # bottom (left)
   for i in range(1,nb+1):
      fp[nb-i] = 2.*fp[nb]-fp[nb+i]
   xe = nb + f.shape[0] - 1
   for i in range(1,nb+1):
      fp[xe+i] = 2.*fp[xe]-fp[xe-i]

   nx = len(fp)
   d =   -5. / 2048
   c =   49. / 2048
   b = -245. / 2048
   a = .5 - b - c - d
   x = (a * (fp + np.roll(fp, 1)) +
        b * (np.roll(fp, -1) + np.roll(fp, 2)) +
        c * (np.roll(fp, -2) + np.roll(fp, 3)) +
        d * (np.roll(fp, -3) + np.roll(fp, 4)))
   return x[nb+1:-(nb-1)]

y = np.linspace(0.0,0.5,N_y,endpoint=True)
z = np.linspace(0.0,1.0,N_z,endpoint=True)

# Shift x and y with stagger routine

y_half = get_faces(y)
z_half = get_faces(z)

yv, zv = np.meshgrid(y, z, sparse=False, indexing='xy')
yv_h, zv_h = np.meshgrid(y_half, z_half, sparse=False, indexing='xy')

# Create empty arrays

tmp = np.zeros_like(yv) # tmp array
rho = np.zeros_like(yv) # density

ux  = np.zeros_like(yv)
uy  = np.zeros_like(yv)
uz  = np.zeros_like(yv)

px  = np.zeros_like(yv)
py  = np.zeros_like(yv)
pz  = np.zeros_like(yv)

bx  = np.zeros_like(yv)
by  = np.zeros_like(yv)
bz  = np.zeros_like(yv)

e   = np.zeros_like(yv)

# Solar units (not used here)

# u_l  = 1e8
# u_t  = 1e2
# u_r  = 1e-7
# u_u  = u_l/u_t
# u_p  = u_r*(u_l/u_t)**2 # pressure [dyne/cm2]
# u_ee = u_u**2
# u_e  = u_r*u_ee
# u_B  = u_u*np.sqrt(4.*np.pi*u_r)

# Fill MHD variables with values

ux.fill(0.0) # velocity zero everywhere
uy.fill(0.0)
uz.fill(0.0)

bx.fill(0.0) # magnetic fields zero everywhere
by.fill(0.0)
bz.fill(0.0)

d1 = 1.0
d2 = 2.0
z0 = 0.5
deltaz= 0.025
deltavz = 0.025
z_grav_acc = -0.5

zmin = 0.3
zmax = 0.7

gamma = 1.4

for j in range(len(y)):
  for k in range(len(z)):
    rho[k,j] = d1 + (d2-d1) / (1.0+np.exp((z0-z[k])/deltaz))
    #if j/len(y) >= dymin and j/(len(y)) <= dymax:
    #  uz[k,j] = deltavz * (1.0+np.cos(8.0*np.pi*(y_half[j]+0.25))) * (1.0+np.cos(5.0*np.pi*(z_half[k]+0.5)))
    #else:
    uz[k,j] = deltavz * (1.0+np.cos(8.0*np.pi*(y_half[j]+0.25))) * (1.0+np.cos(5.0*np.pi*(z_half[k]+0.5)))
    tmp[k,j] = d2 / gamma + z_grav_acc * rho[k,j] * (z[k] - z0)


# Calculate e from pressure using Ideal gas
e = tmp / (gamma - 1.0) # translate pressure to internal energy

# Calculate moementum from velocities / no need for stagger since rho is uniform

px = rho * ux
py = rho * uy
pz = rho * uz

#  Write snapshots
file_name_template  = 'rt.snap'

shape = (N_x,N_y,N_z,8)
snap = np.zeros(shape=shape)

snap[0,:,:,0] = np.transpose(rho[:,:]) # / u_r
snap[0,:,:,1] = np.transpose(py[:,:]) # / (u_u * u_r)
snap[0,:,:,2] = np.transpose(px[:,:]) # / (u_u * u_r)
# make fingers centered
snap[0,:,:,3] = np.roll(-np.transpose(pz[:,:]), N_y//4, axis=0) # / (u_u * u_r)
snap[0,:,:,4] = np.transpose(e[:,:]) # already in bifrost units becouse of u_p
snap[0,:,:,5] = np.transpose(by[:,:]) # / u_B
snap[0,:,:,6] = np.transpose(bx[:,:]) # / u_B
snap[0,:,:,7] = np.transpose(bz[:,:]) # / u_B

data = np.memmap(file_name_template, dtype='float32', mode='w+', order='f',shape=shape)
data[:,:,:,:] = snap[:,:,:,:]
data.flush()

# Calculate dx,dy and change in template

dx = 1
dy = 0.5/N_y
dz = 1.0/N_z

# Change template accodring to new N

mhd_template = dict() # empty dictionary

mhd_template['mx'] = N_x
mhd_template['my'] = N_y
mhd_template['mz'] = N_z
mhd_template['periodic_x'] = 1
mhd_template['periodic_y'] = 1
mhd_template['periodic_z'] = 0
mhd_template['ndim'] = 2
mhd_template['dx'] = dx
mhd_template['dy'] = dy
mhd_template['dz'] = dz
mhd_template['Cdt'] = 0.3
mhd_template['dt'] = 1e-7
mhd_template['do_mhd'] = 1
mhd_template['gamma'] = gamma
mhd_template['nsnap']  = 5000000
mhd_template['nscr']   = 5000000
mhd_template['dtsnap'] = 0.5
mhd_template['nstep']  = 1000000
mhd_template['t'] = 0.0
mhd_template['tstop'] = 5.0
mhd_template['one_file'] = 0
mhd_template['snapname'] = '\"rt\"'
mhd_template['aux'] = '\" p \"'
mhd_template['isnap'] = 0
mhd_template['grav'] = 0.5
mhd_template['nu1'] = 0.1
mhd_template['nu2'] = 0.1
mhd_template['nu3'] = 0.5
mhd_template['nu_r'] = 0.3


# Save mhd.in as sb.idl

with open('rt.idl','w') as f:
  for k, v in mhd_template.items():
      f.write('%015s = %s\n' % (str(k),str(v)))
