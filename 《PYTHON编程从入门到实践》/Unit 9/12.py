# 从三个模块user、privileges、admin 中进行调用，并且引用一个方法
from privileges_admin import Admin # privilege_admin 模块中已经调用了User类
admin_1 = Admin('Q.', 'Hz')
admin_1.privileges.show_privilege()