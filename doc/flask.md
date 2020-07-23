## flask

### 入口函数

在setup.py中定义,如下所示

```
entry_points={"console_scripts": ["flask = flask.cli:main"]},
```

flask的命令行是通过click模块开发的，所以先简单介绍一下click模块的使用.这个例子用的是click.Group的方式实现的.
需要创建一个Group类继承自click.Group，然后再用@click.command方式建一个具体的命令，然后通过add_command方法加入到组中.这样就实现了一个最简单的命令行框架



