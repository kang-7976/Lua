import os
import glob

def super_search(root_dir, keyword, search_type='name'):
    matched_files = []
    # 设置一个上限，防止全盘扫描把手机卡死
    MAX_LIMIT = 500 
    
    print(f"🚀 正在全盘暴力搜索中... (最多展示前 {MAX_LIMIT} 个结果)\n")

    # 过滤掉系统文件夹，加快扫描速度
    def filter_dirs(dirs):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['Android', 'LOST.DIR', 'system', 'data']]

    # 方式1：按后缀全盘翻找 (使用 glob 递归匹配)
    if search_type == 'ext':
        # 确保后缀带点，比如输入 pdf 自动转为 *.pdf
        ext = keyword if keyword.startswith('.') else f'.{keyword}'
        # ** 代表递归搜索所有子目录
        search_pattern = os.path.join(root_dir, '**', f'*{ext}')
        
        # iglob 是迭代器，找到一个吐一个，非常省内存
        for file_path in glob.iglob(search_pattern, recursive=True):
            if os.path.isfile(file_path): # 确保是文件不是文件夹
                matched_files.append(file_path)
                if len(matched_files) >= MAX_LIMIT:
                    print("⚠️ 文件太多啦，已为你暂停搜索！")
                    break

    # 方式2：按全称/部分名称搜索 (使用 os.walk 深度遍历)
    elif search_type == 'name':
        for dirpath, dirnames, filenames in os.walk(root_dir):
            filter_dirs(dirnames) # 过滤垃圾文件夹
            
            for filename in filenames:
                if keyword.lower() in filename.lower(): # 忽略大小写匹配
                    matched_files.append(os.path.join(dirpath, filename))
                    if len(matched_files) >= MAX_LIMIT:
                        print("⚠️ 文件太多啦，已为你暂停搜索！")
                        break
            if len(matched_files) >= MAX_LIMIT:
                break

    return matched_files

if __name__ == "__main__":
    # 安卓手机通用内部存储路径
    default_path = '/storage/emulated/0' 
    
    print("📱 欢迎使用手机文件暴力搜索神器！")
    print("请选择搜索方式：")
    print("1. 按后缀全盘翻找 (例如输入 .pdf 或 pdf，翻出所有PDF)")
    print("2. 按名称/全称搜索 (例如输入 简历，翻出所有带这两个字的文件)")
    
    choice = input("请输入数字(1/2)：").strip()
    keyword = input("请输入你的关键词：").strip()
    
    search_type = 'ext' if choice == '1' else 'name'
    
    # 开始搜索
    results = super_search(default_path, keyword, search_type)
    
    if results:
        print(f"\n🎉 战果汇报：共翻出 {len(results)} 个相关文件：")
        for i, path in enumerate(results, 1):
            print(f"{i}. {path}")
    else:
        print("\n😭 翻遍了整个手机，也没找到相关文件。")
#共创 kang-7976,chatGPT

