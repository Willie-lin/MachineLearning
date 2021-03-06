#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      : 
# @File      : DripDrop.py
# @Time      : 2018/6/6 11:30
# @software  : PyCharm

# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# New figure with white background
fig = plt.figure(figsize=(6, 6), facecolor='white')

# New axis over the whole figureand a 1:1 aspect ratio
ax = fig.add_axes([0.005, 0.005, .99, .99], frameon=True, aspect=1)

# Number of ring
n = 50
size_min = 50
size_max = 50 * 50

# Ring position
P = np.random.uniform(0, 1, (n, 2))

# Ring colors
C = np.ones((n, 4)) * (0, 0, 0, 1)

# Alpha color channel goes from 0 (transparent) to 1 (opaque)
C[:, 3] = np.linspace(0, 1, n)

# Ring sizes
S = np.linspace(size_min, size_max, n)

# Scatter plot
scat = ax.scatter(P[:, 0], P[:, 1], s=S, lw=0.5,
                  edgecolors=C, facecolors='None')

# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# plt.savefig("../figures/rain-static.png",dpi=72)
plt.show()