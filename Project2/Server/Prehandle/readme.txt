FileHanle模块：
预处理模块，内有pretreatment的方法，接受四个参数(addpre, addpost, numOfFile, addlist)，因为要批量处理文件，文件的地址格式为'addpre+i+addposrt'，i代表整数。numOfFile代表文件的数目，addlist代表文件与对应url的索引表。
该函数的功能有预处理，将结果存入数据库PretreatmentInfo.db中，共有5张表。
InvertedFile表，内有两个属性（WORD，FileNumber），WORD代表单词，FileNumber是由对应文件组成的字符串，文件间用空格分隔。

tf_idf表，内有三个属性（FileID，WORD，VALUE），WORD代表单词，FileID代表文件序号，VALUE代表该词对应的TF-IDF的值。

urlTitleIndex表，内有三个属性（FileID，Title，URL），FileID代表文件序号，Title代表文章的标题，URL代表对应的URL。

这里已经预处理了标点符号，由于tf-idf方法的关系不再处理常用词。


SearchDemo模块
搜索模块，内有Search函数，接受一个字符串做参数，返回一个列表。列表中每一个元素是一个元组，（文件序号 整数，文件标题 字符串，文件url 字符串）