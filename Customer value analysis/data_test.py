"""
  数据探索分析主要分析与客户价值RFM模型有关的数据是否存在数据缺失，数据异常的情况，从而分析出数据的规律。
  对数据进行基本的探索，返回缺失值个数以及最大和最小值
"""

import pandas as pd

data = pd.read_excel('all.xlsx')  # 读取data_concat输出的Excel文件

"""
   使用descrbe函数，该函数可自动计算字段非空值数（count）(空值数=数据总数-非空值数)
   运行出来后，“订单付款时间”中有637条空值记录，买家实际支付金额最小值为0，说明这些数据中的客户并没有
在店铺消费，属于无效数据，因此没有必要对这部分的客户进行分析。
"""
view = data.describe(percentiles=[], include='all').T  # 数据的基本描述
view['null'] = len(data) - view['count']  # describe()函数自动计算非空值数，需要手动计算空值数
view = view[['null', 'max', 'min']]
view.columns = [u'空值数', u'最大值', u'最小值']  # 表头重命名
print(view)  # 输出结果
view.to_excel('result.xlsx')  # 导出结果
