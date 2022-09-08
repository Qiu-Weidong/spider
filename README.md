# 爬虫
通过英文查询汉字比较困难，这里将常用字的英文等翻译爬取了下来。爬取自[汉典](https://www.zdic.net/)

## 运行方法
首先在douban.py文件里面修改爬取的汉字范围(修改位置位于该文件下的9~11行)。
```shell
scrapy  crawl douban --nolog -o 保存文件名.json
```
