import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)  # derivative of sigmoid

# XOR dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

Y = np.array([[0], [1], [1], [0]])  # Expected output

# Initialize weights and biases
np.random.seed(42)
input_size = 2
hidden_size = 3
output_size = 1

W1 = np.random.randn(input_size, hidden_size)  # Weights for input to hidden layer 1
b1 = np.random.randn(hidden_size)              # Bias for hidden layer 1

W2 = np.random.randn(hidden_size, hidden_size) # Weights for hidden layer 1 to hidden layer 2
b2 = np.random.randn(hidden_size)              # Bias for hidden layer 2

W3 = np.random.randn(hidden_size, output_size) # Weights for hidden layer 2 to output
b3 = np.random.randn(output_size)              # Bias for output layer

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training loop
for epoch in range(epochs):
    # Forward pass
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    Z3 = np.dot(A2, W3) + b3
    A3 = sigmoid(Z3)  # Final output

    # Compute loss (mean squared error)
    loss = np.mean((Y - A3) ** 2)

    # Backpropagation
    dA3 = 2 * (A3 - Y) / Y.size * sigmoid_derivative(A3)  # Gradient for output layer
    dW3 = np.dot(A2.T, dA3)
    db3 = np.sum(dA3, axis=0)

    dA2 = np.dot(dA3, W3.T) * sigmoid_derivative(A2)
    dW2 = np.dot(A1.T, dA2)
    db2 = np.sum(dA2, axis=0)

    dA1 = np.dot(dA2, W2.T) * sigmoid_derivative(A1)
    dW1 = np.dot(X.T, dA1)
    db1 = np.sum(dA1, axis=0)

    # Update weights and biases
    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Print loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Test the trained model
print("\nFinal Output:")
print(A3)
