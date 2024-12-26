# generate_json.py
import os
import json

# 获取当前目录下所有 .list 文件
list_files = [f for f in os.listdir('.') if f.endswith('.list')]

for list_file in list_files:
    # 初始化规则
    domain_keyword = []
    domain_suffix = []

    # 读取 .list 文件内容
    with open(list_file, 'r') as file:
        for line in file:
            if line.startswith('DOMAIN-KEYWORD,'):
                domain_keyword.append(line.strip().split(',', 1)[1])
            elif line.startswith('DOMAIN-SUFFIX,'):
                domain_suffix.append(line.strip().split(',', 1)[1])

    # 构建 JSON 数据
    json_data = {
        "version": 1,
        "rules": [
            {
                "domain_keyword": domain_keyword,
                "domain_suffix": domain_suffix
            }
        ]
    }

    # 写入对应的 JSON 文件
    json_file = list_file.replace('.list', '.json')
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=2)
