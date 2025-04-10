

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成多类单标签数据集
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60)

# 可视化数据集
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Blobs Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()