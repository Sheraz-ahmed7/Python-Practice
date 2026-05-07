from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# 2. Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# MODEL A: WITHOUT SCALING
# -------------------------------
model_a = LogisticRegression(max_iter=10000)
model_a.fit(X_train, y_train)

y_pred_a = model_a.predict(X_test)

print("MODEL A (Without Scaling)")
print("Accuracy:", accuracy_score(y_test, y_pred_a))
print(classification_report(y_test, y_pred_a))

# -------------------------------
# MODEL B: WITH SCALING
# -------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model_b = LogisticRegression(max_iter=10000)
model_b.fit(X_train_scaled, y_train)

y_pred_b = model_b.predict(X_test_scaled)

print("\nMODEL B (With Scaling)")
print("Accuracy:", accuracy_score(y_test, y_pred_b))
print(classification_report(y_test, y_pred_b))