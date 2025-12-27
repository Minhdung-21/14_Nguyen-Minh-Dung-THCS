import os

def tao_file_rong(path: str):
    with open(path, "a", encoding="utf-8"):
        pass

def in_cau_truc(root: str, indent: str = ""):
    items = sorted(os.listdir(root))
    for i, name in enumerate(items):
        full = os.path.join(root, name)
        is_last = (i == len(items) - 1)
        branch = "└── " if is_last else "├── "
        print(indent + branch + name)
        if os.path.isdir(full):
            next_indent = indent + ("    " if is_last else "│   ")
            in_cau_truc(full, next_indent)

if __name__ == "__main__":
    root = "my_project"
    src_dir = os.path.join(root, "src")
    docs_dir = os.path.join(root, "docs")
    data_dir = os.path.join(root, "data")

    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    tao_file_rong(os.path.join(src_dir, "main.py"))
    tao_file_rong(os.path.join(docs_dir, "README.md"))
    tao_file_rong(os.path.join(data_dir, "input.txt"))

    print(root + "/")
    in_cau_truc(root)
