# 声明

本软件仅供学习交流，如作他用所承受的法律责任一概与作者无关（下载使用即代表你同意上述观点）

# 商品后台管理系统
django+mongodb+hui 实现的后台管理系统

运行环境：windows10 + pytcharm + anaconda3 

实验前：需要在本地安装mongodb，并建立test数据库，以及在models.py创建相关表格

下载后将admin改名为myadmin, 并将static压缩文件解压到当前文件夹下

# mongodb 命令行下基本操作

连接远程mongodb: mongo ip地址：端口号

查看数据库： show dbs;

使用数据库： use test;

查看数据表： show collections;

删除goods表中address字段: db.goods.update({},{$unset:{'address':''}},false, true)

# mongodb 在django项目view.py常用操作

修改数据
``` python
def geditsubmit(request):
    gid = request.POST.get('gid')
    gname = request.POST.get('gname')
    gprice = request.POST.get('gprice')
    gsummary = request.POST.get('gsummary')
    Goods.objects(id=gid).update(gname=gname)
    Goods.objects(id=gid).update(gprice=gprice)
    Goods.objects(id=gid).update(gsummary=gsummary)
    return redirect('/product')
```
删除数据
``` python
def del_classes(request):
    nid = request.GET.get('nid')
    Goods.objects.filter(id=nid).first().delete()
    return redirect('/product')
```
查找数据
``` python
def index(request):
    goods = Goods.objects
    context = {
        'GoodsInfo':goods
    }
    return render(request, 'product-list.html', context) # 传递context参数,参数必须是字典形式传递到前端
```

# django 踩坑记录

页面样式，js文件经常出现路径不对，找不到页面中的样式文件，解决办法：

1、项目根目录创建static文件夹

2、在setting.py 中添加：

``` python
  STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
  STATIC_URL = '/static/'
  STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__), '../static/').replace('\\', '/'),)
```

3、在urls.py 中添加：

``` python
from django.contrib.staticfiles.urls import static
from . import settings
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

4、在根目录的templates中的html文件中首行添加：
``` html
{% load staticfiles %}
```
样式文件如下：
``` html
<link rel="stylesheet" type="text/css" href="{% static 'css/h-ui/css/H-ui.min.css' %}" />
```

# 运行结果
![](https://github.com/liuluyeah/admin/blob/master/result/%E7%99%BB%E5%BD%95.png)

![](https://github.com/liuluyeah/admin/blob/master/QQ%E5%9B%BE%E7%89%8720180503160841.png)

![](https://github.com/liuluyeah/admin/blob/master/result/%E5%9B%BE.png)
