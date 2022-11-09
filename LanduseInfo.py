#coding=utf-8

# 统计土地利用相关的信息

import arcpy
import arcpy             # 导入 arcpy 模块用于影像处理
import numpy as np       # 导入 numpy 模块用于后续数据的统计处理
import matplotlib.pyplot as plt # 导入 matplotlib模块用于绘图
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#file_path = 'W:\\数据\\湖北省植被覆盖度研究\\各类FVC\\'     # 定义数据保存的文件夹地址
file_path = 'H:\\Python\\Data\\'

# 定义所要处理的图像文件
files = ['2000年草地FVC.tif', '2020年草地FVC.tif']  # 草地

# 将所需要的数据从影像文件保存到 data
data = []

for f in files:                  # 每次取出 files 列表中的一个元素 （文件名）
    fpath = file_path + f        # 组成带路径的文件名
    ras = arcpy.Raster(fpath)    # 将这个元素对应的影像文件读取到程序变量 ras 中
    arr = arcpy.RasterToNumPyArray(ras)  # 将 ras 变量所表示的影像数据转为二维矩阵
    lst =[i for item in arr for i in item]       # 将二维矩阵 arr 转换成一维向量
    vmin = -1
    vmax = 1
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):
            tmplst.append(value)
    data.append(tmplst)

    # 统计各个图的特征值
    print(f + ':')
    print('最大值 = ', np.max(tmplst))
    print('最小值 = ', np.min(tmplst))
    print('平均值 = ', np.mean(tmplst))
    print('标准差 = ', np.std(tmplst))
    print('变异系数 = ', np.std(tmplst) / np.mean(tmplst))
    print('5% 分位数 = ', np.percentile(tmplst, 5))
    print('25% 分位数 = ', np.percentile(tmplst, 25))
    print('50% 分位数 = ', np.percentile(tmplst, 50))
    print('75% 分位数 = ', np.percentile(tmplst, 75))
    print('95% 分位数 = ', np.percentile(tmplst, 95))
    print('像素个数', len(tmplst))
    print('\n')

# 根据 data 所保存的数据进行绘图
plt.boxplot(data,patch_artist=True,boxprops={'facecolor':'b','alpha':0.2})          # 画分位数的箱线图
plt.xticks([1,2], ['2000年','2020年'], fontsize=16) # 设置 x 轴标签及字体
plt.yticks(fontsize=16)    # 设置 y 轴字体大小
plt.ylabel("草地植被覆盖度",fontsize=20)
plt.show()







