from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from scipy.stats import randint


def make_pipes():
    pipes, models_names = [], []

    algorithms = ['auto']
    weights = ['uniform']
    n_neighbors = [20, 25, 30, 35, 40]

    for weight in weights:
        for algorithm in algorithms:
            for n_neighbor in n_neighbors:
                model = KNeighborsClassifier(
                    n_neighbors=n_neighbor,
                    weights=weight,
                    algorithm=algorithm,
                    leaf_size=30,
                    n_jobs=-1)
                pipe = make_pipeline(model)
                pipes.append(pipe)
                models_names.append('kneighborsclassifier')
    return pipes, models_names


def make_grid_optimization_pipes(n_features):
    estimator = KNeighborsClassifier()

    grid_parameters = {
        'n_neighbors': [1, 2, 3, 5, 10, 20, 25, 30, 35, 40],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'brute'],
        'leaf_size': [1, 5, 10, 20, 30],
        'n_jobs': [-1]
    }

    return estimator, grid_parameters


def set_parameters(parameters):
    return KNeighborsClassifier(n_neighbors=parameters['n_neighbors'], weights=parameters['weights'],
                                algorithm=parameters['algorithm'], leaf_size=parameters['leaf_size'], n_jobs=-1)


def make_random_optimization_pipes(n_features):
    estimator = [KNeighborsClassifier()]
    estimator_name = 'kneighborsclassifier'

    random_parameters = {
        'n_neighbors': randint(10, 40),
        'weights': ['uniform'],
        'algorithm': ['auto'],
        'leaf_size': [30],
        'n_jobs': [-1]
    }

    return estimator, random_parameters, estimator_name


def make_estimator():
    estimator_name = 'kneighborsclassifier'
    estimator = KNeighborsClassifier(
        n_neighbors=20,
        weights='uniform',
        algorithm='auto',
        leaf_size=30,
        n_jobs=-1
    )

    return estimator, estimator_name