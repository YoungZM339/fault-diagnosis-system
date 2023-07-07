from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from fault_diagnosis_ml.preprocessing import preprocess
import pickle


def train(file_path, task_id):
    dataset = preprocess(file_path)
    X_train = dataset.iloc[:, 1:-1].values
    y_train = dataset.iloc[:, -1].values

    # 拆分训练集和测试集
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 定义三种不同类型的分类器
    dt_clf = DecisionTreeClassifier(random_state=45)
    rf_clf = RandomForestClassifier(random_state=45)
    et_clf = ExtraTreesClassifier(random_state=45)

    # 定义模型融合分类器
    voting_clf = VotingClassifier(estimators=[
        ('decision_tree', dt_clf),
        ('random_forest', rf_clf),
        ('extra_trees', et_clf)
    ])

    # 训练模型融合分类器
    voting_clf.fit(X_train, y_train)

    # 存储模型
    with open(f'fault_diagnosis_ml/modles/{task_id}.pkl', 'wb') as file:
        pickle.dump(voting_clf, file)

    return (dataset)


if __name__ == '__main__':
    file_path = 'fault_diagnosis_ml/train/train_10000.csv'
    print(train(file_path, 1))
