import pickle
import pandas as pd
import json


def compute_mean_of_feature(data):
    """计算数据中每个特征列的`mean value`

    Parameters:
    - data: Pandas加载数据后的DataFrame

    Returns:
      - features_m_value: 计算每个feature的meam value的列表
    """
    data.fillna(0, inplace=True)
    features_m_value = list()
    for idx in range(len(data.columns) - 1):
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


def preprocess(input_file_path):
    data = pd.read_csv(input_file_path)
    features_m_value = compute_mean_of_feature(data.copy())
    print(f'Features Mean Value: {features_m_value}')
    data = fill_mean_value(data, features_m_value)
    return data


def predict(input_file_path, task_id):
    dataset = preprocess(input_file_path)
    X_test = dataset.iloc[:, 1:].values

    with open('fault_diagnosis_ml/modles/voting_clf_model.pkl', 'rb') as file:
        voting_clf = pickle.load(file)

    # 预测并生成标签
    y_pred = voting_clf.predict(X_test)

    # 假设 y_pred 是一个包含预测值的 NumPy 数组或列表
    y_pred_list = y_pred.tolist()  # 将 NumPy 数组转换为 Python 列表

    # 创建一个空字典来存储预测结果
    predictions = {}

    # 遍历预测值列表
    for value in y_pred_list:
        next_index = len(predictions) + 1  # 计算下一个数字对应的字典值
        predictions[next_index] = value

    # 将字典转换为 JSON 格式
    json_data = json.dumps(predictions)

    # 将 JSON 数据写入文件
    with open(f'fault_diagnosis_ml/json/{task_id}.json', 'w') as f:
        f.write(json_data)
    # return y_pred
    return json_data


if __name__ == '__main__':
    file_path = 'fault_diagnosis_ml/test/test_2000_x.csv'  # 'test/test_2000_x.csv'
    report = predict(file_path, 2)
    print(report)
