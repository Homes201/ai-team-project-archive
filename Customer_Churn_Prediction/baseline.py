"""Reproducible churn baseline; fit preprocessing only on training data."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, precision_recall_fscore_support, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parent
TARGET = "Churn"


def run():
    train = pd.read_csv(ROOT / "data" / "train.csv")
    columns = [column for column in train if column not in (TARGET, "CustomerID")]
    labels = train[TARGET].eq("Yes")
    x_train, x_valid, y_train, y_valid = train_test_split(
        train[columns], labels, test_size=0.2, random_state=42, stratify=labels,
    )
    numeric = x_train.select_dtypes(include="number").columns.tolist()
    categorical = [column for column in columns if column not in numeric]
    preprocess = ColumnTransformer([
        ("number", Pipeline([
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
        ]), numeric),
        ("category", Pipeline([
            ("impute", SimpleImputer(strategy="most_frequent")),
            ("encode", OneHotEncoder(handle_unknown="ignore", min_frequency=10)),
        ]), categorical),
    ])
    model = Pipeline([
        ("preprocess", preprocess),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", solver="liblinear")),
    ])
    model.fit(x_train, y_train)
    probability = model.predict_proba(x_valid)[:, 1]
    prediction = probability >= 0.5
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_valid, prediction, average="binary", zero_division=0,
    )
    print(f"train={len(x_train)} validation={len(x_valid)} positive_rate={y_valid.mean():.3f}")
    print(f"precision={precision:.3f} recall={recall:.3f} f1={f1:.3f}")
    print(f"average_precision={average_precision_score(y_valid, probability):.3f} "
          f"roc_auc={roc_auc_score(y_valid, probability):.3f}")
    print("The supplied test.csv has no labels; no test score is claimed.")
    print("Threshold 0.5 is a baseline; choose an operating point on separate validation data.")


if __name__ == "__main__":
    run()
