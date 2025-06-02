import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
X_circle, y_circle = datasets.make_circles(n_samples=500, factor=0.5, noise=0.05, random_state=30)
X_moon, y_moon = datasets.make_moons(n_samples=500, noise=0.05, random_state=30)
X_varied, y_varied = datasets.make_blobs(n_samples=500, cluster_std=[1.0, 0.5], random_state=30, centers=2)
X_aniso, y_aniso = datasets.make_blobs(n_samples=500, random_state=170, centers=2)
X_aniso = np.dot(X_aniso, [[0.6, -0.6], [-0.4, 0.8]])
X_blob, y_blob = datasets.make_blobs(n_samples=500, random_state=30, centers=2)
dataset_configs = [
    (X_circle, y_circle),
    (X_moon, y_moon),
    (X_varied, y_varied),
    (X_aniso, y_aniso),
    (X_blob, y_blob)
]
dataset_names = ['Circles', 'Moons', 'Varied Blobs', 'Anisotropic', 'Simple Blobs']
accuracies = np.zeros((5, 3))
classifiers = [
    MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=1000, random_state=42, early_stopping=True),
    GaussianNB(),
    SVC(kernel='rbf', C=1.0, gamma='auto')
]
classifier_names = ['MLP', 'Naive Bayes', 'SVM']
for row_idx, (X, y) in enumerate(dataset_configs):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    for col_idx, clf in enumerate(classifiers):
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracies[row_idx, col_idx] = accuracy_score(y_test, y_pred)
fig1, axes = plt.subplots(5, 3, figsize=(18, 25))
plt.subplots_adjust(wspace=0.3, hspace=0.4)
markers = ['x', 'o']
cmap = plt.cm.bwr
for row_idx, (X, y) in enumerate(dataset_configs):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    for col_idx, clf in enumerate(classifiers):
        ax = axes[row_idx, col_idx]
        clf.fit(X_train, y_train)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, alpha=0.2, cmap=cmap)
        for class_idx, marker in enumerate(markers):
            ax.scatter(X_train[y_train == class_idx, 0],
                      X_train[y_train == class_idx, 1],
                      marker=marker,
                      c='navy',
                      alpha=0.6,
                      edgecolor='none')
        y_pred = clf.predict(X_test)
        for i in range(len(X_test)):
            true_class = y_test[i]
            color = 'limegreen' if y_pred[i] == true_class else 'crimson'
            marker = markers[true_class]
            ax.scatter(
                X_test[i, 0],
                X_test[i, 1],
                marker=marker,
                c=color,
                s=60,
                edgecolor='black' if marker == 'o' else None,
                linewidth=0.5
            )
        if row_idx == 0:
            ax.set_title(classifier_names[col_idx], fontsize=12, pad=10)
        if col_idx == 0:
            ax.set_ylabel(dataset_names[row_idx], rotation=90, fontsize=12, labelpad=15)
plt.suptitle("Графики классификаций", fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
fig2 = plt.figure(figsize=(8, 4))
ax_table = fig2.add_subplot(111)
ax_table.axis('off')
table_data = [[f"{acc:.2f}" for acc in row] for row in accuracies]
tb = plt.table(cellText=table_data,
               rowLabels=dataset_names,
               colLabels=classifier_names,
               loc='center',
               cellLoc='center',
               bbox=[0, 0, 1, 1])
tb.auto_set_font_size(False)
tb.set_fontsize(12)
tb.scale(1.2, 1.2)
plt.suptitle("Таблица точности разных видов классификации", fontsize=14)
plt.tight_layout()
plt.show()
