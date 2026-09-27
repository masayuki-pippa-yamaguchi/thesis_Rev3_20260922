# fig_multiplicative_log_linear_v3.py

import numpy as np
import matplotlib.pyplot as plt
import os

OUTDIR = "d:/texlive/2026/work/thesis_Rev3_20260922"
os.makedirs(OUTDIR, exist_ok=True)

# -----------------------------
# (a) multiplicative structure
# -----------------------------
t = np.linspace(0, 5, 500)
mu = 1.0
sigma = 0.15

np.random.seed(0)
W = np.random.normal(0, np.sqrt(1/500), size=500).cumsum()
V = np.exp(mu * t + sigma * W)

plt.figure(figsize=(5, 3))
plt.plot(t, V, color="darkblue")
plt.title("(a) Multiplicative structure")
plt.xlabel("t")
plt.ylabel("V(t)")
plt.tight_layout()
plt.savefig(f"{OUTDIR}/multiplicative_structure.png", dpi=300)
plt.close()

# -----------------------------
# (b) log transform
# -----------------------------
logV = np.log(V)

plt.figure(figsize=(5, 3))
plt.plot(t, logV, color="darkgreen")
plt.title("(b) Log transform")
plt.xlabel("t")
plt.ylabel("log V(t)")
plt.tight_layout()
plt.savefig(f"{OUTDIR}/log_transform.png", dpi=300)
plt.close()

# -----------------------------
# (c) linear DD structure
# -----------------------------
log_ratio = np.linspace(-1.0, 1.0, 200)
DD = log_ratio

plt.figure(figsize=(5, 3))
plt.plot(log_ratio, DD, color="darkred")
plt.title("(c) Linear DD structure")
plt.xlabel("log(V/F)")
plt.ylabel("DD")
plt.tight_layout()
plt.savefig(f"{OUTDIR}/linear_dd.png", dpi=300)
plt.close()
