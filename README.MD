## Flask拆分为简单迷你的MTV模式

依赖的库有:
- flask_script
- flask_sqlalchemy
- flask_migrate


## 文件目录结构
- manage.py
- app目录
    - \_\_init__.py初始化程序目录
    - ext.py 第三方库目录
    - settings.py 项目配置目录
    - models.py 模型定义文件
    - views 视图处理目录
        - \_\_init__.py 视图注册蓝图初始化
        - first.py 定义蓝图路由业务逻辑


文件目录很简单,就只有manage.py和app目录


manage.py是程序入口文件,用来运行flask和迁移数据库使用.

### 启动flask:
```python
python manage.py runserver -r -d
# 启动并开启自动重启调试模式
```

### 生成迁移文件
```python
python manage.py db init #初始化
python manage.py db migrate # 生成迁移文件
python manage.py db upgrade # 更新数据库并记录版本信息

```

### 启动之后的访问路径
首页: http://127.0.0.1:5000

其他测试路径在app/views/first.py文件中
