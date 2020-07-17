# -*- coding: utf-8 -*-

# BCDI: tools for pre(post)-processing Bragg coherent X-ray diffraction imaging data
#   (c) 07/2017-06/2019 : CNRS UMR 7344 IM2NP
#   (c) 07/2019-present : DESY PHOTON SCIENCE
#       authors:
#         Jerome Carnis, carnis_jerome@yahoo.fr

import os
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog
import sys
sys.path.append('C:/Users/Jerome/Documents/myscripts/bcdi/')

helptext = """
Load the output file of xcca_3D.py and plot the cross-correlation function.

Input: a NPZ file with the fields 'angles', 'ccf', 'points': 
    - 'angles' are the values between [0, 180] where the cross-correlation function was calculated
    - 'ccf' are the the cross-correlation function values at these angles
    - 'points' are the number of points contributing to the cross-correlation function at these angles
"""

datadir = "D:/data/P10_August2019_CDI/data/gold_2_2_2_00022/pynx/1_4_4_fullrange_xcca/"
savedir = "D:/data/P10_August2019_CDI/data/gold_2_2_2_00022/pynx/1_4_4_fullrange_xcca/"
comment = ''  # should start with _
ylim = None  # [0, 60]  # limits used for the vertical axis of plots, leave None otherwise
##########################
# end of user parameters #
##########################

###################################
# load the cross-correlation data #
###################################
plt.ion()
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir=datadir, title="Select the CCF file",
                                       filetypes=[("NPZ", "*.npz")])
filename = os.path.splitext(os.path.basename(file_path))[0]  # the extension .npz is removed
npzfile = np.load(file_path)
try:
    ccf = npzfile['ccf']
except KeyError:
    ccf = npzfile['corr']
try:
    angles = npzfile['angles']
    points = npzfile['points']
except KeyError:
    print('Keys in the NPZ file:', list(npzfile.keys()))
    sys.exit()

#######################################
# plot the cross-correlation function #
#######################################
fig, ax = plt.subplots(1, 1)
ax.plot(angles, ccf, linestyle='None', marker='.', markerfacecolor='blue')
if ylim is not None:
    ymin, ymax = ylim
else:
    ymin, ymax = np.floor(ax.get_ylim())
ax.set_xlim(0, 180)
ax.set_ylim(ymin, ymax)
ax.set_xlabel('Angle (deg)')
ax.set_ylabel('Cross-correlation')
ax.set_xticks(np.arange(0, 181, 30))
ax.set_title('CCF' + comment)
fig.savefig(savedir + filename + comment + '_ylim[{:.1f},{:.1f}]'.format(ymin, ymax)+'.png')

_, ax = plt.subplots()
ax.plot(angles, points, linestyle='None', marker='.', markerfacecolor='blue')
ax.set_xlim(0, 180)
ax.set_xlabel('Angle (deg)')
ax.set_ylabel('Number of points')
ax.set_xticks(np.arange(0, 181, 30))
ax.set_title('Points per angular bin')

plt.ioff()
plt.show()
