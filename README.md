# BS
## 毕业设计相关代码

此仓库包含北京交通大学交通运输学院匿名92号毕设必要程序及数据集

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

上述操作将在文件夹data下生成  
- '存储名称__cus.npy'
- '存储名称__cus2.npy'
- '存储名称__cus_key.npy'
- '存储名称__shop.npy'
- '存储名称__shop_key.npy'
五个数据集，key为唯一元素序列，其余为划分好的顾客/店铺序列

## Skip-gram词向量编码训练
```
from skip_grame.skip_gram import *
```
配置参数以shop为例：
```
#字典路径 key
keypath = 'data/存储名称_shop_key.npy'
#序列数据路径
datapath  ='data/存储名称_shop.npy'
# 编码维度
n_embedding = 3
# 负抽样数量
n_sampled = 5
#训练次数
epochs = 50
# 每批大小
batch_size = 1000
# 训练数据生成时的近邻窗口大小，代表中心词上下文最大可取到window_size内为与中心词相关的词
window_size = 5
#记录存储
ch_save = "checkpoints_close/text8.ckpt"
#编码向量的存储位置
savename='data/w2v_mat_cus_10_10000'
```
配置参数以cus作为训练时，window_size越大越好，推荐10000
```
#进行训练
Tdl = Train_data_load()
Tdl.auto_train(datapath,keypath,n_embedding ,\
n_sampled,\
epochs,\
batch_size,\
window_size,\
ch_save,\
savename=savename)
```
训练完成后将在data文件夹生成'w2v_mat_cus_10_10000.npy'文件

## 向量数据可视化
可视化中，对2维数据与3维数据不作降维处理，高于三维的数据才有T-SNE降维后可视化
```
from visualize.visualize import *
#对两种数据进行可视化，（'数据类型'，int(展示数量)）
plot_data('shop',100)
plot_data('cus',100)
```
