import numpy as np

# Activation and derivative functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Network architecture
input_size = 2
hidden_size = 2
output_size = 1

# Weight initialization
np.random.seed(42)
w1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
w2 = np.random.randn(hidden_size, hidden_size)
b2 = np.zeros((1, hidden_size))
w3 = np.random.randn(hidden_size, output_size)
b3 = np.zeros((1, output_size))

# ADAM parameters
alpha = 0.01  # Learning rate
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8
t = 0

# Moment estimates
m_w1, v_w1 = np.zeros_like(w1), np.zeros_like(w1)
m_b1, v_b1 = np.zeros_like(b1), np.zeros_like(b1)
m_w2, v_w2 = np.zeros_like(w2), np.zeros_like(w2)
m_b2, v_b2 = np.zeros_like(b2), np.zeros_like(b2)
m_w3, v_w3 = np.zeros_like(w3), np.zeros_like(w3)
m_b3, v_b3 = np.zeros_like(b3), np.zeros_like(b3)

# Training
epochs = 10000
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X, w1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, w2) + b2
    a2 = sigmoid(z2)

    z3 = np.dot(a2, w3) + b3
    y_pred = sigmoid(z3)

    # Loss (Mean Squared Error)
    loss = np.mean((y - y_pred) ** 2)

    # Backpropagation
    d_loss = (y_pred - y) * sigmoid_derivative(y_pred)
    d_w3 = np.dot(a2.T, d_loss)
    d_b3 = np.sum(d_loss, axis=0, keepdims=True)

    d_a2 = np.dot(d_loss, w3.T) * sigmoid_derivative(a2)
    d_w2 = np.dot(a1.T, d_a2)
    d_b2 = np.sum(d_a2, axis=0, keepdims=True)

    d_a1 = np.dot(d_a2, w2.T) * sigmoid_derivative(a1)
    d_w1 = np.dot(X.T, d_a1)
    d_b1 = np.sum(d_a1, axis=0, keepdims=True)

    # ADAM optimization
    t += 1
    for param, d_param, m, v in [(w1, d_w1, m_w1, v_w1), (b1, d_b1, m_b1, v_b1),
                                  (w2, d_w2, m_w2, v_w2), (b2, d_b2, m_b2, v_b2),
                                  (w3, d_w3, m_w3, v_w3), (b3, d_b3, m_b3, v_b3)]:
        m[:] = beta1 * m + (1 - beta1) * d_param
        v[:] = beta2 * v + (1 - beta2) * (d_param ** 2)
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        param -= alpha * m_hat / (np.sqrt(v_hat) + epsilon)

    # Print loss
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")

# Testing
print("Final Predictions:")
print(y_pred)
