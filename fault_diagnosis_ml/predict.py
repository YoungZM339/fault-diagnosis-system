import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from fault_diagnosis_ml.preprocessing import preprocess
import pickle


def predict(file_path):
    dataset = preprocess(file_path)
    X_test = dataset.iloc[:, 1:-1].values
    y_test = dataset.iloc[:, -1].values

    with open('fault_diagnosis_ml/modles/voting_clf_model.pkl', 'rb') as file:
        voting_clf = pickle.load(file)

    # 预测并生成分类报告
    y_pred = voting_clf.predict(X_test)
    labels = ['0', '1', '2', '3', '4', '5']
    report = classification_report(y_test, y_pred, target_names=labels)
    return report


if __name__ == '__main__':
    file_path = 'fault_diagnosis_ml/val/validate_1000.csv'  # 'test/test_2000_x.csv'
    report = predict(file_path)
    print(report)
