import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
my_font =  {'family' : 'MicroSoft YaHei',  'weight' : 'bold', 'size'   : 'larger'}
matplotlib.rc("font",)
my_font = font_manager.FontProperties(fname="../font/simhei.ttf")


class first_Predict_shop(object):
    
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

    
    
    def __init__(self, salepath ='../data/sales.csv',auto = False ):
        self.salep_path = salepath
        self.sale_df = pd.read_csv(salepath,encoding = 'UTF-8')
        if auto:
            self . shop_name_clean()
            self . frequancy_filter()
            self . depart_group_of_shop()
            self . depart_group_of_cus()
            self . save_shop_result('pros_1_')
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
        
        
#     def form_df_list(self,read=False):
#         if not read:
#             dff = self.sale_df_drop_frequancy
#             dff =dff .reset_index()
#             dffa = dff.sort_values(by = ['会员卡号','交易日时'])
#             listType = dffa['会员卡号'].unique()
#             dflist = []
#             for i in listType:
#                 dflist.append(dffa[dffa['会员卡号'].isin([i])])
#             self.dflist = dflist 
#         else:
            
    def get_one(self,windows=5):
        dff1 = self.sale_df_drop_frequancy
        dff1 =dff1 .reset_index()
        dff1 = dff1.sort_values(by = '交易时间')
        gdf_regin = dff1.groupby(['会员卡号','交易时间','店铺名称','消费金额'])['交易日时'].sum()
        gdf_regin = pd.DataFrame(gdf_regin).reset_index([1,2,3])
        gdf_regin['交易时间'] = pd.to_datetime(gdf_regin['交易时间'])
        dffli = []
        for i in range(windows):

            gdf = gdf_regin.copy()
            gdf['交易时间'] = pd.to_datetime(gdf['交易时间'])
            gdf['shift_shop'] = gdf.groupby(['会员卡号',])['店铺名称'].shift(-1*(i+1))
            gdf['shift_time'] = gdf.groupby(['会员卡号'])['交易时间'].shift(-1*(i+1))
            gdf['delta'] = gdf['shift_time'] - gdf['交易时间']
            gdf['delta']=gdf['delta'].astype(str).apply(lambda x: x.split(' ')[0])
            gdf['next_range'] = i+1
            gdf = gdf.reset_index()
            gdf = gdf.reset_index()
            gdf1 = gdf[['index','next_range','会员卡号','交易时间','店铺名称','消费金额','shift_shop','delta']].dropna()
            gdf1['delta']=gdf1['delta'].astype(int)
            dffli.append(gdf1)
        ansdf = pd.concat(dffli).reset_index(drop=True)
        self. ansdf = ansdf
        
