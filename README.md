# engine-hcraes

## termGenerator.py

该文件的主要作用在于原始文档的处理，Result是结果输出，形式是python的list。再次读入的时候使用python的eval函数即可。

### 提供的一些方法

* get_tokens_from_string 返回将string词条化以后的list，输入为一个string
* get_tokens_from_file 返回将文件内容词条化以后的list，输入为一个文件路径
* preprocessing 将一个目录下面的所有文件词条化

### 20190610

目前有两个设想，一是用Doc2Vec构建搜索系统，对于query直接给结果文档
二是利用Word2Vec实现近义词的查找，增强搜索的鲁棒性