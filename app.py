import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# ========= 字体设置部分 =========
# 确认字体路径
font_path = "./fonts/msyh.ttc"    # 替换为你的字体文件路径
if not os.path.exists(font_path):
    st.warning("未检测到字体文件 msyh.ttc，请确认已上传 fonts/msyh.ttc")
prop = fm.FontProperties(fname=font_path)

# ========= Streamlit 页面设置 =========
st.set_page_config(page_title="双缝干涉模拟（含单缝衍射）", layout="centered")
st.title("双缝干涉光强模拟（含单缝衍射）")

# ========= 参数控制 =========
lambda_nm = st.slider("波长 λ (nm)", 400.0, 700.0, 633.0)
d_mm = st.slider("双缝间距 d (mm)", 0.1, 0.5, 0.2)
a_mm = st.slider("单缝宽度 a (mm)", 0.01, 0.1, 0.05)
D_m = st.slider("屏幕距离 D (m)", 0.5, 2.0, 1.0)

# 单位转换
lambda_ = lambda_nm * 1e-9
d = d_mm * 1e-3
a = a_mm * 1e-3
D = D_m

# ========= 计算光强 =========
theta = np.linspace(-0.01, 0.01, 1000)
beta = (np.pi * a * np.sin(theta)) / lambda_
alpha = (np.pi * d * np.sin(theta)) / lambda_
# 避免除以0
beta = np.where(beta == 0, 1e-10, beta)
intensity = (np.sin(beta) / beta) ** 2 * (np.cos(alpha)) ** 2

# ========= 绘制第一张图：光强随角度 =========
fig1, ax1 = plt.subplots(figsize=(8, 4))
ax1.plot(theta, intensity, color='b')
ax1.set_xlabel("衍射角 θ (弧度)", fontproperties=prop)
ax1.set_ylabel("相对光强 I/I₀", fontproperties=prop)
ax1.set_title("双缝干涉光强分布（含单缝衍射）", fontproperties=prop)
ax1.grid(True)
st.pyplot(fig1)

# ========= 绘制第二张图：条纹模拟 =========
x = D * np.tan(theta)
fig2, ax2 = plt.subplots(figsize=(8, 1.5))
ax2.imshow(intensity.reshape(1, -1), cmap='gray',
           extent=[x.min(), x.max(), 0, 1], aspect='auto')
ax2.set_xlabel("屏上位置 x (m)", fontproperties=prop)
ax2.set_title("双缝干涉条纹模拟", fontproperties=prop)
st.pyplot(fig2)

st.caption("提示：若出现方块字，请确认 fonts 文件夹下存在 msyh.ttc 字体文件。")