#!/usr/bin/env python3
"""
AI 代理程式中文化工具
使用 Ollama Gemma3:12B 模型進行翻譯
"""

import os
import json
import requests
import time
from pathlib import Path

def translate_with_gemma(text, model="gemma3:12b"):
    """使用 Gemma 模型翻譯文字"""
    url = "http://localhost:11434/api/generate"
    
    prompt = f"""請將以下英文內容翻譯為繁體中文，保持 Markdown 格式：

{text}"""
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "max_tokens": 4000
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except Exception as e:
        print(f"翻譯錯誤: {e}")
        return None

def translate_file(file_path, model="gemma3:12b"):
    """翻譯單個檔案"""
    print(f"翻譯 {file_path.name}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 翻譯
    translated = translate_with_gemma(content, model)
    if not translated:
        return False
    
    # 備份原檔案
    backup_path = file_path.with_suffix('.md.backup')
    if not backup_path.exists():
        file_path.rename(backup_path)
        file_path = Path(file_path.name)
    
    # 儲存翻譯結果
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print(f"✓ 完成 {file_path.name}")
    return True

def get_files_to_translate():
    """取得需要翻譯的檔案清單"""
    current_dir = Path('.')
    all_files = list(current_dir.glob('*-zh-TW.md'))
    
    # 過濾掉已經完全中文化的檔案
    files_to_translate = []
    for file_path in all_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 簡單檢查是否還有大量英文內容
        english_words = len([word for word in content.split() if word.isalpha() and word.isascii() and len(word) > 2])
        total_words = len(content.split())
        
        if english_words > total_words * 0.1:  # 如果英文單字超過 10%
            files_to_translate.append(file_path)
    
    return files_to_translate

def main():
    """主函數"""
    print("AI 代理程式中文化工具")
    print("使用 Ollama Gemma3:12B 模型")
    print("=" * 50)
    
    files_to_translate = get_files_to_translate()
    
    if not files_to_translate:
        print("所有檔案已經完全中文化！")
        return
    
    print(f"找到 {len(files_to_translate)} 個需要翻譯的檔案")
    
    success_count = 0
    for i, file_path in enumerate(files_to_translate, 1):
        print(f"\n[{i}/{len(files_to_translate)}] 處理 {file_path.name}")
        success = translate_file(file_path)
        if success:
            success_count += 1
        time.sleep(2)  # 避免過快請求
    
    print(f"\n翻譯完成！成功: {success_count}/{len(files_to_translate)}")
    
    if success_count < len(files_to_translate):
        print("\n部分檔案翻譯失敗，可能原因：")
        print("1. Ollama 服務未啟動")
        print("2. 模型載入中，請稍後再試")
        print("3. 檔案過大導致超時")

if __name__ == '__main__':
    main()
