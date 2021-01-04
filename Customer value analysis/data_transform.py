"""
  数据转换
  它是将数据转换成适当的格式，以适应数据分析和数据挖掘算法的需要。这里是将RFM模型的数据进行标准化处理。
"""
import pandas as pd

data = pd.read_excel('RFM.xlsx')  # 读取Excel文件
data = data[['最近消费时间间隔', '消费频率', '消费金额']]  # 提取指定列数据
data = (data - data.mean(axis=0)) / (data.std(axis=0))  # 标准化处理
data.columns = ['R', 'F', 'M']  # 表头重命名
print(data.head())  # 输出部分数据
data.to_excel('transformdata.xlsx', index=False)  # 导出数据
