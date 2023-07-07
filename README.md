# fault_diagnosis_system

## 运行前准备

1. 安装必备软件包

> pip install requirements.txt

2. 设置了环境变量

> PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=fault_diagnosis_system.settings

3. 启动Django

> python .\manage.py runserver 127.0.0.1:8000

## Tips

- 预设了用户admin，密码admin，已具有管理员权限
- 内置Django管理系统({base_url}/admin)，管理系统可增删改用户和相关数据