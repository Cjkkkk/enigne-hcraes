# engine-hcraes

## termGenerator.py

该文件的主要作用在于原始文档的处理，Result是结果输出，形式是python的list。再次读入的时候使用python的eval函数即可。

### 提供的一些方法

* get_tokens_from_string 返回将string词条化以后的list，输入为一个string
* get_tokens_from_file 返回将文件内容词条化以后的list，输入为一个文件路径
* preprocessing 将一个目录下面的所有文件词条化