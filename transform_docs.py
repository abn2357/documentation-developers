import os
import re

def transform_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    yaml_end_index = -1
    title = None
    excerpt = None
    in_yaml = False
    yaml_boundary_count = 0

    for i, line in enumerate(lines):
        # 识别 YAML 边界 ---
        if line.strip() == '---':
            yaml_boundary_count += 1
            if yaml_boundary_count == 1:
                in_yaml = True
            elif yaml_boundary_count == 2:
                in_yaml = False
                yaml_end_index = i
            new_lines.append(line)
            continue

        if in_yaml:
            # 提取 title 字段
            if line.startswith('title:'):
                title = line.replace('title:', '', 1).strip().strip("'").strip('"')
            
            # 提取 excerpt 字段
            if line.startswith('excerpt:'):
                excerpt = line.replace('excerpt:', '', 1).strip().strip("'").strip('"')
            
            new_lines.append(line)
        else:
            # 标题降级逻辑：将 # 变为 ##，## 变为 ###
            if line.startswith('#'):
                new_lines.append('#' + line)
            else:
                new_lines.append(line)

    # 在 YAML 结束后插入内容
    if yaml_end_index != -1 and title:
        insertion_content = [f"\n# {title}\n"]
        
        # 如果 excerpt 有内容（不为空字符串且不是单引号/双引号占位），则插入
        if excerpt and excerpt.strip():
            insertion_content.append(f"\n{excerpt}\n")
            
        # 将构造好的标题和摘要插入到 YAML 结束后的位置
        for idx, text in enumerate(insertion_content):
            new_lines.insert(yaml_end_index + 1 + idx, text)

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 执行遍历
docs_dir = 'docs'
if not os.path.exists(docs_dir):
    print(f"错误: 找不到 {docs_dir} 文件夹")
else:
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                print(f"正在处理: {os.path.join(root, file)}")
                transform_markdown(os.path.join(root, file))
    print("\n✅ 处理完成！YAML 中的 title 已转为 # 标题，excerpt 已转为正文首段。")