#查看任意两家的流量转移组成
    def prepare(self):
        userdf = pd.read_csv('../data/users.csv')
        userdf=userdf.dropna()
        userdf['性别']=userdf['性别'].apply(lambda x: 1 if x=="M" else 2 if x=="F" else 0)

        userdf['年龄']=userdf['年龄'].apply(lambda x: 0 if x==-1 else x)

        userdf['会员卡级别']=userdf['会员卡级别'].apply(lambda x: 1 if x=="预享卡" else 2 if x=="缤纷卡" else 3 if x=="璀璨卡" else 4)

        userdmerge = userdf[['会员卡号','性别','年龄','会员卡级别']]
        dff=self.ansdf
        dff['num'] = 1
        dff_m = pd.merge(dff,userdmerge,how='inner',on ='会员卡号' )
        self.dff_m =dff_m
        
        dff_m = self.dff_m
        
        dffgroup = dff_m.groupby(['店铺名称','shift_shop'],as_index = False)['num','delta','消费金额','性别','年龄','会员卡级别'].sum()
        sumdf = dffgroup.groupby(['店铺名称'],as_index = False)['num','delta','消费金额','性别','年龄','会员卡级别'].sum()
        sumdf.columns = ['店铺名称','sum_num','sum_delta','sum_消费金额','sum_性别','sum_年龄','sum_会员卡级别']
        mergedf = pd.merge(dffgroup,sumdf,how='inner',on = '店铺名称')
        mergedf['num_rate'] = mergedf['num'] /mergedf['sum_num'] 
        mergedf['delta_rate'] = mergedf['delta'] /mergedf['sum_delta'] 
        mergedf['消费金额_rate'] = mergedf['消费金额'] /mergedf['num'] 

        mergedf['性别_rate'] = mergedf['性别'] /mergedf['num'] 
        mergedf['年龄_rate'] = mergedf['年龄'] /mergedf['num'] 
        self.mergedf=mergedf
        
        emat = np.load('../data/w2v_mat_shop.npy')
        key = np.load('../data/pros_1__shop_key.npy')



        def distance(array1,attay2):
            return np.sum((array1-attay2)**2)


        w2idic = {j:i for i,j in enumerate(key)}

        lsiaa = []
        for i in key:
            for j in key:
                ans = distance(emat[w2idic[i]],emat[w2idic[j]])

                lsiaa.append([i,j,ans])

        cordf = pd.DataFrame(lsiaa)

        cordf.columns = ['店铺名称','shift_shop','corr']
        mm = max(cordf['corr'])
        cordf['corr']=cordf['corr']/mm
        cordf['corr']=1 - cordf['corr']
        corrdf = pd.merge(mergedf,cordf,how ='inner',on = ['shift_shop','店铺名称'])
        self.corrdf=corrdf
        
    def cheack_trans_flow(self,s1,s2=''):
        if s2 =='':
            look_up_table = DPS.dff_m[(DPS.dff_m['店铺名称'] ==s1)]
        else:
            look_up_table = self.dff_m[(self.dff_m['店铺名称'] ==s1) & (self.dff_m['shift_shop'] ==s2)]
        
        plt.figure(figsize = (10,14))
        ax1 = plt.subplot(321)
        look_up_table.groupby(['会员卡级别'],as_index = True )['num'].count().plot.bar()
        ax1.set_title('会员卡等级分布',fontproperties=my_font)
        ax1.set_xlabel('会员等级',fontproperties=my_font)



        ax2 = plt.subplot(322)
        look_up_table.groupby(['性别'],as_index = True )['num'].count().plot.bar()
        ax2.set_title('性别分布：1为男性',fontproperties=my_font)
        ax2.set_xlabel('性别',fontproperties=my_font)

        ax3 = plt.subplot(312)
        #look_up_table.groupby(['delta'],as_index = True )['num'].count().hist()
        plt.hist(look_up_table['delta'],bins=50)
        ax3.set_title('交易间隔分布',fontproperties=my_font)
        ax3.set_xlabel('交易间隔',fontproperties=my_font)

        ax4 = plt.subplot(325)
        #look_up_table.groupby(['年龄'],as_index = True )['num'].count().plot.bar()
        plt.hist(look_up_table['年龄'],bins=20)
        ax4.set_title('年龄分布',fontproperties=my_font)
        ax4.set_xlabel('年龄分布',fontproperties=my_font)

        ax5 = plt.subplot(326)
        #look_up_table.groupby(['消费金额'],as_index = True )['num'].count().hist()
        plt.hist(look_up_table['消费金额'],bins=20)
        ax5.set_title('消费金额分布',fontproperties=my_font)
        ax5.set_xlabel('消费金额',fontproperties=my_font)
        self.corrdf['rank'] = self.corrdf['corr']*self.corrdf['num_rate']
    def predict_one(self,shopname):
        self.corrdf['rank'] = self.corrdf['corr']*self.corrdf['num_rate']
        anslist = list(self.corrdf[self.corrdf['店铺名称'] == shopname].sort_values(by = 'corr',ascending = False).head(6)['shift_shop'][1:])
        return anslist
    
    def plot_mat_come(self,shopname):
        scatterdf = self.corrdf[self.corrdf['shift_shop']== shopname][['shift_shop','店铺名称','corr','num_rate']]
        scatterdf=scatterdf.reset_index(drop = True)
        scatterdf['d_'] = scatterdf['corr']**2 *scatterdf['num_rate']
        scatterdf = scatterdf.sort_values(by = 'd_',ascending = False)
        
        fig, ax = plt.subplots(figsize=(5,5))
        for idx in range(0,len(scatterdf.index)):
            plt.scatter(scatterdf['corr'][idx],scatterdf['num_rate'][idx] ,color='steelblue')
            plt.annotate(scatterdf['店铺名称'][idx], (scatterdf['corr'][idx],scatterdf['num_rate'][idx]), alpha=0.7,fontproperties=my_font)
            
    def plot_mat_out(self,shopname):
        scatterdf = self.corrdf[self.corrdf['店铺名称']== shopname][['shift_shop','店铺名称','corr','num_rate']]
        scatterdf=scatterdf.reset_index(drop = True)
        scatterdf['d_'] = scatterdf['corr']**2 *scatterdf['num_rate']
        scatterdf = scatterdf.sort_values(by = 'd_',ascending = False)
        
        fig, ax = plt.subplots(figsize=(5,5))
        for idx in range(0,len(scatterdf.index)):
            plt.scatter(scatterdf['corr'][idx],scatterdf['num_rate'][idx] ,color='steelblue')
            plt.annotate(scatterdf['shift_shop'][idx], (scatterdf['corr'][idx],scatterdf['num_rate'][idx]), alpha=0.7,fontproperties=my_font)
            
        