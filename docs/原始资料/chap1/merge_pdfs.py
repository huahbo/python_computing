import os
import argparse
from PyPDF2 import PdfMerger
from typing import List, Union
import re

def validate_path_exists(path: str, is_file: bool = False) -> None:
    """验证路径是否存在且类型正确"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"路径不存在: {path}")
    if is_file and not os.path.isfile(path):
        raise ValueError(f"路径不是文件: {path}")
    if not is_file and not os.path.isdir(path):
        raise ValueError(f"路径不是文件夹: {path}")

def natural_keys(text):
    """自然排序辅助函数"""
    return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]

def get_pdf_files_sorted(folder_path: str) -> List[str]:
    """获取文件夹中PDF文件（自然排序）"""
    pdf_files = []
    for entry in os.scandir(folder_path):
        if entry.is_file() and entry.name.lower().endswith(".pdf"):
            pdf_files.append(entry.path)
    pdf_files.sort(key=lambda x: natural_keys(os.path.basename(x)))
    return pdf_files

def merge_pdfs(input_paths: Union[str, List[str]], output_path: str) -> None:
    """合并PDF（彻底修复资源管理）"""
    # 支持逗号分隔的多个文件
    if isinstance(input_paths, str):
        if ',' in input_paths:
            input_paths = [p.strip() for p in input_paths.split(',')]
        else:
            input_paths = [input_paths]
    
    all_files = []
    for path in input_paths:
        try:
            if os.path.isdir(path):
                files_in_dir = get_pdf_files_sorted(path)
                if not files_in_dir:
                    print(f"警告：跳过空文件夹 {path}")
                    continue
                all_files.extend(files_in_dir)
            else:
                validate_path_exists(path, is_file=True)
                all_files.append(path)
        except Exception as e:
            print(f"警告：跳过无效路径 {path}（错误: {str(e)}）")
    
    if not all_files:
        raise ValueError("无有效PDF文件可合并")
    
    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    merger = PdfMerger()
    try:
        for pdf_path in all_files:
            merger.append(pdf_path)
            print(f"已添加: {pdf_path}")
        with open(output_path, "wb") as out_file:
            merger.write(out_file)
        print(f"✓ 合并完成: {output_path}")
    except Exception as e:
        raise RuntimeError(f"合并失败: {str(e)}")
    finally:
        # PyPDF2 的 PdfMerger 有 close 方法，部分版本没有，可安全忽略
        try:
            merger.close()
        except Exception:
            pass

def main():
    parser = argparse.ArgumentParser(description="PDF合并工具（修复版）")
    parser.add_argument("-i", "--input", required=True, help="输入路径（文件/文件夹/逗号分隔多个文件）")
    parser.add_argument("-o", "--output", required=True, help="输出文件路径")
    args = parser.parse_args()
    
    try:
        merge_pdfs(args.input, args.output)
        print("操作成功！")
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()


# 场景 1：合并文件夹中的所有 PDF​​
# 假设文件夹 ./input_pdfs包含多个 PDF 文件，执行以下命令：
# python merge_pdfs.py -i ./input_pdfs -o ./merged.pdf

# ​​场景 2：合并指定的多个 PDF 文件​​
# 手动指定 3 个 PDF 文件路径：
# python merge_pdfs.py -i "file1.pdf,file2.pdf,file3.pdf" -o ./merged.pdf

# （注意：Windows 系统需用双引号包裹路径，Linux/macOS 可用单引号或双引号）