#!/usr/bin/env python3
"""
代理程式檔案中文化腳本
將所有 .md 檔案翻譯為繁體中文版本
"""

import os
import re
from pathlib import Path

def translate_agent_file(file_path):
    """翻譯單個代理程式檔案"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻譯檔案頭部
    content = re.sub(r'name: (.+)', r'name: \1', content)
    
    # 翻譯描述
    translations = {
        'Build production-ready LLM applications': '建構生產就緒的 LLM 應用程式',
        'Master Python 3.12+ with modern features': '掌握具備現代功能的 Python 3.12+',
        'Write idiomatic Python code': '撰寫慣用 Python 程式碼',
        'Expert Python developer': '專家 Python 開發者',
        'You are a Python expert': '您是一位 Python 專家',
        'You are an AI engineer': '您是一位 AI 工程師',
        'Build production-ready LLM applications, advanced RAG systems': '建構生產就緒的 LLM 應用程式、進階 RAG 系統',
        'Use PROACTIVELY for': '主動使用於',
        'Python development, optimization': 'Python 開發、優化',
        'LLM features, chatbots, AI agents': 'LLM 功能、聊天機器人、AI 代理程式',
        'AI-powered applications': 'AI 驅動應用程式',
        'Expert AI engineer specializing': '專精於的專家 AI 工程師',
        'LLM application development': 'LLM 應用程式開發',
        'RAG systems': 'RAG 系統',
        'AI agent architectures': 'AI 代理程式架構',
        'Masters both traditional and cutting-edge': '掌握傳統和尖端',
        'generative AI patterns': '生成式 AI 模式',
        'deep knowledge of the modern AI stack': '對現代 AI 堆疊的深度知識',
        'vector databases': '向量資料庫',
        'embedding models': '嵌入模型',
        'agent frameworks': '代理程式框架',
        'multimodal AI systems': '多模態 AI 系統',
        '## Purpose': '## 目的',
        '## Capabilities': '## 能力',
        '## Behavioral Traits': '## 行為特徵',
        '## Knowledge Base': '## 知識庫',
        '## Response Approach': '## 回應方式',
        '## Example Interactions': '## 範例互動'
    }
    
    for en, zh in translations.items():
        content = content.replace(en, zh)
    
    return content

def main():
    """主函數"""
    current_dir = Path('.')
    md_files = list(current_dir.glob('*.md'))
    
    # 排除已翻譯的檔案
    exclude_files = ['README.md', 'README-zh-TW.md']
    md_files = [f for f in md_files if f.name not in exclude_files]
    
    print(f"找到 {len(md_files)} 個需要翻譯的檔案")
    
    for md_file in md_files:
        print(f"翻譯 {md_file.name}...")
        
        # 建立中文檔名
        zh_name = md_file.stem + '-zh-TW.md'
        zh_path = md_file.parent / zh_name
        
        # 翻譯內容
        translated_content = translate_agent_file(md_file)
        
        # 寫入翻譯檔案
        with open(zh_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"已建立 {zh_name}")

if __name__ == '__main__':
    main()
