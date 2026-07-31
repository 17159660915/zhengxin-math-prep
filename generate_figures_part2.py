# -*- coding: utf-8 -*-
"""
正心童学·初中数学思维题库 — 高精度配图生成脚本 Part 2 (初三)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Rectangle, Circle, FancyBboxPatch, Polygon, Wedge
from matplotlib.lines import Line2D
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Microsoft YaHei', 'SimHei', 'DejaVu Sans'],
    'font.size': 11, 'axes.unicode_minus': False,
    'figure.dpi': 300, 'savefig.dpi': 300, 'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15, 'lines.antialiased': True, 'text.antialiased': True,
    'mathtext.fontset': 'dejavusans',
})

OUT = r"C:\Users\Administrator\Desktop\zhengxin-math-prep\assets\figures"

def add_title_label(ax, code):
    ax.text(0.02, 0.97, code, transform=ax.transAxes, fontsize=8,
            color='#888888', ha='left', va='top', alpha=0.8,
            bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='#cccccc', alpha=0.7))
# ══════════════════════════════════════════════════════════════
# 【初三】22-1 第2题 — 抛物线顶点
# ══════════════════════════════════════════════════════════════
def fig_22_1_2():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(-4, 2, 400)
    y = x**2 + 2*x - 3
    ax.plot(x, y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 交点
    ax.plot(1, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(1.1, -0.3, 'A(1,0)', fontsize=10, color='#c82423')
    ax.plot(-3, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(-3.4, -0.3, 'B(-3,0)', fontsize=10, color='#c82423')
    # 顶点
    ax.plot(-1, -4, 'o', color='#2196F3', markersize=8, zorder=5)
    ax.text(-1.3, -4.3, '顶点(-1,-4)', fontsize=10, color='#2196F3')
    # 对称轴
    ax.axvline(x=-1, color='green', lw=1.0, ls='--', alpha=0.6)
    ax.text(-1.2, 3, '对称轴\nx=-1', fontsize=9, color='green', ha='center')
    ax.set_xlim(-4.5, 2.5)
    ax.set_ylim(-5, 4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_aspect('equal')
    add_title_label(ax, '22-1 第2题')
    fig.savefig(os.path.join(OUT, '初三', '22-1-2.png'))
    plt.close(fig)

# ══════════════════════════════════════════════════════════════
# 【初三】22-1 第3题 — 二次函数与x轴交点距离为2
# ══════════════════════════════════════════════════════════════
def fig_22_1_3():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(-3, 2, 400)
    # y = x^2 + 2x - 3  (m=1时, 交点在-1和-3)
    # 或 m=3: y = x^2 + 4x + 3, 交点在-1和-3
    y = x**2 + 4*x + 3
    ax.plot(x, y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.plot(-1, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.plot(-3, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(-1, -0.3, '(-1,0)', fontsize=10, color='#c82423', ha='center')
    ax.text(-3, -0.3, '(-3,0)', fontsize=10, color='#c82423', ha='center')
    # 距离标注
    ax.annotate('', xy=(-3, -0.5), xytext=(-1, -0.5),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.2))
    ax.text(-2, -0.8, '距离=2', ha='center', fontsize=10, color='green')
    ax.set_xlim(-4, 2.5)
    ax.set_ylim(-2, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls=':', alpha=0.3)
    add_title_label(ax, '22-1 第3题')
    fig.savefig(os.path.join(OUT, '初三', '22-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】22-1 第4题 — 二次函数顶点最大值
# ══════════════════════════════════════════════════════════════
def fig_22_1_4():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(-1, 3, 400)
    y = -2*x**2 + 4*x + 2
    ax.plot(x, y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 顶点
    ax.plot(1, 4, 'o', color='#c82423', markersize=10, zorder=5)
    ax.text(1.2, 4.1, '最大值(1,4)', fontsize=11, color='#c82423', fontweight='bold')
    # 过(0,2)
    ax.plot(0, 2, 'o', color='#2196F3', markersize=8, zorder=5)
    ax.text(0.1, 1.7, '(0,2)', fontsize=10, color='#2196F3')
    # 对称轴
    ax.axvline(x=1, color='green', lw=1.0, ls='--', alpha=0.6)
    ax.text(1.2, 2.5, 'x=1', fontsize=9, color='green')
    ax.set_xlim(-1.5, 3.5)
    ax.set_ylim(-1, 5.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls=':', alpha=0.3)
    add_title_label(ax, '22-1 第4题')
    fig.savefig(os.path.join(OUT, '初三', '22-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】22-2 第1题 — 二次函数与x轴交点
# ══════════════════════════════════════════════════════════════
def fig_22_2_1():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(-2.5, 4.5, 400)
    y = x**2 - 2*x - 3
    ax.plot(x, y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.plot(-1, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.plot(3, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(-1.2, -0.3, '(-1,0)', fontsize=10, color='#c82423', ha='center')
    ax.text(3.2, -0.3, '(3,0)', fontsize=10, color='#c82423', ha='center')
    ax.set_xlim(-3, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_title('y = x² - 2x - 3, 2个交点', fontsize=10)
    add_title_label(ax, '22-2 第1题')
    fig.savefig(os.path.join(OUT, '初三', '22-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】22-2 第2题 — 二次函数不等式
# ══════════════════════════════════════════════════════════════
def fig_22_2_2():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(-2.5, 3.5, 400)
    y = x**2 - x - 2
    ax.plot(x, y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 填充x²-x-2>0的区域
    x1, x2 = -1, 2
    x_fill1 = np.linspace(-2.5, x1, 200)
    x_fill2 = np.linspace(x2, 3.5, 200)
    ax.fill_between(x_fill1, x_fill1**2 - x_fill1 - 2, 0, alpha=0.15, color='#c82423')
    ax.fill_between(x_fill2, x_fill2**2 - x_fill2 - 2, 0, alpha=0.15, color='#c82423')
    ax.plot(-1, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.plot(2, 0, 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(-1, -0.3, '-1', fontsize=10, color='#c82423', ha='center')
    ax.text(2, -0.3, '2', fontsize=10, color='#c82423', ha='center')
    ax.text(-1.5, 3, 'x²-x-2>0\nx<-1 或 x>2', ha='center', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_xlim(-3, 4)
    ax.set_ylim(-3.5, 5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, ls=':', alpha=0.3)
    add_title_label(ax, '22-2 第2题')
    fig.savefig(os.path.join(OUT, '初三', '22-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】22-3 第2题 — 矩形菜地
# ══════════════════════════════════════════════════════════════
def fig_22_3_2():
    fig, ax = plt.subplots(figsize=(5.5, 4))
    # 墙在左边
    ax.plot([0, 0], [0, 3.5], 'k-', lw=2.5, color='#8B4513')
    ax.fill_between([-0.2, 0], 0, 3.5, color='#D2B48C', alpha=0.5)
    ax.text(-0.4, 1.7, '墙', fontsize=12, ha='center', va='center', rotation=90)
    # 矩形菜地
    rect = Rectangle((0, 0.5), 4, 2.5, fill=False, ec='#4CAF50', lw=2.0)
    ax.add_patch(rect)
    ax.fill_between([0, 4], 0.5, 3.0, color='#4CAF50', alpha=0.1)
    # 篱笆（三边）
    ax.plot([0, 4], [0.5, 0.5], 'g-', lw=2.5)
    ax.plot([4, 4], [0.5, 3.0], 'g-', lw=2.5)
    ax.plot([0, 4], [3.0, 3.0], 'g-', lw=2.5)
    # 标注尺寸
    ax.annotate('', xy=(0, 0.3), xytext=(4, 0.3),
                arrowprops=dict(arrowstyle='<->', color='#c82423', lw=1.2))
    ax.text(2, 0.1, '长 = 20m', ha='center', fontsize=11, color='#c82423')
    ax.annotate('', xy=(4.1, 0.5), xytext=(4.1, 3.0),
                arrowprops=dict(arrowstyle='<->', color='#2196F3', lw=1.2))
    ax.text(4.4, 1.75, '宽 = 10m', fontsize=11, color='#2196F3', va='center')
    ax.text(2, 1.75, 'S = 200m²', ha='center', fontsize=13, color='#4CAF50', fontweight='bold')
    ax.set_xlim(-0.8, 5.2)
    ax.set_ylim(-0.2, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '22-3 第2题')
    fig.savefig(os.path.join(OUT, '初三', '22-3-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-1 第1题 — 旋转(等腰Rt△)
# ══════════════════════════════════════════════════════════════
def fig_23_1_1():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    # 等腰Rt△ABC, ∠C=90°
    A = np.array([0, 4])
    B = np.array([4, 0])
    C = np.array([0, 0])
    # 三角形
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    draw_right_angle_mark(ax, C, A, B)
    ax.text(A[0]+0.1, A[1]+0.1, 'A', fontsize=12)
    ax.text(B[0]+0.1, B[1]-0.1, 'B', fontsize=12)
    ax.text(C[0]-0.15, C[1]-0.15, 'C', fontsize=12)
    # 内点P
    P = np.array([0.8, 0.8])
    ax.plot(P[0], P[1], 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(P[0]+0.1, P[1]+0.1, 'P', fontsize=12, color='#c82423')
    # 连接PA, PB, PC
    ax.plot([P[0], A[0]], [P[1], A[1]], 'r--', lw=1.0, alpha=0.6)
    ax.plot([P[0], B[0]], [P[1], B[1]], 'b--', lw=1.0, alpha=0.6)
    ax.plot([P[0], C[0]], [P[1], C[1]], 'g--', lw=1.0, alpha=0.6)
    ax.text(0.5, 2.5, 'PA=2', fontsize=9, color='r', rotation=-30)
    ax.text(2.5, 0.5, 'PB=1', fontsize=9, color='b', rotation=-45)
    ax.text(0.3, 0.5, 'PC=√3', fontsize=9, color='g')
    # 旋转示意
    ax.annotate('', xy=(1.5, 0.5), xytext=(0.8, 0.8),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.2, ls=':'))
    ax.text(1.3, 0.5, '旋转90°', fontsize=8, color='purple')
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')
    add_title_label(ax, '23-1 第1题')
    fig.savefig(os.path.join(OUT, '初三', '23-1-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-1 第2题 — 等边三角形内一点到三边距离
# ══════════════════════════════════════════════════════════════
def fig_23_1_2():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    side = 4*np.sqrt(3)
    h = side * np.sqrt(3)/2
    # 等边三角形
    A = np.array([0, 0])
    B = np.array([side, 0])
    C = np.array([side/2, h])
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.5)
    ax.text(A[0], A[1]-0.3, 'A', fontsize=12, ha='center')
    ax.text(B[0], B[1]-0.3, 'B', fontsize=12, ha='center')
    ax.text(C[0], C[1]+0.2, 'C', fontsize=12, ha='center')
    # 内点P
    P = np.array([side/2, h/3])
    ax.plot(P[0], P[1], 'o', color='#c82423', markersize=8, zorder=5)
    ax.text(P[0]+0.2, P[1]+0.2, 'P', fontsize=12, color='#c82423')
    # 到三边垂线
    for y_offset, (x1, y1, x2, y2), label in [
        (1, (0, 0, side, 0), 'd₁=1'),
        (2, (side, 0, side/2, h), 'd₂=2'),
        (3, (side/2, h, 0, 0), 'd₃=3'),
    ]:
        # 垂足到P
        # 简化: 画垂线示意
        pass
    # 画三条垂线
    # 到底边
    d1_y = 1/side * (h/3 - 0) * side/2 + 0  # 垂足在底边上的位置
    ax.plot([P[0], P[0]], [P[1], 0], 'r-', lw=1.0, alpha=0.7)
    ax.text(P[0]-0.5, 0.3, 'd₁=1', fontsize=9, color='r')
    # 到右边
    ax.plot([P[0], 6.0], [P[1], 1.5], 'b-', lw=1.0, alpha=0.7)
    ax.text(6.2, 1.8, 'd₂=2', fontsize=9, color='b')
    # 到左边
    ax.plot([P[0], 0.9], [P[1], 3.0], 'g-', lw=1.0, alpha=0.7)
    ax.text(0.5, 3.2, 'd₃=3', fontsize=9, color='g')
    ax.text(side/2, h/2, 'h = 1+2+3 = 6\n边长 = 4√3', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, side+0.5)
    ax.set_ylim(-0.5, h+0.5)
    ax.axis('off')
    add_title_label(ax, '23-1 第2题')
    fig.savefig(os.path.join(OUT, '初三', '23-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-1 第4题 — 旋转60°
# ══════════════════════════════════════════════════════════════
def fig_23_1_4():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    # Rt△ABC, ∠C=90°, ∠A=30°, AB=4, BC=2, AC=2√3
    C = np.array([0, 0])
    A = np.array([2*np.sqrt(3), 0])
    B = np.array([0, 2])
    # 旋转后: 绕B旋转60°
    angle = np.radians(60)
    A_prime = np.array([B[0] + (A[0]-B[0])*np.cos(angle) - (A[1]-B[1])*np.sin(angle),
                        B[1] + (A[0]-B[0])*np.sin(angle) + (A[1]-B[1])*np.cos(angle)])
    C_prime = np.array([B[0] + (C[0]-B[0])*np.cos(angle) - (C[1]-B[1])*np.sin(angle),
                        B[1] + (C[0]-B[0])*np.sin(angle) + (C[1]-B[1])*np.cos(angle)])
    # 原三角形
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.5)
    draw_right_angle_mark(ax, C, A, B)
    ax.text(A[0]+0.1, A[1]-0.1, 'A', fontsize=12)
    ax.text(B[0]-0.15, B[1]+0.1, 'B', fontsize=12)
    ax.text(C[0]-0.15, C[1]-0.15, 'C', fontsize=12)
    # 旋转后三角形
    ax.plot([A_prime[0], B[0]], [A_prime[1], B[1]], 'r-', lw=1.5)
    ax.plot([B[0], C_prime[0]], [B[1], C_prime[1]], 'r-', lw=1.5)
    ax.plot([C_prime[0], A_prime[0]], [C_prime[1], A_prime[1]], 'r-', lw=1.5)
    ax.text(A_prime[0]+0.1, A_prime[1]+0.1, "A'", fontsize=12, color='r')
    ax.text(C_prime[0]+0.1, C_prime[1]+0.1, "C'", fontsize=12, color='r')
    # 旋转弧
    arc = Arc(B, width=0.8, height=0.8, theta1=0, theta2=60, color='purple', lw=1.2, ls='--')
    ax.add_patch(arc)
    ax.text(0.4, 2.3, '60°', fontsize=9, color='purple')
    # A'C连线
    ax.plot([A_prime[0], C[0]], [A_prime[1], C[1]], 'g--', lw=1.0, alpha=0.6)
    ax.text(2.5, 1.0, "A'C = 2√7", fontsize=10, color='green', rotation=20)
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')
    add_title_label(ax, '23-1 第4题')
    fig.savefig(os.path.join(OUT, '初三', '23-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-1 第5题 — 等腰Rt△垂直
# ══════════════════════════════════════════════════════════════
def fig_23_1_5():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    # 等腰Rt△ABC, AB=AC, ∠BAC=90°
    A = np.array([0, 0])
    B = np.array([4, 0])
    C = np.array([0, 4])
    D = np.array([2, 2])  # BC中点
    E = np.array([1.5, 0])  # AB上一点
    F = np.array([0, 1.5])  # AC上一点
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    draw_right_angle_mark(ax, A, B, C)
    ax.text(A[0]-0.15, A[1]-0.15, 'A', fontsize=12)
    ax.text(B[0]+0.1, B[1]-0.1, 'B', fontsize=12)
    ax.text(C[0]-0.1, C[1]+0.1, 'C', fontsize=12)
    ax.plot(D[0], D[1], 'o', color='#2196F3', markersize=6, zorder=5)
    ax.text(D[0]+0.1, D[1]-0.15, 'D', fontsize=11, color='#2196F3')
    ax.plot(E[0], E[1], 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(E[0]+0.1, E[1]-0.1, 'E', fontsize=11, color='#c82423')
    ax.plot(F[0], F[1], 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(F[0]-0.15, F[1]+0.1, 'F', fontsize=11, color='#c82423')
    # DE⊥DF
    ax.plot([D[0], E[0]], [D[1], E[1]], 'r--', lw=1.2)
    ax.plot([D[0], F[0]], [D[1], F[1]], 'b--', lw=1.2)
    # 直角标记
    draw_right_angle_mark(ax, D, E, F, size=0.15, color='#c82423')
    # 连接AD
    ax.plot([A[0], D[0]], [A[1], D[1]], 'g-', lw=1.0, alpha=0.5)
    ax.text(1, 1, 'AD', fontsize=8, color='green', alpha=0.6)
    ax.text(2, 2.5, 'BE = AF', ha='center', fontsize=11, color='#c82423', fontweight='bold')
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')
    add_title_label(ax, '23-1 第5题')
    fig.savefig(os.path.join(OUT, '初三', '23-1-5.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-2 第2题 — 中心对称
# ══════════════════════════════════════════════════════════════
def fig_23_2_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-6.5, 6.5)
    ax.grid(True, ls=':', alpha=0.3)
    ax.plot(2, -5, 'o', color='#c82423', markersize=10, zorder=5)
    ax.text(2.2, -5.2, 'A(2, -5)', fontsize=11, color='#c82423')
    ax.plot(-2, 5, 'o', color='#2196F3', markersize=10, zorder=5)
    ax.text(-2.5, 5.2, 'B(-2, 5)', fontsize=11, color='#2196F3')
    # 连线
    ax.plot([2, -2], [-5, 5], 'k--', lw=0.8, alpha=0.4)
    ax.text(0, -0.5, 'O(0,0)', ha='center', fontsize=10, color='#666')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '23-2 第2题')
    fig.savefig(os.path.join(OUT, '初三', '23-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】23-3 第1题 — 等边三角形旋转成六边形
# ══════════════════════════════════════════════════════════════
def fig_23_3_1():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    # 正六边形
    angles = np.linspace(0, 2*np.pi, 7)[:-1] + np.pi/6
    hex_pts = np.array([[np.cos(a), np.sin(a)] for a in angles])
    ax.plot([*hex_pts[:, 0], hex_pts[0, 0]], [*hex_pts[:, 1], hex_pts[0, 1]], 'b-', lw=1.5)
    # 中心三角形
    tri_pts = hex_pts[[0, 2, 4]]
    ax.plot([*tri_pts[:, 0], tri_pts[0, 0]], [*tri_pts[:, 1], tri_pts[0, 1]], 'r-', lw=2.0)
    ax.fill(tri_pts[:, 0], tri_pts[:, 1], alpha=0.15, color='#c82423')
    # 旋转箭头
    for i in range(3):
        j = (i+1) % 3
        mid = (tri_pts[i] + tri_pts[j]) / 2
        ax.annotate('', xy=hex_pts[2*i+1], xytext=mid,
                    arrowprops=dict(arrowstyle='->', color='green', lw=1.0, ls='--'))
    ax.text(0, 0.15, '中心旋转60°', ha='center', fontsize=10, color='green')
    ax.text(0, -0.15, '得到正六边形', ha='center', fontsize=10, color='#2196F3')
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.axis('off')
    add_title_label(ax, '23-3 第1题')
    fig.savefig(os.path.join(OUT, '初三', '23-3-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-1 第2题 — 圆内弦与直径互相平分
# ══════════════════════════════════════════════════════════════
def fig_24_1_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    circle = Circle((0, 0), 5, fill=False, color='#333', lw=1.5)
    ax.add_patch(circle)
    # 直径AB(水平)
    ax.plot([-5, 5], [0, 0], 'k-', lw=1.5)
    ax.text(-5.3, 0, 'A', fontsize=12)
    ax.text(5.3, 0, 'B', fontsize=12)
    # 弦CD(垂直)
    ax.plot([0, 0], [-4, 4], 'r-', lw=1.5)
    ax.text(-0.2, 4.2, 'C', fontsize=12, color='r')
    ax.text(-0.2, -4.2, 'D', fontsize=12, color='r')
    # 圆心O
    ax.plot(0, 0, 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(0.2, 0.2, 'O', fontsize=12, color='#c82423')
    # 垂线OE
    ax.plot([0, 0], [0, 4], 'g--', lw=1.0, alpha=0.6)
    ax.text(0.3, 2, 'OE = 3', fontsize=10, color='green')
    ax.set_aspect('equal')
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)
    ax.axis('off')
    add_title_label(ax, '24-1 第2题')
    fig.savefig(os.path.join(OUT, '初三', '24-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-1 第3题 — 圆内平行弦
# ══════════════════════════════════════════════════════════════
def fig_24_1_3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))
    for ax, label in [(ax1, '同侧: 距离=1'), (ax2, '异侧: 距离=7')]:
        circle = Circle((0, 0), 5, fill=False, color='#333', lw=1.5)
        ax.add_patch(circle)
        ax.plot(0, 0, 'o', color='#c82423', markersize=5, zorder=5)
        ax.text(0.2, 0.2, 'O', fontsize=10)
        if label == '同侧: 距离=1':
            y1, y2 = 3, -4  # 简化为不同位置
            # AB (弦长6, 距圆心4)
            x_ab = np.sqrt(25-16)
            ax.plot([-x_ab, x_ab], [4, 4], 'b-', lw=1.5)
            ax.text(-x_ab-0.3, 4, 'A', fontsize=10, color='b')
            ax.text(x_ab+0.3, 4, 'B', fontsize=10, color='b')
            # CD (弦长8, 距圆心3)
            x_cd = np.sqrt(25-9)
            ax.plot([-x_cd, x_cd], [3, 3], 'r-', lw=1.5)
            ax.text(-x_cd-0.3, 3, 'C', fontsize=10, color='r')
            ax.text(x_cd+0.3, 3, 'D', fontsize=10, color='r')
            ax.annotate('', xy=(0, 3), xytext=(0, 4),
                        arrowprops=dict(arrowstyle='<->', color='green', lw=1.0))
            ax.text(0.5, 3.5, '1', fontsize=9, color='green')
        else:
            ax.plot([-4, 4], [3, 3], 'b-', lw=1.5)
            ax.text(-4.3, 3, 'A', fontsize=10, color='b')
            ax.text(4.3, 3, 'B', fontsize=10, color='b')
            ax.plot([-3, 3], [-4, -4], 'r-', lw=1.5)
            ax.text(-3.3, -4, 'C', fontsize=10, color='r')
            ax.text(3.3, -4, 'D', fontsize=10, color='r')
            ax.annotate('', xy=(0, -4), xytext=(0, 3),
                        arrowprops=dict(arrowstyle='<->', color='green', lw=1.0))
            ax.text(0.5, -0.5, '7', fontsize=9, color='green')
        ax.set_title(label, fontsize=10)
        ax.set_aspect('equal')
        ax.set_xlim(-5.8, 5.8)
        ax.set_ylim(-5.8, 5.8)
        ax.axis('off')
    add_title_label(ax1, '24-1 第3题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初三', '24-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-1 第4题 — 三角形外接圆
# ══════════════════════════════════════════════════════════════
def fig_24_1_4():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    # 等腰三角形ABC, AB=AC=5, BC=6
    A = np.array([0, 4])
    B = np.array([-3, 0])
    C = np.array([3, 0])
    # 外接圆
    R = 25/8
    circle = Circle((0, 25/8 - 4), R, fill=False, color='#2196F3', lw=1.5)
    ax.add_patch(circle)
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.5)
    ax.text(A[0], A[1]+0.2, 'A', fontsize=12, ha='center')
    ax.text(B[0]-0.2, B[1]-0.2, 'B', fontsize=12)
    ax.text(C[0]+0.2, C[1]-0.2, 'C', fontsize=12)
    # 外心O
    O = np.array([0, 25/8 - 4])
    ax.plot(O[0], O[1], 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(O[0]+0.2, O[1]+0.2, 'O', fontsize=11, color='#c82423')
    # 半径
    ax.plot([O[0], A[0]], [O[1], A[1]], 'r--', lw=0.8, alpha=0.5)
    ax.text(0.3, 0.5, 'R = 25/8', fontsize=10, color='#c82423')
    ax.set_aspect('equal')
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-2, 5)
    ax.axis('off')
    add_title_label(ax, '24-1 第4题')
    fig.savefig(os.path.join(OUT, '初三', '24-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-2 第1题 — 点与圆位置
# ══════════════════════════════════════════════════════════════
def fig_24_2_1():
    fig, ax = plt.subplots(figsize=(5, 5))
    circle = Circle((0, 0), 5, fill=False, color='#333', lw=1.5)
    ax.add_patch(circle)
    ax.plot(0, 0, 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(0.2, 0.2, 'O', fontsize=12, color='#c82423')
    # 点P在圆内
    P = np.array([3, 0])
    ax.plot(P[0], P[1], 'o', color='#2196F3', markersize=8, zorder=5)
    ax.text(P[0]+0.2, P[1]+0.2, 'P', fontsize=12, color='#2196F3')
    ax.plot([0, 3], [0, 0], 'r--', lw=1.0)
    ax.text(1.5, -0.5, 'd=3<r=5', ha='center', fontsize=10, color='#c82423')
    ax.text(0, -3, '点P在圆内', ha='center', fontsize=11, color='#2196F3')
    ax.set_aspect('equal')
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)
    ax.axis('off')
    add_title_label(ax, '24-2 第1题')
    fig.savefig(os.path.join(OUT, '初三', '24-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-2 第2题 — 直线与圆位置
# ══════════════════════════════════════════════════════════════
def fig_24_2_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    circle = Circle((0, 0), 4, fill=False, color='#333', lw=1.5)
    ax.add_patch(circle)
    ax.plot(0, 0, 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(0.2, 0.2, 'O', fontsize=12, color='#c82423')
    # 直线l: y = -3 (距离=3)
    ax.plot([-5, 5], [-3, -3], 'r-', lw=2.0)
    ax.text(-5.3, -3, 'l', fontsize=12, color='r')
    # 距离
    ax.plot([0, 0], [0, -3], 'g--', lw=1.0)
    ax.text(0.3, -1.5, 'd=3<r=4', fontsize=10, color='green')
    ax.text(0, -4.5, '直线与圆相交（2个交点）', ha='center', fontsize=10, color='#c82423')
    ax.set_aspect('equal')
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-5.8, 5.8)
    ax.axis('off')
    add_title_label(ax, '24-2 第2题')
    fig.savefig(os.path.join(OUT, '初三', '24-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-3 第1题 — 正六边形
# ══════════════════════════════════════════════════════════════
def fig_24_3_1():
    fig, ax = plt.subplots(figsize=(5, 5))
    angles = np.linspace(0, 2*np.pi, 7)[:-1] + np.pi/2
    pts = np.array([[np.cos(a), np.sin(a)] for a in angles])
    ax.plot([*pts[:, 0], pts[0, 0]], [*pts[:, 1], pts[0, 1]], 'b-', lw=1.5)
    ax.fill(pts[:, 0], pts[:, 1], alpha=0.1, color='#2196F3')
    # 中心
    ax.plot(0, 0, 'o', color='#c82423', markersize=5, zorder=5)
    ax.text(0.1, 0.1, 'O', fontsize=11, color='#c82423')
    # 中心角
    annotate_angle_deg(ax, (0, 0), pts[0], pts[1], 60, radius=0.3, color='#c82423')
    ax.text(0, -1.4, '中心角 = 360°/6 = 60°', ha='center', fontsize=10, color='#c82423')
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.6, 1.3)
    ax.axis('off')
    add_title_label(ax, '24-3 第1题')
    fig.savefig(os.path.join(OUT, '初三', '24-3-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-3 第2题 — 正五边形
# ══════════════════════════════════════════════════════════════
def fig_24_3_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    angles = np.linspace(0, 2*np.pi, 6)[:-1] - np.pi/2
    pts = np.array([[np.cos(a), np.sin(a)] for a in angles])
    ax.plot([*pts[:, 0], pts[0, 0]], [*pts[:, 1], pts[0, 1]], 'b-', lw=1.5)
    ax.fill(pts[:, 0], pts[:, 1], alpha=0.1, color='#FF9800')
    # 内角标注
    ax.text(0, -0.15, '每个内角 = 108°', ha='center', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.text(0, -1.1, '内角和 = (5-2)×180° = 540°', ha='center', fontsize=10, color='#666')
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.4, 1.3)
    ax.axis('off')
    add_title_label(ax, '24-3 第2题')
    fig.savefig(os.path.join(OUT, '初三', '24-3-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-4 第1题 — 扇形
# ══════════════════════════════════════════════════════════════
def fig_24_4_1():
    fig, ax = plt.subplots(figsize=(5, 5))
    wedge = Wedge((0, 0), 6, 0, 120, fill=True, color='#FF9800', alpha=0.2, ec='#c82423', lw=1.5)
    ax.add_patch(wedge)
    ax.plot([0, 6], [0, 0], 'k-', lw=1.5)
    ax.plot([0, 6*np.cos(np.radians(120))], [0, 6*np.sin(np.radians(120))], 'k-', lw=1.5)
    ax.plot(0, 0, 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(0.2, -0.2, 'O', fontsize=12)
    # 弧长标注
    arc = Arc((0, 0), 5, 5, theta1=0, theta2=120, color='#2196F3', lw=1.5, ls='--')
    ax.add_patch(arc)
    ax.text(0, 4.5, '弧长 = 4π', ha='center', fontsize=11, color='#2196F3')
    # 角度标注
    annotate_angle_deg(ax, (0, 0), (6, 0), (6*np.cos(np.radians(120)), 6*np.sin(np.radians(120))),
                       120, radius=1.0, color='#c82423')
    ax.text(3.5, 0.5, 'r=6', fontsize=10)
    ax.text(0, -1.5, '扇形面积 = 12π', ha='center', fontsize=11, color='#c82423', fontweight='bold')
    ax.set_aspect('equal')
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1.8, 7)
    ax.axis('off')
    add_title_label(ax, '24-4 第1题')
    fig.savefig(os.path.join(OUT, '初三', '24-4-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】24-4 第2题 — 圆锥
# ══════════════════════════════════════════════════════════════
def fig_24_4_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    # 圆锥侧面
    r, l = 3, 5
    h = np.sqrt(l**2 - r**2)
    theta = np.linspace(0, 2*np.pi, 100)
    base_x = r * np.cos(theta)
    base_y = r * np.sin(theta) - 0.5
    ax.fill(base_x, base_y, alpha=0.1, color='#2196F3')
    ax.plot(base_x, base_y, 'b-', lw=1.5)
    # 顶点到底面
    ax.plot([0, r], [h, -0.5], 'b-', lw=1.5)
    ax.plot([0, -r], [h, -0.5], 'b-', lw=1.5)
    ax.plot(0, h, 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(0.1, h+0.1, 'S', fontsize=12, color='#c82423')
    # 标注半径和母线
    ax.annotate('', xy=(0, -0.5), xytext=(r, -0.5),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.0))
    ax.text(r/2, -1.0, 'r=3', ha='center', fontsize=10, color='green')
    # 母线
    ax.text(r/2+0.3, h/2, 'l=5', fontsize=10, color='#c82423', rotation=-30)
    # 高
    ax.plot([0, 0], [-0.5, h], 'k--', lw=0.8, alpha=0.4)
    ax.text(0.3, h/2, 'h=4', fontsize=10, color='#666')
    ax.text(0, -2.5, '侧面积=15π, 全面积=24π', ha='center', fontsize=11, color='#c82423', fontweight='bold')
    ax.set_aspect('equal')
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-2.8, h+0.5)
    ax.axis('off')
    add_title_label(ax, '24-4 第2题')
    fig.savefig(os.path.join(OUT, '初三', '24-4-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】25-1 第2题 — 组合概率
# ══════════════════════════════════════════════════════════════
def fig_25_1_2():
    fig, ax = plt.subplots(figsize=(5.5, 3))
    numbers = [1, 2, 3, 4, 5]
    data = [
        (0, 0, [1, 2, 3], '❌'),
        (1, 0, [1, 2, 4], '❌'),
        (2, 0, [1, 2, 5], '❌'),
        (3, 0, [1, 3, 4], '❌'),
        (4, 0, [1, 3, 5], '❌'),
        (0, 1, [1, 4, 5], '❌'),
        (1, 1, [2, 3, 4], '✅'),
        (2, 1, [2, 3, 5], '❌'),
        (3, 1, [2, 4, 5], '✅'),
        (4, 1, [3, 4, 5], '✅'),
    ]
    for x, y, nums, mark in data:
        ax.text(x, y, f'({",".join(map(str, nums))}) {mark}', fontsize=9, ha='center', va='center')
    ax.text(2, -0.5, 'P = 3/10', ha='center', fontsize=13, color='#c82423', fontweight='bold')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-1, 1.5)
    ax.axis('off')
    add_title_label(ax, '25-1 第2题')
    fig.savefig(os.path.join(OUT, '初三', '25-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】26-1 第2题 — 反比例函数象限
# ══════════════════════════════════════════════════════════════
def fig_26_1_2():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(0.5, 5, 200)
    y = 2/x  # k>0示例
    ax.plot(x, y, 'b-', lw=2.0, label='k>0')
    ax.plot(-x, -y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 象限标注
    ax.text(2, 2, '第一象限', fontsize=10, color='green', ha='center')
    ax.text(-3, -2, '第三象限', fontsize=10, color='green', ha='center')
    ax.text(2, -2, 'k>0 在一、三象限', ha='center', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_aspect('equal')
    add_title_label(ax, '26-1 第2题')
    fig.savefig(os.path.join(OUT, '初三', '26-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】26-1 第3题 — 反比例函数比较大小
# ══════════════════════════════════════════════════════════════
def fig_26_1_3():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(0.5, 5, 200)
    y = 6/x
    ax.plot(x, y, 'b-', lw=2.0, label='k=6>0')
    ax.plot(-x, -y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 点A和B在第三象限
    A = np.array([-1, -6])
    B = np.array([-3, -2])
    ax.plot(A[0], A[1], 'o', color='#c82423', markersize=8, zorder=5)
    ax.plot(B[0], B[1], 'o', color='#2196F3', markersize=8, zorder=5)
    ax.text(A[0]-0.5, A[1]-0.3, 'A(x₁,y₁)', fontsize=10, color='#c82423')
    ax.text(B[0]-0.5, B[1]-0.3, 'B(x₂,y₂)', fontsize=10, color='#2196F3')
    ax.text(-2, -4, 'x₁ < x₂ < 0\ny₁ > y₂', ha='center', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-7.5, 5.5)
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_aspect('equal')
    add_title_label(ax, '26-1 第3题')
    fig.savefig(os.path.join(OUT, '初三', '26-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】26-1 第4题 — 反比例与一次函数交点
# ══════════════════════════════════════════════════════════════
def fig_26_1_4():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(0.3, 3, 200)
    y = 3/x
    ax.plot(x, y, 'b-', lw=2.0, label='y=3/x')
    ax.plot(-x, -y, 'b-', lw=2.0)
    # 一次函数 y=2x+1
    x_line = np.linspace(-2, 2, 200)
    y_line = 2*x_line + 1
    ax.plot(x_line, y_line, 'r-', lw=2.0, label='y=2x+1')
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 交点
    ax.plot(1, 3, 'o', color='green', markersize=8, zorder=5)
    ax.text(1.1, 3.1, 'A(1,3)', fontsize=10, color='green')
    ax.plot(-1.5, -2, 'o', color='green', markersize=8, zorder=5)
    ax.text(-1.8, -2.2, 'B(-1.5,-2)', fontsize=10, color='green')
    ax.set_xlim(-3, 3.5)
    ax.set_ylim(-5, 5)
    ax.grid(True, ls=':', alpha=0.3)
    ax.legend(fontsize=9)
    add_title_label(ax, '26-1 第4题')
    fig.savefig(os.path.join(OUT, '初三', '26-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】26-1 第5题 — 反比例函数
# ══════════════════════════════════════════════════════════════
def fig_26_1_5():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    x = np.linspace(0.5, 5, 200)
    y = 2/x
    ax.plot(x, y, 'b-', lw=2.0, label='y=2/x')
    ax.plot(-x, -y, 'b-', lw=2.0)
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    # 两点P和Q在图象上
    P = np.array([1, 2])
    Q = np.array([2, 1])
    ax.plot(P[0], P[1], 'o', color='#c82423', markersize=8, zorder=5)
    ax.plot(Q[0], Q[1], 'o', color='#2196F3', markersize=8, zorder=5)
    ax.text(P[0]+0.2, P[1]+0.1, 'P(x₁,y₁)', fontsize=10, color='#c82423')
    ax.text(Q[0]+0.2, Q[1]+0.1, 'Q(x₂,y₂)', fontsize=10, color='#2196F3')
    ax.set_xlim(-5.5, 5.5)
    ax.set_ylim(-5.5, 5.5)
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_aspect('equal')
    add_title_label(ax, '26-1 第5题')
    fig.savefig(os.path.join(OUT, '初三', '26-1-5.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】26-2 第2题 — 反比例函数实际应用
# ══════════════════════════════════════════════════════════════
def fig_26_2_2():
    fig, ax = plt.subplots(figsize=(5.5, 4))
    t = np.linspace(1, 20, 200)
    v = 1000/t
    ax.plot(t, v, 'b-', lw=2.0)
    ax.set_xlabel('t (h)')
    ax.set_ylabel('v (m³/h)')
    ax.grid(True, ls=':', alpha=0.3)
    ax.set_title('v = 1000/t (t > 0)', fontsize=12)
    ax.text(10, 150, '水量一定\n速度与时间成反比', ha='center', fontsize=11,
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    add_title_label(ax, '26-2 第2题')
    fig.savefig(os.path.join(OUT, '初三', '26-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】27-2 第1题 — 相似三角形(DE∥BC)
# ══════════════════════════════════════════════════════════════
def fig_27_2_1():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    A = np.array([2, 4])
    B = np.array([0, 0])
    C = np.array([5, 0])
    D = np.array([0.8, 1.6])  # AD=2, AB=5, 比例2/5
    E = np.array([3.2, 1.6])  # AE/AC=2/5
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([D[0], E[0]], [D[1], E[1]], 'r-', lw=2.0)
    ax.text(A[0], A[1]+0.2, 'A', fontsize=12, ha='center')
    ax.text(B[0]-0.2, B[1]-0.2, 'B', fontsize=12)
    ax.text(C[0]+0.2, C[1]-0.2, 'C', fontsize=12)
    ax.text(D[0]-0.2, D[1]-0.2, 'D', fontsize=12, color='r')
    ax.text(E[0]+0.2, E[1]-0.2, 'E', fontsize=12, color='r')
    # 平行标记
    ax.plot([0.6, 0.7], [1.6, 1.7], 'r-', lw=1.0)
    ax.plot([0.7, 0.8], [1.6, 1.7], 'r-', lw=1.0)
    ax.text(2, 2, 'DE∥BC', fontsize=11, color='r')
    ax.text(2, 0.5, 'AD/AB = DE/BC', ha='center', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 4.5)
    ax.axis('off')
    add_title_label(ax, '27-2 第1题')
    fig.savefig(os.path.join(OUT, '初三', '27-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】27-2 第2题 — 相似三角形
# ══════════════════════════════════════════════════════════════
def fig_27_2_2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    # △ABC
    A1 = np.array([1.5, 3])
    B1 = np.array([0, 0])
    C1 = np.array([3, 0])
    ax1.plot([A1[0], B1[0]], [A1[1], B1[1]], 'b-', lw=1.5)
    ax1.plot([A1[0], C1[0]], [A1[1], C1[1]], 'b-', lw=1.5)
    ax1.plot([B1[0], C1[0]], [B1[1], C1[1]], 'b-', lw=1.5)
    ax1.text(A1[0], A1[1]+0.2, 'A', fontsize=12, ha='center')
    ax1.text(B1[0]-0.2, B1[1]-0.2, 'B', fontsize=12)
    ax1.text(C1[0]+0.2, C1[1]-0.2, 'C', fontsize=12)
    ax1.set_title('△ABC (AB=6)', fontsize=11)
    ax1.set_aspect('equal')
    ax1.set_xlim(-0.5, 3.5)
    ax1.set_ylim(-0.5, 3.5)
    ax1.axis('off')
    # △DEF (相似比3:2, 所以DE=4)
    A2 = np.array([1.0, 2])
    B2 = np.array([0, 0])
    C2 = np.array([2, 0])
    ax2.plot([A2[0], B2[0]], [A2[1], B2[1]], 'r-', lw=1.5)
    ax2.plot([A2[0], C2[0]], [A2[1], C2[1]], 'r-', lw=1.5)
    ax2.plot([B2[0], C2[0]], [B2[1], C2[1]], 'r-', lw=1.5)
    ax2.text(A2[0], A2[1]+0.2, 'D', fontsize=12, ha='center')
    ax2.text(B2[0]-0.2, B2[1]-0.2, 'E', fontsize=12)
    ax2.text(C2[0]+0.2, C2[1]-0.2, 'F', fontsize=12)
    ax2.set_title('△DEF (DE=4)', fontsize=11)
    ax2.set_aspect('equal')
    ax2.set_xlim(-0.5, 2.5)
    ax2.set_ylim(-0.5, 2.5)
    ax2.axis('off')
    fig.suptitle('相似比 3:2', fontsize=12, y=1.02)
    add_title_label(ax1, '27-2 第2题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初三', '27-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】28-2 第1题 — Rt三角形30度
# ══════════════════════════════════════════════════════════════
def fig_28_2_1():
    fig, ax = plt.subplots(figsize=(5, 4.5))
    C = np.array([0, 0])
    A = np.array([5*np.sqrt(3), 0])
    B = np.array([0, 5])
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.5)
    draw_right_angle_mark(ax, C, A, B)
    ax.text(A[0]+0.1, A[1]-0.1, 'A', fontsize=12)
    ax.text(B[0]-0.15, B[1]+0.1, 'B', fontsize=12)
    ax.text(C[0]-0.15, C[1]-0.15, 'C', fontsize=12)
    # 角度标注
    annotate_angle_deg(ax, A, C, B, 30, radius=0.6, color='#c82423')
    ax.text(2.5, 0.3, '∠A=30°', fontsize=10, color='#c82423')
    ax.text(2, 2.5, 'c=10', fontsize=11, rotation=-30)
    ax.text(1, -0.3, 'b=5√3', fontsize=10, color='#2196F3')
    ax.text(-0.5, 2.5, 'a=5', fontsize=10, color='#4CAF50', rotation=90)
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, 9.5)
    ax.set_ylim(-0.5, 5.5)
    ax.axis('off')
    add_title_label(ax, '28-2 第1题')
    fig.savefig(os.path.join(OUT, '初三', '28-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】28-2 第2题 — 俯角
# ══════════════════════════════════════════════════════════════
def fig_28_2_2():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    # 建筑物
    ax.plot([0, 0], [0, 3], 'k-', lw=2.5)
    ax.plot([-0.3, 0.3], [3, 3], 'k-', lw=2.0)
    ax.plot([-0.3, 0.3], [0, 0], 'k-', lw=2.0)
    ax.fill_between([-0.3, 0.3], 0, 3, color='#999', alpha=0.3)
    ax.text(0.5, 1.5, '30m', fontsize=11, color='#333')
    # 地面
    ax.plot([-0.3, 5], [0, 0], 'k-', lw=1.5)
    # 楼顶-地面点连线
    ax.plot([0, 3], [3, 0], 'r--', lw=1.5)
    ax.text(3, 0, '●', fontsize=10, color='#c82423', zorder=5)
    ax.text(3.2, -0.2, '地面点', fontsize=10, color='#c82423')
    # 水平线
    ax.plot([0, 3], [3, 3], 'k--', lw=0.8, alpha=0.4)
    # 俯角
    annotate_angle_deg(ax, (0, 3), (3, 3), (3, 0), 45, radius=0.6, color='#c82423')
    ax.text(1.5, 2.5, '俯角45°', fontsize=10, color='#c82423')
    # 距离
    ax.annotate('', xy=(0, -0.3), xytext=(3, -0.3),
                arrowprops=dict(arrowstyle='<->', color='#2196F3', lw=1.2))
    ax.text(1.5, -0.6, 'x = 30m', ha='center', fontsize=11, color='#2196F3', fontweight='bold')
    ax.set_aspect('equal')
    ax.set_xlim(-0.8, 5.5)
    ax.set_ylim(-1, 3.8)
    ax.axis('off')
    add_title_label(ax, '28-2 第2题')
    fig.savefig(os.path.join(OUT, '初三', '28-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】29-1 第1题 — 投影
# ══════════════════════════════════════════════════════════════
def fig_29_1_1():
    fig, ax = plt.subplots(figsize=(5.5, 4))
    # 竹竿
    ax.plot([0.5, 0.5], [0, 1.6], 'b-', lw=3.0)
    ax.text(0.5, 1.8, '1.6m', ha='center', fontsize=10, color='b')
    # 竹竿影子
    ax.plot([0.5, 1.3], [0, 0], 'b--', lw=1.5)
    ax.annotate('', xy=(0.5, -0.2), xytext=(1.3, -0.2),
                arrowprops=dict(arrowstyle='<->', color='b', lw=1.0))
    ax.text(0.9, -0.4, '0.8m', ha='center', fontsize=10, color='b')
    # 树
    ax.plot([3, 3], [0, 6.4], 'g-', lw=3.0)
    ax.text(3, 6.6, '树高?', ha='center', fontsize=10, color='g')
    # 树的影子
    ax.plot([3, 6.2], [0, 0], 'g--', lw=1.5)
    ax.annotate('', xy=(3, -0.2), xytext=(6.2, -0.2),
                arrowprops=dict(arrowstyle='<->', color='g', lw=1.0))
    ax.text(4.6, -0.4, '3.2m', ha='center', fontsize=10, color='g')
    # 光线
    ax.plot([0.5, 1.3], [1.6, 0], color='orange', lw=1.0, ls=':', alpha=0.6)
    ax.plot([3, 6.2], [6.4, 0], color='orange', lw=1.0, ls=':', alpha=0.6)
    ax.text(1.5, 5, '平行光线', fontsize=10, color='orange', rotation=-30)
    # 比例关系
    ax.text(3.5, 3.5, 'h/3.2 = 1.6/0.8', fontsize=11, color='#c82423',
            bbox=dict(boxstyle='round', fc='white', ec='#c82423', alpha=0.8))
    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-0.6, 7.2)
    ax.axis('off')
    add_title_label(ax, '29-1 第1题')
    fig.savefig(os.path.join(OUT, '初三', '29-1-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】29-1 第2题 — 圆锥三视图
# ══════════════════════════════════════════════════════════════
def fig_29_1_2():
    fig, axes = plt.subplots(1, 3, figsize=(8, 3.5))
    titles = ['主视图', '左视图', '俯视图']
    shapes = [
        ([(0, 0), (2, 0), (1, 2)], '三角形'),
        ([(0, 0), (2, 0), (1, 2)], '三角形'),
        ([], '圆+圆心'),
    ]
    for ax, title, (pts, desc) in zip(axes, titles, shapes):
        if title == '俯视图':
            circle = Circle((1, 1), 0.8, fill=False, color='#333', lw=1.5)
            ax.add_patch(circle)
            ax.plot(1, 1, 'o', color='#333', markersize=3, zorder=5)
        else:
            tri = Polygon(pts, fill=False, color='#333', lw=1.5)
            ax.add_patch(tri)
        ax.set_title(f'{title}: {desc}', fontsize=10)
        ax.set_aspect('equal')
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(-0.5, 2.5)
        ax.axis('off')
    fig.suptitle('圆锥的三视图', fontsize=12, y=1.05)
    add_title_label(axes[0], '29-1 第2题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初三', '29-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】29-1 第3题 — 小正方体组合
# ══════════════════════════════════════════════════════════════
def fig_29_1_3():
    fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
    # 主视图
    ax1 = axes[0]
    grid = [[2, 1, 2]]
    for i, h in enumerate(grid[0]):
        ax1.add_patch(Rectangle((i, 0), 0.8, h, fill=False, ec='#333', lw=1.5))
        ax1.text(i+0.4, h/2, str(h), ha='center', va='center', fontsize=11)
    ax1.set_title('主视图: 2, 1, 2', fontsize=10)
    ax1.set_xlim(-0.3, 2.5)
    ax1.set_ylim(-0.3, 2.5)
    ax1.axis('off')
    ax1.set_aspect('equal')
    # 左视图
    ax2 = axes[1]
    grid2 = [[2], [1]]
    for i, h in enumerate([g[0] for g in grid2]):
        ax2.add_patch(Rectangle((0, i), 0.8, h, fill=False, ec='#333', lw=1.5))
        ax2.text(0.4, i+h/2, str(h), ha='center', va='center', fontsize=11)
    ax2.set_title('左视图: 2, 1', fontsize=10)
    ax2.set_xlim(-0.3, 1.5)
    ax2.set_ylim(-0.3, 2.5)
    ax2.axis('off')
    ax2.set_aspect('equal')
    fig.suptitle('最少需要 5 个小正方体', fontsize=12, y=1.05)
    add_title_label(axes[0], '29-1 第3题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初三', '29-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初三】29-1 第4题 — 球体三视图
# ══════════════════════════════════════════════════════════════
def fig_29_1_4():
    fig, axes = plt.subplots(1, 3, figsize=(8, 3.5))
    for ax in axes:
        circle = Circle((0.5, 0.5), 0.4, fill=False, color='#333', lw=1.5)
        ax.add_patch(circle)
        ax.set_aspect('equal')
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(-0.1, 1.1)
        ax.axis('off')
    axes[0].set_title('主视图: 圆', fontsize=10)
    axes[1].set_title('左视图: 圆', fontsize=10)
    axes[2].set_title('俯视图: 圆', fontsize=10)
    fig.suptitle('球体: 三视图都是圆', fontsize=12, y=1.05)
    add_title_label(axes[0], '29-1 第4题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初三', '29-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 辅助函数
# ══════════════════════════════════════════════════════════════
def draw_right_angle_mark(ax, vertex, p1, p2, size=0.12, color='#333333'):
    v1 = np.array(p1) - np.array(vertex)
    v2 = np.array(p2) - np.array(vertex)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = v2 / np.linalg.norm(v2) * size
    pts = [np.array(vertex) + v1, np.array(vertex) + v1 + v2, np.array(vertex) + v2]
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=0.9)

def annotate_angle_deg(ax, center, p1, p2, deg, radius=0.4, color='#333333'):
    v1 = np.array(p1) - np.array(center)
    v2 = np.array(p2) - np.array(center)
    a1 = np.degrees(np.arctan2(v1[1], v1[0]))
    a2 = np.degrees(np.arctan2(v2[1], v2[0]))
    arc = Arc(center, width=2*radius, height=2*radius, theta1=a1, theta2=a2, color=color, lw=1.0)
    import matplotlib.pyplot as plt
    ax.add_patch(arc)
    mid = (a1 + a2) / 2
    mr = radius * 1.3
    lx = center[0] + mr * np.cos(np.radians(mid))
    ly = center[1] + mr * np.sin(np.radians(mid))
    ax.text(lx, ly, f'${deg}^\\circ$', fontsize=9, color=color, ha='center', va='center')


# ══════════════════════════════════════════════════════════════
# 主函数（初三）
# ══════════════════════════════════════════════════════════════
def generate_all_chusan():
    print("生成初三配图...")
    fig_22_1_2(); print("  ✓ 22-1-2")
    fig_22_1_3(); print("  ✓ 22-1-3")
    fig_22_1_4(); print("  ✓ 22-1-4")
    fig_22_2_1(); print("  ✓ 22-2-1")
    fig_22_2_2(); print("  ✓ 22-2-2")
    fig_22_3_2(); print("  ✓ 22-3-2")
    fig_23_1_1(); print("  ✓ 23-1-1")
    fig_23_1_2(); print("  ✓ 23-1-2")
    fig_23_1_4(); print("  ✓ 23-1-4")
    fig_23_1_5(); print("  ✓ 23-1-5")
    fig_23_2_2(); print("  ✓ 23-2-2")
    fig_23_3_1(); print("  ✓ 23-3-1")
    fig_24_1_2(); print("  ✓ 24-1-2")
    fig_24_1_3(); print("  ✓ 24-1-3")
    fig_24_1_4(); print("  ✓ 24-1-4")
    fig_24_2_1(); print("  ✓ 24-2-1")
    fig_24_2_2(); print("  ✓ 24-2-2")
    fig_24_3_1(); print("  ✓ 24-3-1")
    fig_24_3_2(); print("  ✓ 24-3-2")
    fig_24_4_1(); print("  ✓ 24-4-1")
    fig_24_4_2(); print("  ✓ 24-4-2")
    fig_25_1_2(); print("  ✓ 25-1-2")
    fig_26_1_2(); print("  ✓ 26-1-2")
    fig_26_1_3(); print("  ✓ 26-1-3")
    fig_26_1_4(); print("  ✓ 26-1-4")
    fig_26_1_5(); print("  ✓ 26-1-5")
    fig_26_2_2(); print("  ✓ 26-2-2")
    fig_27_2_1(); print("  ✓ 27-2-1")
    fig_27_2_2(); print("  ✓ 27-2-2")
    fig_28_2_1(); print("  ✓ 28-2-1")
    fig_28_2_2(); print("  ✓ 28-2-2")
    fig_29_1_1(); print("  ✓ 29-1-1")
    fig_29_1_2(); print("  ✓ 29-1-2")
    fig_29_1_3(); print("  ✓ 29-1-3")
    fig_29_1_4(); print("  ✓ 29-1-4")
    print("初三配图完成!")
# 主入口
if __name__ == '__main__':
    generate_all_chusan()
