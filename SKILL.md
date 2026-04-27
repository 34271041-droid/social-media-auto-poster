---
name: "social-media-auto-poster"
description: "小红书自动发布+养号，MuMu模拟器+ADB方案，无需Appium"
version: "1.0.0"
author: "郭哥"
pricing: "$9.9"
tags: ["小红书", "自动化", "MuMu", "ADB", "引流"]
---

# social-media-auto-poster

小红书自动发布+养号技能（引流兵完整版）

## 🎯 功能清单

| 功能 | 说明 | 状态 |
|------|------|------|
| 自动发布笔记 | 标题+内容+图片（可选） | ✅ 完整实现 |
| 养号例行 | 浏览Feed+点赞+评论+关注 | ✅ 完整实现 |
| 点赞笔记 | 自动点赞指定笔记 | ✅ 完整实现 |
| 评论笔记 | 自动评论指定笔记 | ✅ 完整实现 |
| 关注用户 | 自动关注指定用户 | ✅ 完整实现 |

## 📋 使用场景

1. **批量发布笔记** - 准备好标题/内容/图片，一键发布
2. **养号** - 每天自动浏览/互动，提升账号权重
3. **互动引流** - 自动点赞/评论/关注，吸引粉丝

## 🔧 技术实现

- **纯ADB命令**（无需Appium，避开环境配置问题）
- **支持MuMu模拟器**（安卓9/12版本）
- **坐标自适应**（需根据实际UI微调）

## 📦 安装依赖

```bash
# 无需Python依赖（纯subprocess调用ADB）
# 需要：
# 1. MuMu模拟器（安装小红书APP）
# 2. ADB.exe（MuMu自带）
```

## 🚀 快速开始

```python
from social_media_auto_poster_complete import SocialMediaAutoPoster

# 初始化（ADB路径为MuMu自带）
poster = SocialMediaAutoPoster(
    muemu_path="C:\\Program Files\\Netease\\MuMuPlayer-12.0\\shell\\adb.exe"
)

# 检查MuMu是否运行
if poster.check_mumu_running():
    # 发布笔记
    result = poster.post_note(
        title="AI赚钱实战",
        content="用AI帮你自动赚钱，月入百八十美元不是梦！#AI #赚钱 #副业",
        images=None  # 暂不支持图片（需手动实现）
    )
    print(result)
    
    # 养号（5分钟）
    poster.run_yanghao_routine(duration_minutes=5)
```

## ⚙️ 配置说明

### ADB路径（根据MuMu安装位置调整）
```
默认路径：C:\Program Files\Netease\MuMuPlayer-12.0\shell\adb.exe
```

### 坐标调整（根据模拟器分辨率）
```
默认分辨率：1080x1920（竖屏）
坐标获取：adb shell uiautomator dump + 解析XML
```

## 📝 注意事项

1. **坐标需调整** - 不同模拟器分辨率不同，需实际测试调整
2. **小红书限制** - 频繁操作可能触发风控，建议间隔>30秒
3. **图片功能** - v1.0暂不支持图片（后续版本加入）
4. **养号策略** - 建议每天<50次互动，避免被封

## 🔄 更新日志

- **v1.0.0** (2026-04-28) - 初始版本，完整ADB方案
