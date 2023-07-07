import pandas as pd

def compute_mean_of_feature(data):
  """计算数据中每个特征列的`mean value`

  Parameters:
  - data: Pandas加载数据后的DataFrame

  Returns:
    - features_m_value: 计算每个feature的meam value的列表
  """
  data.fillna(0, inplace=True)
  features_m_value = list()
  for idx in range(len(data.columns) - 2):
    feature_mean_value = data['feature{}'.format(idx)].mean()
    features_m_value.append(feature_mean_value)
  return features_m_value


def fill_mean_value(data, features_m_value):
  """根据`mean value` 填充替换原生数据集中的缺失值

  Parameters:
    - data: Pandas加载数后的DataFrame
    - features_m_values: `data`中每个特征的`mean value`
  Returns:
    - data: 返回替换后的数据
  """
  for idx, mean_value in zip(range(len(features_m_value)), features_m_value):
    data['feature{}'.format(idx)].fillna(mean_value, inplace=True)
  return data


def preprocess(file_path):
  data = pd.read_csv(file_path)
  features_m_value = compute_mean_of_feature(data.copy())
  print(f'Features Mean Value: {features_m_value}')
  data = fill_mean_value(data, features_m_value)
  return data


if __name__ == '__main__':
  file_path = 'train/train_10000.csv'
  dataset = preprocess(file_path)
  print(dataset)
  
