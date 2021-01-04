"""数据抽取"""
import pandas as pd

# 读取excel文件中的数据
df_2018 = pd.read_excel('data/2018.xlsx')
df_2019 = pd.read_excel('data/2019.xlsx')

# 抽取指定列数据
df_2018 = df_2018[['买家会员名', '买家实际支付金额', '订单付款时间']]
df_2019 = df_2019[['买家会员名', '买家实际支付金额', '订单付款时间']]

"""
 由于两年的数据分别存储在不同的Excel文件中，所以首先对数据进行合并，然后从数据中抽取与客户价值分析相关的数据。
"""
# 数据合并与导出
dfs = pd.concat([df_2018, df_2019])  # 使用concat函数进行连接两个提取出来的数据
print(dfs.head())                    # 输出部分数据，默认输出前五行数据
dfs.to_excel('all.xlsx', index=False)  # 输出到Excel文件中，不显示index（索引）值
