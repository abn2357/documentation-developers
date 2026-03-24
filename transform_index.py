import json
import os

# 原始路径
index_path = 'site/search/search_index.json'
# 新的输出路径
output_path = 'site/search/develop_search_index.json'

def transform_location(loc):
    parts = loc.strip('/').split('/')
    if not parts or parts == ['']:
        return loc
    last_part = parts[-1]
    if '#' in last_part:
        if len(parts) >= 3:
            return f"{parts[0]}/{parts[-2]}/{parts[-1]}"
        else:
            return loc
    else:
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[-1]}/"
        else:
            return loc

if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for doc in data.get('docs', []):
        doc['location'] = transform_location(doc.get('location', ''))

    # 修改此处：将 f 写入到 output_path
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    
    print(f"✅ 优化完成！新文件已生成至: {output_path}")
else:
    print("❌ 找不到原始 search_index.json")
