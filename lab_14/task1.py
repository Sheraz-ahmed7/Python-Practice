# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# 1. Generate non-linear synthetic data
np.random.seed(42)

# X values (input)
X = np.sort(5 * np.random.rand(80, 1), axis=0)

# y values (output) -> sin function + noise
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# 2. Create Decision Tree Regressor
# max_depth controls complexity (smaller = smoother)
model = DecisionTreeRegressor(max_depth=4)

# Train the model
model.fit(X, y)

# 3. Predict on new data
X_test = np.arange(0.0, 5.0, 0.01).reshape(-1, 1)
y_pred = model.predict(X_test)

# 4. Plot results
plt.scatter(X, y, color="orange", label="Original Data")
plt.plot(X_test, y_pred, color="blue", label="Prediction")

plt.title("Decision Tree Regression (Max Depth = 4)")
plt.xlabel("Input (X)")
plt.ylabel("Output (y)")
plt.legend()

plt.show()