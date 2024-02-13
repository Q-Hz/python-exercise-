# 导入Admin 并调用其中一个方法
from user_privileges_admin import Admin
admin_1 =Admin('Q', 'Hz')
admin_1.privileges.show_privilege()
print()
admin_1.describe_user()