import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np 
import matplotlib
from matplotlib import font_manager
my_font =  {'family' : 'MicroSoft YaHei',  'weight' : 'bold', 'size'   : 'larger'}
matplotlib.rc("font",)
my_font = font_manager.FontProperties(fname="font/simhei.ttf")

def plot_data (types,limit = 1000 ):
    if types == 'shop':
        mat = np.load('data/w2v_mat_shop.npy')
        workey=np.load('data/pros_1__shop_key.npy',allow_pickle=True)
        workey = list(set(workey))
        int_to_vocab = {j:i for i,j in zip(workey,range(len(workey)))}
        word2int = {int_to_vocab[i]:i for i in int_to_vocab}
    elif types == 'cus':
        mat = np.load('data/w2v_mat_cus.npy')
        workey=np.load('data/pros_1__cus_key.npy',allow_pickle=True)
        workey = list(set(workey))
        int_to_vocab = {j:i for i,j in zip(workey,range(len(workey)))}
        word2int = {int_to_vocab[i]:i for i in int_to_vocab}                
    if mat.shape[1]>2:
        tsne = TSNE()
        embed_tsne = tsne.fit_transform(mat[:limit, :])
        #int_to_vocab = 
        fig, ax = plt.subplots(figsize=(14, 14))
        for idx in range(limit):
            plt.scatter(*embed_tsne[idx, :], color='steelblue')
            plt.annotate(int_to_vocab[idx], (embed_tsne[idx, 0], embed_tsne[idx, 1]), alpha=0.7,fontproperties=my_font)
    else:
        fig, ax = plt.subplots(figsize=(14, 14))
        for idx in range(limit):
            plt.scatter(*mat[idx, :], color='steelblue')
            plt.annotate(int_to_vocab[idx], (mat[idx, 0], mat[idx, 1]), alpha=0.7,fontproperties=my_font)