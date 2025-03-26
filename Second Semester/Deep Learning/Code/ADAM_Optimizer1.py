import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Network architecture
input_neurons = 2
hidden_neurons_1 = 2
hidden_neurons_2 = 2
output_neurons = 1
alpha = 0.01  # Learning rate
epochs = 10000

# Initialize weights and biases
np.random.seed(42)
W1 = np.random.randn(input_neurons, hidden_neurons_1)
b1 = np.zeros((1, hidden_neurons_1))
W2 = np.random.randn(hidden_neurons_1, hidden_neurons_2)
b2 = np.zeros((1, hidden_neurons_2))
W3 = np.random.randn(hidden_neurons_2, output_neurons)
b3 = np.zeros((1, output_neurons))

# Adam parameters
m_W1, v_W1 = np.zeros_like(W1), np.zeros_like(W1)
m_W2, v_W2 = np.zeros_like(W2), np.zeros_like(W2)
m_W3, v_W3 = np.zeros_like(W3), np.zeros_like(W3)
m_b1, v_b1 = np.zeros_like(b1), np.zeros_like(b1)
m_b2, v_b2 = np.zeros_like(b2), np.zeros_like(b2)
m_b3, v_b3 = np.zeros_like(b3), np.zeros_like(b3)
beta1, beta2 = 0.9, 0.999
epsilon = 1e-8

# Training loop
for epoch in range(epochs):
    # Forward propagation
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    Z3 = np.dot(A2, W3) + b3
    y_pred = sigmoid(Z3)

    # Compute loss (Binary Cross Entropy)
    loss = -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

    # Backpropagation
    dZ3 = y_pred - y
    dW3 = np.dot(A2.T, dZ3) / X.shape[0]
    db3 = np.sum(dZ3, axis=0, keepdims=True) / X.shape[0]

    dA2 = np.dot(dZ3, W3.T)
    dZ2 = dA2 * sigmoid_derivative(A2)
    dW2 = np.dot(A1.T, dZ2) / X.shape[0]
    db2 = np.sum(dZ2, axis=0, keepdims=True) / X.shape[0]

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * sigmoid_derivative(A1)
    dW1 = np.dot(X.T, dZ1) / X.shape[0]
    db1 = np.sum(dZ1, axis=0, keepdims=True) / X.shape[0]

    # Adam optimizer update
    for param, dparam, m, v in zip(
        [W1, W2, W3, b1, b2, b3],
        [dW1, dW2, dW3, db1, db2, db3],
        [m_W1, m_W2, m_W3, m_b1, m_b2, m_b3],
        [v_W1, v_W2, v_W3, v_b1, v_b2, v_b3]
    ):
        m[:] = beta1 * m + (1 - beta1) * dparam
        v[:] = beta2 * v + (1 - beta2) * (dparam ** 2)
        m_hat = m / (1 - beta1 ** (epoch + 1))
        v_hat = v / (1 - beta2 ** (epoch + 1))
        param -= alpha * m_hat / (np.sqrt(v_hat) + epsilon)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Testing
print("\nPredictions:")
for i in range(4):
    print(f"Input: {X[i]} -> Predicted Output: {y_pred[i][0]:.4f}")
