import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import MiniBatchKMeans, HDBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.preprocessing import StandardScaler



def generate_datasets():
    datasets = []

    X, _ = make_circles(n_samples=300, factor=0.8, noise=0.03)
    datasets.append(StandardScaler().fit_transform(X))


    X, _ = make_moons(n_samples=300, noise=0.05)
    datasets.append(StandardScaler().fit_transform(X))


    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.5)
    datasets.append(StandardScaler().fit_transform(X))


    X, _ = make_blobs(n_samples=300, centers=3, random_state=52)
    transformation = [[0.6, -0.6], [-0.4, 0.8]]
    datasets.append(StandardScaler().fit_transform(np.dot(X, transformation)))


    X, _ = make_blobs(n_samples=300, centers=3, cluster_std=[1.0, 2.2, 0.5])
    datasets.append(StandardScaler().fit_transform(X))

    return datasets


datasets = generate_datasets()
names = ['Circles', 'Moons', 'Isotropic', 'Anisotropic', 'Different Variance']


methods = [
    ("MiniBatchKMeans", MiniBatchKMeans(n_clusters=3, random_state=50)),
    ("HDBSCAN", HDBSCAN(min_cluster_size=15)),
    ("Gaussian Mixture", GaussianMixture(n_components=3, random_state=42))
]


fig, axes = plt.subplots(len(datasets), len(methods), figsize=(18, 25))
plt.subplots_adjust(hspace=0.3, wspace=0.05)


for col, (name, _) in enumerate(methods):
    axes[0, col].set_title(name, fontsize=28, pad=20)


for row, name in enumerate(names):
    axes[row, 0].set_ylabel(name, rotation=0, fontsize=26, labelpad=40)


for row, X in enumerate(datasets):
    for col, (method_name, model) in enumerate(methods):
        ax = axes[row, col]


        if method_name == "Gaussian Mixture":
            labels = model.fit(X).predict(X)
        else:
            labels = model.fit_predict(X)


        ax.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab20', s=80, edgecolor='k', lw=0.3)
        ax.set_xticks([])
        ax.set_yticks([])

plt.suptitle("Сравнение алгоритмов кластеризации на разных типах данных", y=0.99, fontsize=16)
plt.show()