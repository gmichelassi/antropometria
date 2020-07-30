from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from scipy.stats import randint
from scipy.stats import uniform


def make_pipes():
    pipes, models_names, models = [], [], []

    model = SVC(kernel='linear',
                C=50,
                gamma=0.1,
                degree=3,
                coef0=0.0,
                probability=True,
                random_state=1000000)
    models.append(model)

    model = SVC(kernel='poly',
                C=0.1,
                gamma=0.001,
                degree=3,
                coef0=0.0,
                probability=True,
                random_state=1000000)
    models.append(model)

    model = SVC(kernel='rbf',
                C=100,
                gamma=0.01,
                degree=3,
                coef0=0.0,
                probability=True,
                random_state=1000000)
    models.append(model)

    model = SVC(kernel='sigmoid',
                C=0.3,
                gamma=0.0004389816,
                degree=3,
                coef0=0.01,
                probability=True,
                random_state=1000000)
    models.append(model)

    for m in models:
        pipe = make_pipeline(m)
        pipes.append(pipe)
        models_names.append('svc')
    return pipes, models_names


def make_grid_optimization_pipes(n_features):
    estimator = SVC()

    grid_parameters = {
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'C': [0.01, 0.1, 1, 5, 10, 50, 100],
        'gamma': ['scale', 'auto', 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.5, 1, 5, 10],
        'degree': [2, 3, 5],
        'coef0': [0],
        'probability': [True],
        'random_state': [707878]
    }

    return estimator, grid_parameters


def set_parameters(parameters):
    return SVC(kernel=parameters['kernel'], C=parameters['C'], gamma=parameters['gamma'], degree=parameters['degree'],
               coef0=parameters['coef0'], probability=True, random_state=707878)


def make_estimator():
    estimator = SVC(
        kernel='poly',
        C=50,
        gamma='auto',
        degree=3,
        coef0=0,
        probability=True,
        random_state=707878
    )

    return estimator
