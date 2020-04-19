import numpy as np
import pandas as pd
import datetime
class Data_Prep_shop(object):
    
# """
# 方法:__init__           传入sale表格的地址
#                         (datapath)  str
#                         (auto)      bool   Ture 将自动执行
#     shop_name_clean     店铺名称清理合并，删除特卖店铺
    
#     frequancy_filter    频次过滤
#                         （lower：uper） int,int
                        
#     depart_group_of_shop拆分为每个顾客下的店铺名单
    
#     save_shop_result    存储拆分好的数据
#                         （savename）Str

# """

    
    
    def __init__(self, salepath ='data/sales.csv',auto = False ):
        self.salep_path = salepath
        self.sale_df = pd.read_csv(salepath,encoding = 'UTF-8')
        if auto:
            self . shop_name_clean()

            self . frequancy_filter()
            self . depart_group_of_shop()
            self . save_shop_result('pros_1_')
            self . depart_group_of_cus()
            
            self . save_cus_result('pros_1_')
    def frequancy_filter(self,lower = 4,uper = 50000):
        dfsum = pd.DataFrame(self.sale_df.groupby(['会员卡号'])['消费金额'].count())
        dorp_index = dfsum[dfsum['消费金额']<lower].index
        sale_df_drop = self.sale_df.set_index('会员卡号').drop(dorp_index)
        dorp_index = dfsum[dfsum['消费金额']>uper].index
        sale_df_drop = sale_df_drop.drop(dorp_index)
        self.sale_df_drop_frequancy = sale_df_drop
    
    
    
    def shop_name_clean(self):
        sale_df = self.sale_df
        #sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:x[:-2] if (x[-2:] =='特卖') else x)
        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'特卖' if (x[-2:] =='特卖') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'fresh' if (x =='fresh馥蕾诗') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'fresh' if (x =='fersh 馥蕾诗') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'fila' if (x =='fila fusion') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'adidas' if (x =='adidas originals') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'adidas' if (x =='adidas neo') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'cafe de paris' if (x =='cafe de pairs') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'calvin klein' if (x =='ck jeans') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'calvin klein' if (x =='ck performance') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'calvin klein' if (x =='ck watch') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'calvin klein' if (x =='ck内衣') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:"d'zzit" if (x =='d‘zzit') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'hm' if (x =='h&m女装') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'hm' if (x =='h&m男装') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'hm' if (x =='h&m') else x)

        #sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'kappa' if (x =='kappa串标') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'kate' if (x =='kate spade') else x)

        #sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'loz' if (x =='loz拼装积木') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'max&co.' if (x =='max&co') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'nike' if (x =='nike360') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'nike' if (x =='nike篮球') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'polo' if (x =='polo sport') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'tea 2 go' if (x =='tea 2 go（三方）') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'the butchers club' if (x =='the butchers club、pizzagram') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'ugg' if (x =='ugg临时店') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'九木杂物社' if (x =='九木杂物 社') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'大嘴猴' if (x =='大嘴猴/dc') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'fila' if (x =='斐乐') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'新百伦' if (x =='new balance') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'杰克琼斯&斯莱德' if (x =='杰克琼斯&斯莱德&vm') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'ochirly' if (x =='欧时力特卖t08') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'ochirly' if (x =='欧时力') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'池田' if (x =='池田寿司') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'热风' if (x =='热 风') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'贡茶' if (x =='贡 茶') else x)

        sale_df['店铺名称'] = sale_df['店铺名称'].apply(lambda x:'ochirly' if (x =='欧时力') else x)
        
        sale_df=sale_df.drop(sale_df[sale_df['店铺名称']=='特卖'].index)
        
        self.sale_df = sale_df 
        
        
    def depart_group_of_shop(self):
        sale_df_dropa = self.sale_df_drop_frequancy[['店铺名称','交易日时']]
        com_list = list(set( self.sale_df_drop_frequancy.index))
        self.shop_list = com_list
        ll = len(com_list)
        
        allcomlist = [] 
        for j,i in enumerate(com_list):
            acc = list(sale_df_dropa.loc[i,:].sort_values(by = '交易日时')['店铺名称'])

            allcomlist.append(acc)
            if j%5000 ==0:
                print(j/ll)
        self . allcomlist = allcomlist
        
    def depart_group_of_cus(self):
        sale_df_dropa = self.sale_df_drop_frequancy
        shop_list = list(set(sale_df_dropa['店铺名称']))
        ll = len(shop_list)
        sale_df_dropa = sale_df_dropa[['店铺名称','交易时间']]
        sale_df_dropa = sale_df_dropa.reset_index().set_index('店铺名称')
        sale_df_dropa['交易时间'] = pd.to_datetime(sale_df_dropa['交易时间'])
        sale_df_dropa['weeks'] = sale_df_dropa['交易时间'].apply(lambda x: str(list(x.isocalendar())[0])+'_'+str(list(x.isocalendar())[1]))    
        wlist = sale_df_dropa['weeks'].unique()
        allcuslist = []
        for j,i in enumerate(shop_list):
            acc = (sale_df_dropa.loc[i,:].sort_values(by = '交易时间'))

            for k,l in enumerate(wlist):
                accc = acc[acc['weeks'] == l]
                acccl = list(accc.sort_values(by = '交易时间')['会员卡号'])
                allcuslist.append(acccl)
            if j%30 ==0:
                print(j/ll)
        self . allcuslist = allcuslist
        
    def depart_group_of_cus2(self):
        sale_df_dropa = self.sale_df_drop_frequancy
        shop_list = list(set(sale_df_dropa['店铺名称']))
        ll = len(shop_list)
        sale_df_dropa = sale_df_dropa[['店铺名称','交易时间']]
        sale_df_dropa = sale_df_dropa.reset_index().set_index('店铺名称')
        sale_df_dropa['交易时间'] = pd.to_datetime(sale_df_dropa['交易时间'])
        sale_df_dropa['weeks'] = sale_df_dropa['交易时间'].apply(lambda x: str(list(x.isocalendar())[0])+'_'+str(list(x.isocalendar())[1]))    
        wlist = sale_df_dropa['weeks'].unique()
        allcuslist = []
        for j,i in enumerate(shop_list):
            acc = (sale_df_dropa.loc[i,:].sort_values(by = '交易时间'))
            acccl  = list(acc.sort_values(by = '交易时间')['会员卡号'])
            allcuslist.append(acccl)
            if j%30 ==0:
                print(j/ll)
        self . allcuslist2 = allcuslist             
        
        
    def save_shop_result(self,savename):
        np.save('data/'+savename+'_shop',self .allcomlist)
        keys = list(set(self.sale_df_drop_frequancy['店铺名称']))
        np.save('data/'+savename+'_shop_key',keys)
                                                              
    def save_cus_result(self,savename):
        np.save('data/'+savename+'_cus',self .allcuslist)
        keys = list(set(self.sale_df_drop_frequancy.index))
        np.save('data/'+savename+'_cus_key',keys)
        
    def save_cus2_result(self,savename):
        np.save('data/'+savename+'_cus2',self .allcuslist2)
        keys = list(set(self.sale_df_drop_frequancy.index))
        np.save('data/'+savename+'_cus_key',keys)