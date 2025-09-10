#!/usr/bin/env python3
"""
批次翻譯代理程式檔案為繁體中文
"""

import os
import shutil
from pathlib import Path

def create_chinese_agent_file(original_file, target_dir):
    """建立中文版代理程式檔案"""
    with open(original_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 基本翻譯對照表
    translations = {
        'name: ': 'name: ',
        'description: ': 'description: ',
        'model: ': 'model: ',
        'You are ': '您是一位',
        'You are an ': '您是一位',
        'Expert ': '專家',
        'Master ': '掌握',
        'Build ': '建構',
        'Write ': '撰寫',
        'Design ': '設計',
        'Create ': '建立',
        'Implement ': '實作',
        'Develop ': '開發',
        'Optimize ': '優化',
        'Analyze ': '分析',
        'Debug ': '除錯',
        'Test ': '測試',
        'Review ': '審查',
        'Manage ': '管理',
        'Configure ': '配置',
        'Deploy ': '部署',
        'Monitor ': '監控',
        'Troubleshoot ': '故障排除',
        '## Purpose': '## 目的',
        '## Capabilities': '## 能力',
        '## Behavioral Traits': '## 行為特徵',
        '## Knowledge Base': '## 知識庫',
        '## Response Approach': '## 回應方式',
        '## Example Interactions': '## 範例互動',
        'Use PROACTIVELY for': '主動使用於',
        'production-ready': '生產就緒',
        'modern features': '現代功能',
        'advanced features': '進階功能',
        'best practices': '最佳實踐',
        'performance optimization': '效能優化',
        'error handling': '錯誤處理',
        'testing strategies': '測試策略',
        'security considerations': '安全考量',
        'deployment strategies': '部署策略'
    }
    
    # 應用翻譯
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    # 建立中文檔名
    original_name = Path(original_file).stem
    chinese_name = f"{original_name}-zh-TW.md"
    target_path = target_dir / chinese_name
    
    # 寫入翻譯檔案
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return chinese_name

def main():
    """主函數"""
    current_dir = Path('.')
    target_dir = current_dir / 'zh-TW-agents'
    
    # 確保目標目錄存在
    target_dir.mkdir(exist_ok=True)
    
    # 取得所有 .md 檔案
    md_files = list(current_dir.glob('*.md'))
    
    # 排除不需要翻譯的檔案
    exclude_files = ['README.md', 'zh-TW-translation-guide.md']
    md_files = [f for f in md_files if f.name not in exclude_files]
    
    print(f"找到 {len(md_files)} 個需要翻譯的檔案")
    
    translated_count = 0
    for md_file in md_files:
        try:
            chinese_name = create_chinese_agent_file(md_file, target_dir)
            print(f"✓ 已建立 {chinese_name}")
            translated_count += 1
        except Exception as e:
            print(f"✗ 翻譯 {md_file.name} 時發生錯誤: {e}")
    
    print(f"\n翻譯完成！共處理 {translated_count} 個檔案")
    print(f"中文檔案位於: {target_dir}")

if __name__ == '__main__':
    main()
