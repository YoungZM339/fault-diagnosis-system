import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def preprocess(file_path):
    data = pd.read_csv(file_path)
    data.fillna(0, inplace=True)
    return data

if __name__ == '__main__':
    file_path = 'val/validate_1000.csv'
    dataset = preprocess(file_path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    # 拆分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 构建决策树模型
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X_train, y_train)

    y_pred = dt_model.predict(X_test)
    labels = ['0', '1', '2', '3', '4', '5']
    report = classification_report(y_test, y_pred, target_names=labels)

    # 构建随机森林模型
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # 预测并生成分类报告
    y_pred = rf_model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=labels)
    print(report)
