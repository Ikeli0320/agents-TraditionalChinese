#!/usr/bin/env python3
"""
使用 AI 進行代理程式檔案中文化
"""

import os
import re
from pathlib import Path

def create_translation_prompt(content):
    """建立翻譯提示"""
    return f"""
請將以下英文內容翻譯為繁體中文，保持 Markdown 格式和技術術語的準確性：

{content}

翻譯要求：
1. 保持原有的 Markdown 格式
2. 技術術語使用標準繁體中文翻譯
3. 保持專業和技術性的語調
4. 確保程式碼範例和配置保持不變
"""

def main():
    """主函數"""
    current_dir = Path('.')
    md_files = list(current_dir.glob('*.md'))
    
    # 排除已翻譯的檔案
    exclude_files = ['README.md', 'README-zh-TW.md']
    md_files = [f for f in md_files if f.name not in exclude_files]
    
    print(f"找到 {len(md_files)} 個需要翻譯的檔案")
    
    for md_file in md_files:
        print(f"處理 {md_file.name}...")
        
        # 讀取原始檔案
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 建立翻譯提示
        prompt = create_translation_prompt(content)
        
        # 建立中文檔名
        zh_name = md_file.stem + '-zh-TW.md'
        zh_path = md_file.parent / zh_name
        
        # 將提示寫入檔案供手動翻譯
        with open(zh_path, 'w', encoding='utf-8') as f:
            f.write(f"# 翻譯提示\n\n{prompt}\n\n# 原始內容\n\n{content}")
        
        print(f"已建立翻譯提示檔案 {zh_name}")

if __name__ == '__main__':
    main()
