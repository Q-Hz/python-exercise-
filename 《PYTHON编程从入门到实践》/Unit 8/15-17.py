# 15 导入printing_functions 模块 中的print_models 函数
import printing_functions as printing
unprinted_models =['A', 'B', 'C']
completed_models = []
printing.print_models(unprinted_models,completed_models)

# 16 用各种方法导入 printing_magician_name 模块中的magician_name_list 函数
# 法一
import printing_magician_name
magician_list =['A', 'B', 'C']
printing_magician_name.magician_name_list(magician_list)
# 法二
from printing_magician_name import magician_name_list
magician_list =['A', 'B', 'C']
magician_name_list(magician_list)
# 法三
from printing_magician_name import magician_name_list as mnl
magician_list =['A', 'B', 'C']
mnl(magician_list)
# 法四
import printing_magician_name as pmn
magician_list =['A', 'B', 'C']
pmn.magician_name_list(magician_list)
# 法五
from printing_magician_name import *
magician_list =['A', 'B', 'C']
magician_name_list(magician_list)