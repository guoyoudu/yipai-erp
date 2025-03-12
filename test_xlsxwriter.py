#!/usr/bin/env python3.10

try:
    import xlsxwriter
    print('成功导入xlsxwriter模块!')
    print('xlsxwriter版本:', xlsxwriter.__version__)
except ImportError as e:
    print('导入xlsxwriter模块失败:', e)

print('Python路径信息:')
import sys
for path in sys.path:
    print(path)