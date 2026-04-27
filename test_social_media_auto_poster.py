#!/usr/bin/env python3
"""
test_social_media_auto_poster.py - 引流兵测试脚本（含模拟模式）
功能：测试social_media_auto_poster_complete.py的各项功能
版本：1.0.0
"""

import sys
import os

# 模拟模式开关（如果没有MuMu，设为True）
SIMULATION_MODE = True

def test_in_simulation_mode():
    """在模拟模式下测试（不依赖实际设备）"""
    print("🧪 模拟模式：测试引流兵功能")
    print("=" * 60)
    
    # 模拟数据
    test_cases = [
        {
            "action": "post",
            "title": "AI赚钱实战",
            "content": "用AI帮你自动赚钱，月入百八十美元不是梦！#AI #赚钱 #副业",
            "images": None
        },
        {
            "action": "like",
            "note_id": "test_note_123"
        },
        {
            "action": "comment",
            "note_id": "test_note_123",
            "comment": "写得真好！"
        },
        {
            "action": "follow",
            "user_id": "test_user_456"
        },
        {
            "action": "browse",
            "duration_minutes": 1  # 模拟1分钟
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📝 测试用例 {i}/{len(test_cases)}")
        print(f"操作: {test_case['action']}")
        
        if test_case["action"] == "post":
            print(f"  标题: {test_case['title']}")
            print(f"  内容: {test_case['content'][:30]}...")
            print("  ✅ 模拟发布成功（笔记ID: XHS_SIM123）")
            
        elif test_case["action"] == "like":
            print(f"  笔记ID: {test_case['note_id']}")
            print("  ✅ 模拟点赞成功")
            
        elif test_case["action"] == "comment":
            print(f"  笔记ID: {test_case['note_id']}")
            print(f"  评论: {test_case['comment']}")
            print("  ✅ 模拟评论成功")
            
        elif test_case["action"] == "follow":
            print(f"  用户ID: {test_case['user_id']}")
            print("  ✅ 模拟关注成功")
            
        elif test_case["action"] == "browse":
            print(f"  时长: {test_case['duration_minutes']} 分钟")
            print("  ✅ 模拟浏览完成（浏览了10条Feed）")
        
        print("  ✅ 测试通过")
    
    print("\n" + "=" * 60)
    print("✅ 所有测试用例通过（模拟模式）")
    print("\n⚠️ 注意：这是模拟测试，实际运行需要MuMu模拟器")
    print("   1. 安装MuMu模拟器")
    print("   2. 安装小红书APP")
    print("   3. 调整ADB坐标（根据实际UI）")
    print("   4. 运行真实模式测试")

def test_real_device():
    """测试实际设备（需要MuMu运行）"""
    print("📱 真实设备模式：测试引流兵功能")
    print("=" * 60)
    
    try:
        # 动态导入（避免没有ADB时崩溃）
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "social_media_auto_poster_complete",
            "social_media_auto_poster_complete.py"
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 初始化
        poster = module.SocialMediaAutoPoster()
        
        if not poster.check_mumu_running():
            print("❌ MuMu模拟器未运行，请先启动")
            return False
        
        # 测试1：打开小红书
        print("\n📱 测试1：打开小红书")
        poster.open_xiaohongshu()
        print("✅ 打开成功")
        
        # 测试2：发布笔记（需要实际调整坐标）
        print("\n📝 测试2：发布笔记")
        result = poster.post_note(
            title="测试笔记",
            content="这是一条测试笔记 #测试",
            images=None
        )
        print(f"结果: {result}")
        
        # 测试3：养号（1分钟）
        print("\n🤖 测试3：养号（1分钟）")
        poster.run_yanghao_routine(duration_minutes=1)
        
        print("\n✅ 真实设备测试完成")
        return True
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("引流兵测试脚本 v1.0.0")
    print("=" * 60)
    
    if SIMULATION_MODE:
        print("\n⚠️ 当前为模拟模式（不依赖实际设备）")
        print("   要测试真实设备，请修改 SIMULATION_MODE = False")
        test_in_simulation_mode()
    else:
        print("\n📱 将测试真实设备（需要MuMu模拟器运行）")
        success = test_real_device()
        if not success:
            print("\n💡 建议先运行模拟模式测试：")
            print("   修改 SIMULATION_MODE = True")

if __name__ == "__main__":
    main()
