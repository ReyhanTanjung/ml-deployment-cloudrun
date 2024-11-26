import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
