# -*- coding: utf-8 -*-
"""
正心童学·初中数学思维题库 — 高精度配图生成脚本
为所有标注"需配图"的题目生成精确示意图
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyBboxPatch, Rectangle, Wedge, Circle
from matplotlib.lines import Line2D
import os
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ── 全局渲染配置 ──
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Microsoft YaHei', 'SimHei', 'DejaVu Sans'],
    'font.size': 11,
    'axes.unicode_minus': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
    'lines.antialiased': True,
    'text.antialiased': True,
    'lines.linewidth': 1.5,
    'mathtext.fontset': 'dejavusans',
})

OUT = r"C:\Users\Administrator\Desktop\zhengxin-math-prep\assets\figures"

def label_box(ax, text, pos, fontsize=9, color='#333333', ha='center', va='center'):
    """在坐标pos处添加带样式的标签"""
    ax.text(pos[0], pos[1], text, fontsize=fontsize, color=color, ha=ha, va=va,
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec='none', alpha=0.8))

def draw_right_angle_mark(ax, vertex, p1, p2, size=0.12, color='#333333'):
    """在vertex处画直角标记，p1和p2是两条边的方向点"""
    v1 = np.array(p1) - np.array(vertex)
    v2 = np.array(p2) - np.array(vertex)
    v1 = v1 / np.linalg.norm(v1) * size
    v2 = v2 / np.linalg.norm(v2) * size
    pts = [np.array(vertex) + v1, np.array(vertex) + v1 + v2, np.array(vertex) + v2]
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=0.9)

def annotate_angle(ax, center, p1, p2, label, radius=0.4, color='#333333'):
    """标注角度弧线和标签"""
    v1 = np.array(p1) - np.array(center)
    v2 = np.array(p2) - np.array(center)
    a1 = np.degrees(np.arctan2(v1[1], v1[0]))
    a2 = np.degrees(np.arctan2(v2[1], v2[0]))
    arc = Arc(center, width=2*radius, height=2*radius, theta1=a1, theta2=a2, color=color, lw=1.0)
    ax.add_patch(arc)
    mid = (a1 + a2) / 2
    mr = radius * 1.3
    lx = center[0] + mr * np.cos(np.radians(mid))
    ly = center[1] + mr * np.sin(np.radians(mid))
    ax.text(lx, ly, label, fontsize=10, color=color, ha='center', va='center')

def annotate_angle_deg(ax, center, p1, p2, deg, radius=0.4, color='#333333'):
    """标注角度（已知角度值）"""
    v1 = np.array(p1) - np.array(center)
    v2 = np.array(p2) - np.array(center)
    a1 = np.degrees(np.arctan2(v1[1], v1[0]))
    a2 = np.degrees(np.arctan2(v2[1], v2[0]))
    arc = Arc(center, width=2*radius, height=2*radius, theta1=a1, theta2=a2, color=color, lw=1.0)
    ax.add_patch(arc)
    mid = (a1 + a2) / 2
    mr = radius * 1.3
    lx = center[0] + mr * np.cos(np.radians(mid))
    ly = center[1] + mr * np.sin(np.radians(mid))
    ax.text(lx, ly, f'${deg}^\\circ$', fontsize=9, color=color, ha='center', va='center')

def add_title_label(ax, code):
    """在图上添加题目编号标签"""
    ax.text(0.02, 0.97, code, transform=ax.transAxes, fontsize=8,
            color='#888888', ha='left', va='top', alpha=0.8,
            bbox=dict(boxstyle='round,pad=0.1', fc='white', ec='#cccccc', alpha=0.7))


# ══════════════════════════════════════════════════════════════
# 【初一】11-2 第1题 — 数轴表示不等式解集
# ══════════════════════════════════════════════════════════════
def fig_11_2_1():
    fig, ax = plt.subplots(figsize=(7, 1.8))
    # 数轴
    ax.plot([-5.5, 2.5], [0, 0], 'k-', lw=1.5)
    # 箭头
    ax.annotate('', xy=(-5.5, 0), xytext=(-5.8, 0),
                arrowprops=dict(arrowstyle='->', color='k', lw=1.5))
    ax.annotate('', xy=(2.5, 0), xytext=(2.8, 0),
                arrowprops=dict(arrowstyle='->', color='k', lw=1.5))
    # 刻度
    for x in range(-5, 3):
        ax.plot([x, x], [-0.08, 0.08], 'k-', lw=1.0)
        ax.text(x, -0.25, str(x), ha='center', va='top', fontsize=9)
    # 实心圆点 at -4
    ax.plot(-4, 0, 'o', color='#c82423', markersize=8, zorder=5)
    # 向右射线（红色粗线）
    ax.plot([-4, 2.5], [0, 0], color='#c82423', lw=3.5, zorder=3)
    # 标注
    ax.text(-4, 0.3, 'x ≥ -4', ha='center', fontsize=10, color='#c82423')
    add_title_label(ax, '11-2 第1题')
    ax.set_xlim(-6, 3.2)
    ax.set_ylim(-0.6, 0.6)
    ax.axis('off')
    fig.savefig(os.path.join(OUT, '初一', '11-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】12-1 第3题 — 扇形统计图
# ══════════════════════════════════════════════════════════════
def fig_12_1_3():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    sizes = [12, 18, 15, 5]
    labels = ['A等 (90-100)', 'B等 (80-89)', 'C等 (70-79)', 'D等 (60-69)']
    colors_pie = ['#4CAF50', '#2196F3', '#FF9800', '#f44336']
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                       colors=colors_pie, startangle=90,
                                       textprops={'fontsize': 10})
    for t in autotexts:
        t.set_fontsize(9)
        t.set_color('white')
    # 标注C等圆心角
    ax.text(0, -0.15, 'C等圆心角: 108°', ha='center', fontsize=11,
            color='#FF9800', fontweight='bold')
    add_title_label(ax, '12-1 第3题')
    fig.savefig(os.path.join(OUT, '初一', '12-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】12-2 第1题 — 扇形统计图
# ══════════════════════════════════════════════════════════════
def fig_12_2_1():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    sizes = [10, 16, 14]
    labels = ['语文 10人\n90°', '数学 16人\n144°', '英语 14人\n126°']
    colors_pie = ['#E91E63', '#2196F3', '#FF9800']
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='',
                                       colors=colors_pie, startangle=90,
                                       textprops={'fontsize': 10})
    add_title_label(ax, '12-2 第1题')
    fig.savefig(os.path.join(OUT, '初一', '12-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】3-1 第3题 — 火柴棒摆正方形
# ══════════════════════════════════════════════════════════════
def fig_3_1_3():
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.2))
    configs = [
        (1, [(0, 0)], '1个正方形: 4根'),
        (2, [(0, 0), (1.1, 0)], '2个正方形: 7根'),
        (3, [(0, 0), (1.1, 0), (2.2, 0)], '3个正方形: 10根'),
    ]
    for ax, (n, offsets, title) in zip(axes, configs):
        for ox, oy in offsets:
            x = [ox, ox+1, ox+1, ox, ox]
            y = [oy, oy, oy+1, oy+1, oy]
            ax.plot(x, y, color='#8B4513', lw=2.0)
        ax.set_aspect('equal')
        ax.set_xlim(-0.3, n*1.1+0.3)
        ax.set_ylim(-0.3, 1.3)
        ax.set_title(title, fontsize=10)
        ax.axis('off')
    fig.suptitle('火柴棒摆正方形规律: 3n+1', fontsize=12, y=1.02)
    add_title_label(axes[0], '3-1 第3题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初一', '3-1-3.png'))
    plt.close(fig)

# ══════════════════════════════════════════════════════════════
# 【初一】6-1 第4题 — 补角与余角
# ══════════════════════════════════════════════════════════════
def fig_6_1_4():
    fig, ax = plt.subplots(figsize=(6, 4))
    # 画一个角及补角余角示意
    O = np.array([0, 0])
    A = np.array([4, 0])
    B = np.array([3.06, 2.57])  # 40°方向
    C = np.array([-3, 0])  # 补角方向
    # 角AOB (x = 40°)
    ax.plot([O[0], A[0]], [O[1], A[1]], 'k-', lw=1.5)
    ax.plot([O[0], B[0]], [O[1], B[1]], 'k-', lw=1.5)
    ax.plot([O[0], C[0]], [O[1], C[1]], 'k--', lw=1.0, alpha=0.5)
    # 角度弧
    arc = Arc(O, width=1.0, height=1.0, theta1=0, theta2=40, color='#c82423', lw=1.5)
    ax.add_patch(arc)
    ax.text(0.7, 0.3, 'x = 40°', fontsize=11, color='#c82423')
    # 补角弧
    arc2 = Arc(O, width=1.6, height=1.6, theta1=40, theta2=180, color='#2196F3', lw=1.0, ls='--')
    ax.add_patch(arc2)
    ax.text(0.2, 1.1, '补角 140°', fontsize=9, color='#2196F3')
    # 余角弧
    arc3 = Arc(O, width=0.6, height=0.6, theta1=0, theta2=40, color='#4CAF50', lw=1.0, ls=':')
    # 余角示意 - 画一个垂直的线
    D = np.array([0, 3])
    ax.plot([O[0], D[0]], [O[1], D[1]], 'k-', lw=1.0, alpha=0.4)
    arc4 = Arc(O, width=0.7, height=0.7, theta1=40, theta2=90, color='#4CAF50', lw=1.0, ls=':')
    ax.add_patch(arc4)
    ax.text(0.15, 1.6, '余角 50°', fontsize=9, color='#4CAF50')
    # 标注
    ax.text(A[0]+0.1, A[1]-0.1, 'A', fontsize=11)
    ax.text(B[0]+0.1, B[1]+0.1, 'B', fontsize=11)
    ax.text(O[0]-0.15, O[1]-0.15, 'O', fontsize=11)
    ax.set_xlim(-3.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '6-1 第4题')
    fig.savefig(os.path.join(OUT, '初一', '6-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】6-3 第1题 — 补角与余角
# ══════════════════════════════════════════════════════════════
def fig_6_3_1():
    fig, ax = plt.subplots(figsize=(6, 4))
    O = np.array([0, 0])
    A = np.array([4, 0])
    # 设角为x，画一条斜线表示
    x_deg = 55  # 解为55°
    rad = np.radians(x_deg)
    B = np.array([4*np.cos(rad), 4*np.sin(rad)])
    ax.plot([O[0], A[0]], [O[1], A[1]], 'k-', lw=1.5)
    ax.plot([O[0], B[0]], [O[1], B[1]], 'k-', lw=1.5)
    arc = Arc(O, width=1.0, height=1.0, theta1=0, theta2=x_deg, color='#c82423', lw=1.5)
    ax.add_patch(arc)
    ax.text(0.8, 0.35, 'x = 55°', fontsize=11, color='#c82423')
    ax.text(A[0]+0.1, A[1]-0.1, 'A', fontsize=11)
    ax.text(B[0]+0.1, B[1]+0.1, 'B', fontsize=11)
    ax.text(O[0]-0.15, O[1]-0.15, 'O', fontsize=11)
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '6-3 第1题')
    # 补角余角关系文字
    ax.text(2.0, -0.5, '补角=3×余角+20°,  x=55°', ha='center', fontsize=10, color='#555')
    fig.savefig(os.path.join(OUT, '初一', '6-3-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】6-3 第2题 — 时钟角度
# ══════════════════════════════════════════════════════════════
def fig_6_3_2():
    fig, ax = plt.subplots(figsize=(4.5, 4.5))
    # 画钟面
    circle = Circle((0, 0), 2.0, fill=False, color='#333', lw=2.0)
    ax.add_patch(circle)
    # 刻度
    for h in range(1, 13):
        ang = np.radians(90 - h * 30)
        x1, y1 = 1.7 * np.cos(ang), 1.7 * np.sin(ang)
        x2, y2 = 2.0 * np.cos(ang), 2.0 * np.sin(ang)
        ax.plot([x1, x2], [y1, y2], 'k-', lw=1.0)
        ax.text(2.25*np.cos(ang), 2.25*np.sin(ang), str(h), ha='center', va='center', fontsize=10)
    # 3:15 时针在3点过7.5°，分针在3点
    # 分针指向3 (90°)
    minute_ang = 90  # 15分 = 90°
    hour_ang = 90 + 7.5  # 3点15分 = 97.5°
    # 分针
    ax.plot([0, 1.6*np.cos(np.radians(90-minute_ang))],
            [0, 1.6*np.sin(np.radians(90-minute_ang))], 'b-', lw=2.0, label='分针')
    # 时针
    ax.plot([0, 1.2*np.cos(np.radians(90-hour_ang))],
            [0, 1.2*np.sin(np.radians(90-hour_ang))], 'r-', lw=2.5, label='时针')
    # 中心点
    ax.plot(0, 0, 'o', color='#333', markersize=4)
    # 夹角弧
    arc = Arc((0, 0), width=0.6, height=0.6, theta1=90-hour_ang, theta2=90-minute_ang,
              color='#c82423', lw=1.5)
    ax.add_patch(arc)
    ax.text(0.55, 0.15, '7.5°', fontsize=10, color='#c82423')
    ax.legend(loc='lower right', fontsize=8)
    ax.set_aspect('equal')
    ax.set_xlim(-2.8, 2.8)
    ax.set_ylim(-2.8, 2.8)
    ax.axis('off')
    add_title_label(ax, '6-3 第2题')
    fig.savefig(os.path.join(OUT, '初一', '6-3-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-1 第2题 — 平行线 (AB∥CD, 求∠AEC)
# ══════════════════════════════════════════════════════════════
def fig_7_1_2():
    fig, ax = plt.subplots(figsize=(6, 4.5))
    # 两条平行线: AB 和 CD
    y_top, y_bot = 3, 0
    ax.plot([-0.5, 5.5], [y_top, y_top], 'k-', lw=1.5)
    ax.plot([-0.5, 5.5], [y_bot, y_bot], 'k-', lw=1.5)
    ax.text(-0.7, y_top, 'A', fontsize=12, va='center')
    ax.text(5.7, y_top, 'B', fontsize=12, va='center')
    ax.text(-0.7, y_bot, 'C', fontsize=12, va='center')
    ax.text(5.7, y_bot, 'D', fontsize=12, va='center')
    # 平行标记
    for y in [y_top, y_bot]:
        ax.plot([-0.3, -0.1], [y-0.12, y+0.12], 'k-', lw=1.0)
        ax.plot([-0.1, 0.1], [y-0.12, y+0.12], 'k-', lw=1.0)
    # 点E在AB和CD之间
    E = np.array([2.5, 1.5])
    ax.plot(E[0], E[1], 'o', color='#c82423', markersize=6, zorder=5)
    ax.text(E[0]+0.1, E[1]-0.2, 'E', fontsize=12, color='#c82423')
    # 连接AE和CE
    A_pt = np.array([2.5, y_top])
    C_pt = np.array([2.5, y_bot])
    # 过E作EF∥AB
    ax.plot([E[0], 5.5], [E[1], E[1]], 'r--', lw=1.0, alpha=0.7)
    ax.text(5.5, E[1], 'F', fontsize=10, color='r', va='center')
    # 角度标注
    # ∠A = 120° → ∠AEF = 60°
    annotate_angle_deg(ax, E, [5.5, E[1]], A_pt, 60, radius=0.5, color='#c82423')
    # ∠C = 130° → ∠FEC = 50°
    annotate_angle_deg(ax, E, C_pt, [5.5, E[1]], 50, radius=0.5, color='#2196F3')
    ax.text(2.5, 3.2, '∠A = 120°', ha='center', fontsize=10, color='#c82423')
    ax.text(2.5, -0.3, '∠C = 130°', ha='center', fontsize=10, color='#2196F3')
    ax.set_xlim(-1, 6)
    ax.set_ylim(-0.5, 3.8)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '7-1 第2题')
    fig.savefig(os.path.join(OUT, '初一', '7-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-1 第3题 — 4条直线交点
# ══════════════════════════════════════════════════════════════
def fig_7_1_3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    # 最多6个交点
    lines_max = [
        ([0, 4], [1, 4]),
        ([0.5, 3.5], [0, 3.5]),
        ([0, 3], [3, 0]),
        ([1, 4], [0, 3]),
    ]
    for (x1, x2), (y1, y2) in lines_max:
        ax1.plot([x1, x2], [y1, y2], 'k-', lw=1.3)
    ax1.set_title('最多6个交点', fontsize=11)
    ax1.set_xlim(-0.5, 4.5)
    ax1.set_ylim(-0.5, 4.5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    # 最少0个交点（全部平行）
    for i in range(4):
        ax2.plot([0, 4], [i, i], 'k-', lw=1.3)
    ax2.set_title('最少0个交点（平行）', fontsize=11)
    ax2.set_xlim(-0.5, 4.5)
    ax2.set_ylim(-0.5, 4.5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    add_title_label(ax1, '7-1 第3题')
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, '初一', '7-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-1 第5题 — 5条直线交点
# ══════════════════════════════════════════════════════════════
def fig_7_1_5():
    fig, ax = plt.subplots(figsize=(5, 5))
    # 2条平行线
    ax.plot([0, 5], [3, 3], 'b-', lw=2.0, label='平行线1')
    ax.plot([0, 5], [1, 1], 'b-', lw=2.0, label='平行线2')
    # 另外3条不平行线
    lines = [
        ([0, 5], [0, 5]),
        ([0, 5], [5, 0]),
        ([0, 5], [2, 4]),
    ]
    for (x1, x2), (y1, y2) in lines:
        ax.plot([x1, x2], [y1, y2], 'k-', lw=1.3)
    ax.set_title('5条直线（2条平行）最多9个交点', fontsize=11)
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(-0.5, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '7-1 第5题')
    fig.savefig(os.path.join(OUT, '初一', '7-1-5.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-2 第2题 — 平行线同位角
# ══════════════════════════════════════════════════════════════
def fig_7_2_2():
    fig, ax = plt.subplots(figsize=(6, 4))
    # 两条平行线
    ax.plot([0, 6], [2, 2], 'k-', lw=1.5)
    ax.plot([0, 6], [0, 0], 'k-', lw=1.5)
    ax.text(6.2, 2, 'a', fontsize=12)
    ax.text(6.2, 0, 'b', fontsize=12)
    # 平行标记
    for y in [0, 2]:
        ax.plot([5.7, 5.85], [y-0.08, y+0.08], 'k-', lw=1.0)
        ax.plot([5.85, 6.0], [y-0.08, y+0.08], 'k-', lw=1.0)
    # 截线
    ax.plot([0.5, 5.5], [2.5, -0.5], 'k-', lw=1.3)
    ax.text(5.7, -0.5, 'c', fontsize=12)
    # 标注∠1和∠2（同位角）
    # ∠1在a上方，∠2在b下方
    annotate_angle_deg(ax, [1.2, 2], [1.8, 2.5], [2.5, 2], 1, radius=0.35, color='#c82423')
    ax.text(1.6, 2.5, '∠1', fontsize=10, color='#c82423')
    annotate_angle_deg(ax, [3.2, 0], [4.5, 0], [3.8, -0.5], 1, radius=0.35, color='#2196F3')
    ax.text(3.6, -0.5, '∠2', fontsize=10, color='#2196F3')
    ax.text(1.8, 1.0, '∠1 = ∠2 → a ∥ b', fontsize=11, color='#c82423', ha='center')
    # ∠3和∠4
    annotate_angle_deg(ax, [4.0, 2], [4.5, 2.5], [5.0, 2], 3, radius=0.3, color='#E91E63')
    ax.text(4.4, 2.5, '∠3=110°', fontsize=9, color='#E91E63')
    annotate_angle_deg(ax, [4.5, 0], [5.5, 0], [5.0, 0.5], 4, radius=0.3, color='#9C27B0')
    ax.text(5.2, 0.3, '∠4=70°', fontsize=9, color='#9C27B0')
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1.0, 3.2)
    ax.set_aspect('equal')
    ax.axis('off')
    add_title_label(ax, '7-2 第2题')
    fig.savefig(os.path.join(OUT, '初一', '7-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-3 第2题 — 对顶角
# ══════════════════════════════════════════════════════════════
def fig_7_3_2():
    fig, ax = plt.subplots(figsize=(5, 4.5))
    # 两条相交直线
    ax.plot([-2.5, 2.5], [0, 0], 'k-', lw=1.5)
    ax.plot([0, 0], [-2.5, 2.5], 'k-', lw=1.5)
    O = np.array([0, 0])
    # 标注对顶角
    annotate_angle(ax, O, [2.5, 0], [0, 2.5], '∠1', radius=0.5, color='#c82423')
    annotate_angle(ax, O, [-2.5, 0], [0, -2.5], '∠2', radius=0.5, color='#c82423')
    annotate_angle(ax, O, [0, 2.5], [-2.5, 0], '∠3', radius=0.5, color='#2196F3')
    annotate_angle(ax, O, [0, -2.5], [2.5, 0], '∠4', radius=0.5, color='#2196F3')
    ax.text(0, -2.8, '对顶角相等: ∠1 = ∠2', ha='center', fontsize=11, color='#c82423')
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3.2, 3)
    ax.axis('off')
    add_title_label(ax, '7-3 第2题')
    fig.savefig(os.path.join(OUT, '初一', '7-3-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】7-4 第1题 — 坐标系平移
# ══════════════════════════════════════════════════════════════
def fig_7_4_1():
    fig, ax = plt.subplots(figsize=(6, 5))
    pts = {'A': (1, 2), 'B': (3, 4), 'C': (2, 1)}
    pts_t = {'A\'': (4, 0), 'B\'': (6, 2), 'C\'': (5, -1)}
    # 坐标轴
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-1, 7.5)
    ax.set_ylim(-2, 5.5)
    ax.grid(True, ls=':', alpha=0.3)
    # 原三角形
    for name, (x, y) in pts.items():
        ax.plot(x, y, 'o', color='#c82423', markersize=8, zorder=5)
        ax.text(x+0.1, y+0.1, name, fontsize=11, color='#c82423')
    xs = [p[0] for p in pts.values()] + [list(pts.values())[0][0]]
    ys = [p[1] for p in pts.values()] + [list(pts.values())[0][1]]
    ax.plot(xs, ys, 'r-', lw=1.5, label='原三角形')
    # 平移后三角形
    for name, (x, y) in pts_t.items():
        ax.plot(x, y, 'o', color='#2196F3', markersize=8, zorder=5)
        ax.text(x+0.1, y+0.1, name, fontsize=11, color='#2196F3')
    xs_t = [p[0] for p in pts_t.values()] + [list(pts_t.values())[0][0]]
    ys_t = [p[1] for p in pts_t.values()] + [list(pts_t.values())[0][1]]
    ax.plot(xs_t, ys_t, 'b-', lw=1.5, label='平移后三角形')
    # 平移箭头
    ax.annotate('', xy=(4, 0), xytext=(1, 2),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5, ls='--'))
    ax.text(1.5, 1.5, '→向右3\n↓向下2', fontsize=9, color='green')
    ax.legend(fontsize=9)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    add_title_label(ax, '7-4 第1题')
    fig.savefig(os.path.join(OUT, '初一', '7-4-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-1 第2题 — 坐标系象限
# ══════════════════════════════════════════════════════════════
def fig_9_1_2():
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-5.5, 5.5)
    ax.grid(True, ls=':', alpha=0.3)
    # 标注象限
    ax.text(2, 3, '第一象限\n(+, +)', ha='center', fontsize=9, color='#999')
    ax.text(-3, 3, '第二象限\n(-, +)', ha='center', fontsize=9, color='#999')
    ax.text(-3, -3, '第三象限\n(-, -)', ha='center', fontsize=9, color='#999')
    ax.text(2, -3, '第四象限\n(+, -)', ha='center', fontsize=9, color='#999')
    # 点P(3, -5)在第四象限
    ax.plot(3, -5, 'o', color='#c82423', markersize=10, zorder=5)
    ax.text(3.2, -5.2, 'P(3, -5)', fontsize=11, color='#c82423')
    # 虚线到坐标轴
    ax.plot([3, 3], [0, -5], 'k--', lw=0.8, alpha=0.4)
    ax.plot([0, 3], [-5, -5], 'k--', lw=0.8, alpha=0.4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('|x|=3, |y|=5, 第四象限 → P(3,-5)', fontsize=10)
    add_title_label(ax, '9-1 第2题')
    fig.savefig(os.path.join(OUT, '初一', '9-1-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-1 第3题 — 坐标系三角形面积
# ══════════════════════════════════════════════════════════════
def fig_9_1_3():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    pts = {'A': (2, 3), 'B': (-2, 1), 'C': (0, -2)}
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 4.5)
    ax.grid(True, ls=':', alpha=0.3)
    for name, (x, y) in pts.items():
        ax.plot(x, y, 'o', color='#c82423', markersize=8, zorder=5)
        ax.text(x+0.15, y+0.15, name, fontsize=12, color='#c82423')
    xs = [2, -2, 0, 2]
    ys = [3, 1, -2, 3]
    ax.plot(xs, ys, 'b-', lw=1.5)
    # 填充三角形
    ax.fill([2, -2, 0], [3, 1, -2], alpha=0.15, color='#2196F3')
    # 面积文字
    ax.text(0.5, 1.5, 'S = 8', fontsize=14, color='#2196F3', fontweight='bold',
            bbox=dict(boxstyle='round', fc='white', ec='#2196F3', alpha=0.8))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '9-1 第3题')
    fig.savefig(os.path.join(OUT, '初一', '9-1-3.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-1 第4题 — 坐标系平移
# ══════════════════════════════════════════════════════════════
def fig_9_1_4():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    pts = {'P': (3, -2), 'Q': (7, 1), 'Q\'(对称)': (-7, -1)}
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-8.5, 8.5)
    ax.set_ylim(-3.5, 3.5)
    ax.grid(True, ls=':', alpha=0.3)
    colors = ['#c82423', '#2196F3', '#4CAF50']
    for (name, (x, y)), c in zip(pts.items(), colors):
        ax.plot(x, y, 'o', color=c, markersize=8, zorder=5)
        ax.text(x+0.2, y+0.2, name, fontsize=11, color=c)
    # 平移箭头
    ax.annotate('', xy=(7, -2), xytext=(3, -2),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(5, -2.3, '→右移4', fontsize=9, color='green', ha='center')
    ax.annotate('', xy=(7, 1), xytext=(7, -2),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(7.3, -0.5, '↑上移3', fontsize=9, color='green')
    # 对称连线
    ax.plot([7, -7], [1, -1], 'k--', lw=0.8, alpha=0.4)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '9-1 第4题')
    fig.savefig(os.path.join(OUT, '初一', '9-1-4.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-1 第5题 — 判断三角形形状
# ══════════════════════════════════════════════════════════════
def fig_9_1_5():
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    pts = {'A': (1, 2), 'B': (5, 2), 'C': (3, 6)}
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.5, 7.5)
    ax.grid(True, ls=':', alpha=0.3)
    for name, (x, y) in pts.items():
        ax.plot(x, y, 'o', color='#c82423', markersize=8, zorder=5)
        ax.text(x+0.15, y+0.15, name, fontsize=12, color='#c82423')
    xs = [1, 5, 3, 1]
    ys = [2, 2, 6, 2]
    ax.plot(xs, ys, 'b-', lw=1.5)
    ax.fill([1, 5, 3], [2, 2, 6], alpha=0.12, color='#2196F3')
    # 边长标注
    ax.text(3, 1.7, 'AB = 4', ha='center', fontsize=10, color='#4CAF50')
    ax.text(3.5, 4.5, 'AC = 2√5', fontsize=10, color='#E91E63')
    ax.text(1.5, 4.5, 'BC = 2√5', fontsize=10, color='#E91E63')
    ax.text(3, 3.5, '等腰三角形', ha='center', fontsize=12, color='#c82423', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '9-1 第5题')
    fig.savefig(os.path.join(OUT, '初一', '9-1-5.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-2 第1题 — 坐标系平移
# ══════════════════════════════════════════════════════════════
def fig_9_2_1():
    fig, ax = plt.subplots(figsize=(5.5, 5))
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-6, 3)
    ax.grid(True, ls=':', alpha=0.3)
    # A和A'
    pts = {'A': (2, -1), 'A\'': (5, -5), 'B\'': (5, 2), 'B': (2, 6)}
    colors = {'A': '#c82423', 'A\'': '#2196F3', 'B\'': '#4CAF50', 'B': '#FF9800'}
    for name, (x, y) in pts.items():
        ax.plot(x, y, 'o', color=colors[name], markersize=8, zorder=5)
        ax.text(x+0.15, y+0.15, name, fontsize=11, color=colors[name])
    # 平移箭头 A→A'
    ax.annotate('', xy=(5, -1), xytext=(2, -1),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.2, ls='--'))
    ax.annotate('', xy=(5, -5), xytext=(5, -1),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.2, ls='--'))
    ax.text(3.5, -1.3, '→右3', fontsize=8, color='green', ha='center')
    ax.text(5.3, -3, '↓下4', fontsize=8, color='green')
    # 平移箭头 B'→B（反向）
    ax.annotate('', xy=(2, 6), xytext=(5, 2),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.2, ls='--'))
    ax.text(3.5, 4.5, '←左3, ↑上4', fontsize=8, color='purple', ha='center')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '9-2 第1题')
    fig.savefig(os.path.join(OUT, '初一', '9-2-1.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 【初一】9-2 第2题 — 三角形平移
# ══════════════════════════════════════════════════════════════
def fig_9_2_2():
    fig, ax = plt.subplots(figsize=(6, 5.5))
    ax.axhline(y=0, color='k', lw=1.0)
    ax.axvline(x=0, color='k', lw=1.0)
    ax.set_xlim(-2, 6.5)
    ax.set_ylim(-0.5, 8)
    ax.grid(True, ls=':', alpha=0.3)
    pts = {'A': (1, 2), 'B': (3, 4), 'C': (5, 1)}
    pts_t = {'A\'': (-1, 5), 'B\'': (1, 7), 'C\'': (3, 4)}
    for name, (x, y) in pts.items():
        ax.plot(x, y, 'o', color='#c82423', markersize=8, zorder=5)
        ax.text(x+0.12, y+0.12, name, fontsize=11, color='#c82423')
    xs = [1, 3, 5, 1]
    ys = [2, 4, 1, 2]
    ax.plot(xs, ys, 'r-', lw=1.5, label='原三角形')
    for name, (x, y) in pts_t.items():
        ax.plot(x, y, 'o', color='#2196F3', markersize=8, zorder=5)
        ax.text(x+0.12, y+0.12, name, fontsize=11, color='#2196F3')
    xs_t = [-1, 1, 3, -1]
    ys_t = [5, 7, 4, 5]
    ax.plot(xs_t, ys_t, 'b-', lw=1.5, label='平移后三角形')
    # 平移箭头
    ax.annotate('', xy=(0, 3.5), xytext=(2, 3.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(1, 3.7, '←左2', ha='center', fontsize=9, color='green')
    ax.annotate('', xy=(1, 4.5), xytext=(1, 2.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(1.3, 3.5, '↑上3', fontsize=9, color='green')
    ax.legend(fontsize=9)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_aspect('equal')
    add_title_label(ax, '9-2 第2题')
    fig.savefig(os.path.join(OUT, '初一', '9-2-2.png'))
    plt.close(fig)


# ══════════════════════════════════════════════════════════════
# 主函数（初一）
# ══════════════════════════════════════════════════════════════
def generate_all_chuyi():
    print("生成初一配图...")
    fig_11_2_1()
    print("  ✓ 11-2-1")
    fig_12_1_3()
    print("  ✓ 12-1-3")
    fig_12_2_1()
    print("  ✓ 12-2-1")
    fig_3_1_3()
    print("  ✓ 3-1-3")
    fig_6_1_4()
    print("  ✓ 6-1-4")
    fig_6_3_1()
    print("  ✓ 6-3-1")
    fig_6_3_2()
    print("  ✓ 6-3-2")
    fig_7_1_2()
    print("  ✓ 7-1-2")
    fig_7_1_3()
    print("  ✓ 7-1-3")
    fig_7_1_5()
    print("  ✓ 7-1-5")
    fig_7_2_2()
    print("  ✓ 7-2-2")
    fig_7_3_2()
    print("  ✓ 7-3-2")
    fig_7_4_1()
    print("  ✓ 7-4-1")
    fig_9_1_2()
    print("  ✓ 9-1-2")
    fig_9_1_3()
    print("  ✓ 9-1-3")
    fig_9_1_4()
    print("  ✓ 9-1-4")
    fig_9_1_5()
    print("  ✓ 9-1-5")
    fig_9_2_1()
    print("  ✓ 9-2-1")
    fig_9_2_2()
    print("  ✓ 9-2-2")
    print("初一配图完成!")
# 主入口
if __name__ == '__main__':
    generate_all_chuyi()
