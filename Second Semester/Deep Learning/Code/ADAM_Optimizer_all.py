import numpy as np
import matplotlib.pyplot as plt

# Activation function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Loss function (Mean Squared Error)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Initialize parameters
np.random.seed(0)
input_size = 2
hidden_size = 2
output_size = 1
optimizers = ["sgd", "adam", "rmsprop", "adagrad", "adadelta", "nadam", "ftrl", "amsgrad"]
loss_histories = {}

for optimizer in optimizers:
    W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.uniform(-1, 1, (hidden_size, hidden_size))
    b2 = np.zeros((1, hidden_size))
    W3 = np.random.uniform(-1, 1, (hidden_size, output_size))
    b3 = np.zeros((1, output_size))

    # Learning rate and parameters
    lr = 0.1
    beta1, beta2, epsilon = 0.9, 0.999, 1e-8
    rho = 0.95
    lambda_ftrl = 0.1
    v_W1, v_W2, v_W3 = np.zeros_like(W1), np.zeros_like(W2), np.zeros_like(W3)
    v_b1, v_b2, v_b3 = np.zeros_like(b1), np.zeros_like(b2), np.zeros_like(b3)
    m_W1, m_W2, m_W3 = np.zeros_like(W1), np.zeros_like(W2), np.zeros_like(W3)
    m_b1, m_b2, m_b3 = np.zeros_like(b1), np.zeros_like(b2), np.zeros_like(b3)

    epochs = 10000
    loss_history = []

    for epoch in range(1, epochs + 1):
        hidden1 = sigmoid(np.dot(X, W1) + b1)
        hidden2 = sigmoid(np.dot(hidden1, W2) + b2)
        output = sigmoid(np.dot(hidden2, W3) + b3)

        loss = mse(y, output)
        loss_history.append(loss)

        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)
        hidden2_error = output_delta.dot(W3.T)
        hidden2_delta = hidden2_error * sigmoid_derivative(hidden2)
        hidden1_error = hidden2_delta.dot(W2.T)
        hidden1_delta = hidden1_error * sigmoid_derivative(hidden1)

        dW3 = hidden2.T.dot(output_delta)
        db3 = np.sum(output_delta, axis=0, keepdims=True)
        dW2 = hidden1.T.dot(hidden2_delta)
        db2 = np.sum(hidden2_delta, axis=0, keepdims=True)
        dW1 = X.T.dot(hidden1_delta)
        db1 = np.sum(hidden1_delta, axis=0, keepdims=True)

        if optimizer == "sgd":
            W1 += lr * dW1
            W2 += lr * dW2
            W3 += lr * dW3
            b1 += lr * db1
            b2 += lr * db2
            b3 += lr * db3
        elif optimizer == "amsgrad":
            v_W1 = np.maximum(beta2 * v_W1, dW1 ** 2)
            W1 += lr * dW1 / (np.sqrt(v_W1) + epsilon)
            v_W2 = np.maximum(beta2 * v_W2, dW2 ** 2)
            W2 += lr * dW2 / (np.sqrt(v_W2) + epsilon)
            v_W3 = np.maximum(beta2 * v_W3, dW3 ** 2)
            W3 += lr * dW3 / (np.sqrt(v_W3) + epsilon)
        elif optimizer == "ftrl":
            W1 += -lr * dW1 / (lambda_ftrl + np.abs(dW1))
            W2 += -lr * dW2 / (lambda_ftrl + np.abs(dW2))
            W3 += -lr * dW3 / (lambda_ftrl + np.abs(dW3))
            b1 += -lr * db1 / (lambda_ftrl + np.abs(db1))
            b2 += -lr * db2 / (lambda_ftrl + np.abs(db2))
            b3 += -lr * db3 / (lambda_ftrl + np.abs(db3))

        if epoch % 1000 == 0:
            print(f'Optimizer: {optimizer}, Epoch {epoch}, Loss: {loss}')

    loss_histories[optimizer] = loss_history

# Plot convergence graph
plt.figure(figsize=(10, 6))
for optimizer, loss_history in loss_histories.items():
    plt.plot(loss_history, label=optimizer)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Convergence of Different Optimizers')
plt.legend()
plt.show()

# Testing
print("Final Output:")
print(output)
