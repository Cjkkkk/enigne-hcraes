# PySrc
代码主要是关于排序。
排序的入口是实例化一个RankDemo,然后调用rank（需要传入sentence和待排列的document），得到排序好的列表。

实现主要分为两部分
一部分是RankDemo的运行代码
另一部分是文件夹model中的文件，主要训练包括Word2Vec, PCA和cluster，最终经过pca的是一个90维向量。

Document:是我用来表示文档的类，里面有几个变量，name,url,title,clusters,就是比数据库多了一个clusters，用继承tuple方式实现，所以和searchDemo里兼容
# todo list
一部分是我生成的cluster要存在数据库，这部分没交接好。
cluster 可以通过cluster.py (./model)算出来，但还没存进数据库

＃ 接口交接
数据库接口：tf-idf交接已经做好，cluster还没
与上层接口：做好，但是无法运行（因为缺少cluster）