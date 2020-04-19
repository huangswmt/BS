# BS
## 毕业设计相关代码

此仓库包含北京交通大学电子商务16251118毕设必要程序及数据集

## 数据预处理
请在主目录下运行命令


```
from data_process.process_data import *
```
自动处理数据
```
DPS = Data_Prep_shop(auto = True)
```
手动处理数据
```
-----------------------
DPS = Data_Prep_shop(auto = False)
-----------------------
#第一步： 清洗数据
DPS.shop_name_clean()
-----------------------
#第二步： 过滤过低消费频次顾客
DPS.frequancy_filter()
-----------------------
#第三步： 将交易记录DataFrame中的数据划分成为序列数据
#提供了三种划分方式
  # 第一种 按照顾客购物篮中的店铺序列生成店铺序列
DPS.depart_group_of_shop()
  # 第二种 按照店铺中顾客的访问顺序生成顾客序列
DPS.depart_group_of_cus()  
  # 第三种 按照店铺中顾客的访问顺序及访问发生的时间（xx年xx周）生成顾客序列
DPS.depart_group_of_cus2()
-----------------------
#第四步： 存储数据，对应第三步三种方法
DPS.save_shop_result('存储名称')
DPS.save_cus_result('存储名称')
DPS.save_cus2_result('存储名称')
```
