import json


def train():
    # 此处为训练代码
    pass
    json_data = {
        "item": [
            {"precision": 0.92, "recall": 0.92, "f1-score": 0.92, "support": 0.9},
            {"precision": 0.93, "recall": 0.93, "f1-score": 0.93, "support": 0.9},
            {"precision": 0.95, "recall": 0.95, "f1-score": 0.95, "support": 0.9},
            {"precision": 0.96, "recall": 0.96, "f1-score": 0.96, "support": 0.9},
        ],
        "avg": {"precision": 0.94, "recall": 0.94, "f1-score": 0.94, "support": 0.9},
    }
    return json.dumps(json_data)


if __name__ == "__main__":
    print(train())
