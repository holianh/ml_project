from decision_tree import run_decision_tree 
from k_nearest_neighbour import run_k_nearest_neighbour
from logistic_regression import run_logistic_regression
from naive_bayes import run_naive_bayes
from neural_network import run_neural_network
from perceptron import run_perceptron
from random_forest import run_random_forest
from svm import run_svm
from xg_boost import run_xg_boost
import numpy as np
from data_preprocessor import get_data

if __name__ == '__main__':
	x_train, x_test, y_train, y_test = get_data()

	run_decision_tree(x_train, x_test, y_train, y_test)
	run_k_nearest_neighbour(x_train, x_test, y_train, y_test)
	run_logistic_regression(x_train, x_test, y_train, y_test)
	run_naive_bayes(x_train, x_test, y_train, y_test)
	run_neural_network(x_train, x_test, y_train, y_test)
	run_perceptron(x_train, x_test, y_train, y_test)
	run_random_forest(x_train, x_test, y_train, y_test)
	run_svm(x_train, x_test, y_train, y_test)
	run_xg_boost(x_train, x_test, y_train, y_test)