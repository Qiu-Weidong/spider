# 爬虫
通过英文查询汉字比较困难，这里将常用字的英文等翻译爬取了下来。爬取自[汉典](https://www.zdic.net/)

## 运行方法
首先在douban.py文件里面修改爬取的汉字范围(修改位置位于该文件下的9~11行)。
```shell
scrapy  crawl douban --nolog -o 保存文件名.json
```
## 汉字编码范围
|字符集      |   字数    |    16进制    |    十进制    |
|------------|----------|--------------|--------------|
|基本汉字    |20902      |4E00, 9FA5    |19968, 40869  |
|基本汉字补充|38	     |9FA6, 9FCB|40870, 40907|
|扩展A      |6582	    |3400, 4DB5|13312, 19893|
|扩展B      |42711	    |20000, 2A6D6|131072, 173782|
|扩展C      |222	    |2B740, 2B81D|177984, 178205|
|扩展D      |4149	    |2A700, 2B734|173824, 177972|
|兼容汉字   |477	    |F900, FAD9|63744, 64217|
|兼容扩展   |542	    |2F800, 2FA1D|194560, 195101|
|PUA增补    |207        |E600, E6CF|58880, 59087|
|〇         |1          |3007|12295|


