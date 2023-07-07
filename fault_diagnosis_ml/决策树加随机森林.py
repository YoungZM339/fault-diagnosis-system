import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier


def preprocess(file_path):
    data = pd.read_csv(file_path)
    data.fillna(0, inplace=True)
    return data

if __name__ == '__main__':
    file_path_1 = 'train/train_10000.csv'#'val/validate_1000.csv'
    dataset1 = preprocess(file_path_1)
    file_path_2 = 'val/validate_1000.csv'  # 'val/validate_1000.csv'
    dataset2 = preprocess(file_path_2)

    X = dataset1.iloc[:, :-1].values
    y = dataset2.iloc[:, -1].values

    # 拆分训练集和测试集
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 定义三种不同类型的分类器
    dt_clf = DecisionTreeClassifier(random_state=42)
    rf_clf = RandomForestClassifier(random_state=42)
    et_clf = ExtraTreesClassifier(random_state=42)

    # 定义模型融合分类器
    voting_clf = VotingClassifier(estimators=[
        ('decision_tree', dt_clf),
        ('random_forest', rf_clf),
        ('extra_trees', et_clf)
    ])

    # 训练模型融合分类器
    voting_clf.fit(X_train, y_train)

    # 预测并生成分类报告
    y_pred = voting_clf.predict(X_test)
    labels = ['0', '1', '2', '3', '4', '5']
    report = classification_report(y_test, y_pred, target_names=labels)
    print(report)
