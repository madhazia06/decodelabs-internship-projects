from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
print("Features:", iris.feature_names)
print("Classes:", iris.target_names)
print("Number of samples:", len(iris.data))

print("\nFirst flower measurements:")
print(iris.data[0])

print("First flower class:")
print(iris.target[0])

print("First flower species:")
print(iris.target_names[iris.target[0]])

# Separate the flower measurements (X) and their correct classes (y)
X = iris.data
y = iris.target

# Split the dataset: 80% for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# Create a KNN classification model using 5 nearest neighbors
model = KNeighborsClassifier(n_neighbors=5)

# Train the model using the training data
model.fit(X_train, y_train)

print("\nModel training completed!")

# Predict the classes of the testing data
predictions = model.predict(X_test)

print("\nPredicted classes:")
print(predictions)

print("\nActual classes:")
print(y_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)
print("Model Accuracy Percentage:", accuracy * 100, "%")

# Display the confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Display precision, recall and F1-score
print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))

# Predict the species of a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

new_prediction = model.predict(new_flower)

predicted_species = iris.target_names[new_prediction[0]]

print("\nNew Flower Measurements:", new_flower[0])
print("Predicted Species:", predicted_species)