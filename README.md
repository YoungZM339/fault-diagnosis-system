# fault_diagnosis_system

> Distributed System Fault Diagnosis System based on Machine Learning

![https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png](https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png)

![License](https://img.shields.io/github/license/youngzm339/fault-diagnosis-system)
![Issues](https://img.shields.io/github/issues/youngzm339/fault-diagnosis-system)
![Stars](https://img.shields.io/github/stars/youngzm339/fault-diagnosis-system)

## 运行前准备

1. 安装必备依赖

    `
    sudo apt install python3 python3 python-is-python3 -y
    `

    `
    pip install requirements.txt
    `

2. 设置了环境变量

    `
    DJANGO_SETTINGS_MODULE=fault_diagnosis_system.settings
    `

3. 初始化数据库

    `
    python ./manage.py makemigrations fault_diagnosis_system
    `

    `
    python ./manage.py migrate fault_diagnosis_system
    `

    `
    python ./manage.py makemigrations
    `

    `
    python ./manage.py migrate
    `

4. 创建超级用户

    `
    python ./manage.py createsuperuser
    `
  
5. 启动Django

    `
    python ./manage.py runserver 127.0.0.1:8000
    `
