import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(page_title="Double-slit Simulation", layout="centered")
st.title("Double-slit Interference Simulation (with Single-slit Diffraction)")

# Parameter controls
lambda_nm = st.slider("波长 λ (nm)", 400.0, 700.0, 633.0)
d_mm = st.slider("双缝间距 d (mm)", 0.1, 0.5, 0.2)
a_mm = st.slider("单缝宽度 a (mm)", 0.01, 0.1, 0.05)
D_m = st.slider("屏幕距离 D (m)", 0.5, 2.0, 1.0)

# Unit conversion
lambda_ = lambda_nm * 1e-9
d = d_mm * 1e-3
a = a_mm * 1e-3
D = D_m

# Calculate intensity
theta = np.linspace(-0.01, 0.01, 1000)
beta = (np.pi * a * np.sin(theta)) / lambda_
alpha = (np.pi * d * np.sin(theta)) / lambda_
intensity = (np.sin(beta) / beta) ** 2 * (np.cos(alpha)) ** 2

# Plot intensity curve
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(theta, intensity, color='b')
ax1.set_xlabel("Diffraction angle θ (radian)")
ax1.set_ylabel("Relative intensity I/I₀")
ax1.set_title("Double-slit Interference Intensity Distribution (with Single-slit Diffraction)")
ax1.grid(True)
st.pyplot(fig1)

# Simulated fringe pattern
x = D * np.tan(theta)
fig2, ax2 = plt.subplots(figsize=(8, 1.5))
ax2.imshow(intensity.reshape(1, -1), cmap='gray',
           extent=[x.min(), x.max(), 0, 1], aspect='auto')
ax2.set_xlabel("Screen position x (m)")
ax2.set_title("Interference Fringe Simulation")
st.pyplot(fig2)

