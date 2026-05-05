# ComfyUI Mask to Points

[中文](#中文) | [English](#english)

---

## 中文

### 简介

将遮罩（Mask）转换为随机坐标点的 ComfyUI 自定义节点。从分割节点输出的遮罩中采样指定数量的随机点，输出为 SAM2 兼容的 JSON 坐标格式。

### 典型用途

1. 从任意分割节点（如 SAM3、YOLO 等）获取单张遮罩作为输入
2. 将遮罩输入 **Mask to Points** 节点，采样 N 个随机坐标点
3. 将坐标点作为 SAM2 的点提示输入，实现二次精修分割

### 安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/zhiruizz/comfyui_mask2points.git
```

重启 ComfyUI 即可。

### 节点说明

#### Mask to Points

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `mask` | MASK | — | 输入遮罩 |
| `num_points` | INT | 3 | 采样点数量（1~10000） |
| `seed` | INT | 0 | 随机种子，确保结果可复现 |

| 输出 | 类型 | 说明 |
|------|------|------|
| `points_json` | STRING | JSON 格式坐标，如 `[{"x": 240, "y": 750}, {"x": 540, "y": 700}]` |

---

## English

### Introduction

A ComfyUI custom node that converts masks into random coordinate points. Sample a specified number of random points from masks produced by segmentation models like SAM3, and output them as a JSON coordinate string compatible with SAM2 point prompts.

### Typical Workflow

1. Obtain a single mask from any segmentation node (e.g., SAM3, YOLO, etc.)
2. Feed the mask into the **Mask to Points** node to sample N random coordinate points
3. Use the coordinates as SAM2 point prompts for refined segmentation

### Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/zhiruizz/comfyui_mask2points.git
```

Restart ComfyUI after installation.

### Node Reference

#### Mask to Points

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `mask` | MASK | — | Input mask |
| `num_points` | INT | 3 | Number of points to sample (1–10000) |
| `seed` | INT | 0 | Random seed for reproducible results |

| Output | Type | Description |
|--------|------|-------------|
| `points_json` | STRING | JSON coordinates, e.g. `[{"x": 240, "y": 750}, {"x": 540, "y": 700}]` |
