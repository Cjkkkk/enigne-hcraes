# ReadMe
## requirements
you can see all the requirements in `requirements.txt`, then you can install them by pip.
### using pip
```bash
pip install -r requirements.txt
```
## web server run
python run_server.py
the web server will run, and you can browse the page in your browser.

```bash
python server/runserver.py
```
## python script
change the sentence you want to search in main.py, and then
python main.py


# engine-hcraes

## requirement

要有数据集在根目录，有Result文件夹在根目录

## termGenerator.py

该文件的主要作用在于原始文档的处理，Result是结果输出，形式是python的list。再次读入的时候使用python的eval函数即可。

## main.py

总入口

## InvertedIndex.py

InvertedIndex.txt为带位置信息的倒排索引dict输出，Hash表索引貌似就可以了？
