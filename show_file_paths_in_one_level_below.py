import os

# 現在のディレクトリパスを取得
current_dir = os.getcwd()

# 1階層下のディレクトリを取得
sub_dirs = [os.path.join(current_dir, d) for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))]

# 各サブディレクトリのファイルを一覧取得
for sub_dir in sub_dirs:
    print(f"Directory: {sub_dir}")
    files = os.listdir(sub_dir)
    for file in files:
        print(f"  - {file}")

