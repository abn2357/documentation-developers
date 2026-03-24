import json
import os

# 搜索索引文件的路径（通常在 site/search/search_index.json）
index_path = 'site/search/search_index.json'

def transform_location(loc):
    # 移除首尾的斜杠并按斜杠分割
    parts = loc.strip('/').split('/')
    
    if not parts or parts == ['']:
        return loc

    # 处理逻辑：
    # 1. 检查最后一部分是否包含锚点 #
    last_part = parts[-1]
    
    if '#' in last_part:
        # 如果最后一部分包含 #，保留第一部分 + 最后两部分
        # 例如: a/b/c/d/#hash -> a/d/#hash
        if len(parts) >= 3:
            return f"{parts[0]}/{parts[-2]}/{parts[-1]}"
        else:
            return loc # 层级太浅则保持原样
    else:
        # 如果不含 #，保留第一部分 + 最后一部分
        # 例如: docs/Build Node/deploy/ -> docs/deploy/
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[-1]}/"
        else:
            return loc

# 1. 读取原始索引
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 遍历并修改所有 docs 的 location
    for doc in data.get('docs', []):
        old_loc = doc.get('location', '')
        new_loc = transform_location(old_loc)
        doc['location'] = new_loc

    # 3. 写回文件
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    print(f"✅ 已成功优化 {len(data['docs'])} 条索引路径！")
else:
    print("❌ 找不到 search_index.json，请先运行 mkdocs build")
