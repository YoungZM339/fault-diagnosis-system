# fault_diagnosis_system

## 运行前准备

1. 安装必备依赖
> sudo apt install python3 python3 python-is-python3 -y
> pip install requirements.txt

2. 设置了环境变量

> PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=fault_diagnosis_system.settings

3. 初始化数据库

> python ./manage.py makemigrations fault_diagnosis_system
> python ./manage.py migrate fault_diagnosis_system
> python ./manage.py makemigrations
> python ./manage.py migrate

4. 创建超级用户

> python ./manage.py createsuperuser
  
6. 启动Django

> python ./manage.py runserver 127.0.0.1:8000
