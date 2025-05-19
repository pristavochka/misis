import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import confusion_matrix, adjusted_rand_score
from scipy.spatial import Delaunay
from sklearn.cluster import AffinityPropagation, MeanShift
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GridSearchCV
from sklearn.base import clone

os.environ["LOKY_MAX_CPU_COUNT"] = "4"

def generate_triangle_clusters(n_samples=1000, overlap=0.05, random_state=42):
    vertices = np.array([[0, 0], [2, 0], [1, np.sqrt(3)]])
    centers = vertices * 0.9 + np.array([0.1, 0.1])
    cluster_std = 0.21 + overlap * 2.5

    X, y = make_blobs(n_samples=n_samples,
                      centers=centers,
                      cluster_std=cluster_std,
                      random_state=random_state)

    tri = Delaunay(vertices)
    mask = tri.find_simplex(X) >= 0
    X, y = X[mask], y[mask]

    return X, y

def calculate_overlap(X, y):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import cross_val_predict
    clf = KNeighborsClassifier(n_neighbors=3)
    pred = cross_val_predict(clf, X, y, cv=5)
    cm = confusion_matrix(y, pred)
    np.fill_diagonal(cm, 0)
    return cm.sum() / len(y)


X, y = generate_triangle_clusters(overlap=0.05)

param_grids = {
    'AffinityPropagation': {
        'damping': [0.7, 0.75, 0.8],
        'preference': [-1, -0.5, -0.1],
        'max_iter': [500, 1000]
    },
    'MeanShift': {
        'bandwidth': [0.8, 1.0, 1.2]
    },
    'GaussianMixture': {
        'covariance_type': ['full', 'tied', 'diag']
    }
}

best_params = {}

def cluster_scorer(estimator, X, y_true):
    if hasattr(estimator, 'fit_predict'):
        y_pred = estimator.fit_predict(X)
    else:
        y_pred = estimator.fit(X).predict(X)
    return adjusted_rand_score(y_true, y_pred)

ap = AffinityPropagation(random_state=50)
gscv = GridSearchCV(ap, param_grids['AffinityPropagation'], scoring=cluster_scorer)
gscv.fit(X, y)
best_params['AffinityPropagation'] = gscv.best_params_

ms = MeanShift(bin_seeding=True)
gscv = GridSearchCV(ms, param_grids['MeanShift'], scoring=cluster_scorer)
gscv.fit(X, y)
best_params['MeanShift'] = gscv.best_params_

gmm = GaussianMixture(n_components=3, random_state=42)
gscv = GridSearchCV(gmm, param_grids['GaussianMixture'], scoring=cluster_scorer)
gscv.fit(X, y)
best_params['GaussianMixture'] = gscv.best_params_

methods = [
    ('AffinityPropagation', AffinityPropagation(**best_params['AffinityPropagation'], random_state=50)),
    ('MeanShift', MeanShift(**best_params['MeanShift'], bin_seeding=True)),
    ('GaussianMixture', GaussianMixture(n_components=3, **best_params['GaussianMixture'], random_state=42))
]

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
plt.subplots_adjust(bottom=0.25)

ap = AffinityPropagation(damping=0.7, preference=-0.5, max_iter=1, random_state=50)
ms = MeanShift(bandwidth=1.0, bin_seeding=True)
gm = GaussianMixture(n_components=3, max_iter=1, warm_start=True, random_state=42)

ap_history = []
ms_history = []

for i in range(20):
    ap.max_iter = i + 1
    ap.fit(X)
    ap_history.append(ap.labels_)

    if i == 0:
        ms.fit(X)
    ms_history.append(ms.labels_)

    gm.fit(X)


def get_gm_iteration(iter_num):
    gm_temp = GaussianMixture(n_components=3, max_iter=iter_num, random_state=42)
    gm_temp.fit(X)
    return gm_temp.predict(X)

sc1 = ax1.scatter(X[:, 0], X[:, 1], c=ap_history[0], cmap='viridis', s=10)
ax1.set_title('Affinity Propagation (iter 1)')
sc2 = ax2.scatter(X[:, 0], X[:, 1], c=ms_history[0], cmap='viridis', s=10)
ax2.set_title('MeanShift (iter 1)')
sc3 = ax3.scatter(X[:, 0], X[:, 1], c=get_gm_iteration(1), cmap='viridis', s=10)
ax3.set_title('Gaussian Mixture (iter 1)')

ax_slider1 = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_slider2 = plt.axes([0.25, 0.10, 0.65, 0.03])
ax_slider3 = plt.axes([0.25, 0.05, 0.65, 0.03])

slider1 = Slider(ax_slider1, 'AP Iter', 1, 20, valinit=1, valstep=1)
slider2 = Slider(ax_slider2, 'MS Iter', 1, 20, valinit=1, valstep=1)
slider3 = Slider(ax_slider3, 'GMM Iter', 1, 20, valinit=1, valstep=1)

def update1(val):
    iter_num = int(slider1.val) - 1
    sc1.set_array(ap_history[iter_num])
    ax1.set_title(f'Affinity Propagation (iter {iter_num + 1})')
    fig.canvas.draw_idle()


def update2(val):
    iter_num = int(slider2.val) - 1
    sc2.set_array(ms_history[iter_num])
    ax2.set_title(f'MeanShift (iter {iter_num + 1})')
    fig.canvas.draw_idle()


def update3(val):
    iter_num = int(slider3.val)
    sc3.set_array(get_gm_iteration(iter_num))
    ax3.set_title(f'Gaussian Mixture (iter {iter_num})')
    fig.canvas.draw_idle()

slider1.on_changed(update1)
slider2.on_changed(update2)
slider3.on_changed(update3)

plt.show()