# -*- coding: utf-8 -*-
#
# model_selection.py
#
# The module is part of model_comparison.
#

"""
The hyperparameter grid search framework.
"""

__author__ = 'Hanna Svennevik', 'Paulina Tedesco'
__email__ = 'hanna.svennevik@fys.uio.no', 'paulinatedesco@gmail.com'


import numpy as np
from utils import bootstrap, mean_squared_error, train_test_split, r2_score, A_R2, NRMSE, transforming_predictorspace, standardicing_responce

#from sklearn.model_selection import train_test_split

class GridSearch:

    """
    Determines optimal hyperparameter for given algorithm, without resampling.
    """

    def __init__(self, model, params, name, feature_scale = False):
        self.model = model
        self.params = params
        self.name = name
        self.feature_scale = feature_scale
        
        self.best_mse = None
        self.best_r2 = None
        self.best_param_mse = None
        self.best_param_r2 = None
        self.best_avg_z_pred_mse = None
        self.avg_z_pred = None
        self.best_avg_z_pred_r2 = None
        self.mse_test = None
        self.mse_train = None
        self.r2_test = None
        self.r2_train = None
        self.coef_ = None
        
        
    def fit(self, X, z, split_size):
        """Searches for the optimal hyperparameter combination."""
        # model and params are now lists --> sende med navn istedenfor.
        # Setup
        self.results = {self.name: []}
        self.train_scores_mse, self.test_scores_mse= [], []
        self.train_scores_r2, self.test_scores_r2 = [], []

        # Splitting our original dataset into test and train.
        X_train, X_test, z_train, z_test = train_test_split(X, z, test_size = split_size, feature_scale = self.feature_scale)

        """ Returning these dictionaries to plot (standardized response) mse, r2 vs model"""
        self.mse_test = []
        self.mse_train = []
        self.r2_test = []
        self.r2_train = []
        self.z_pred = []
        self.coef_ = []
        # For en model tester vi alle parameterne og returnerer denne.
        for param in self.params:
            estimator = self.model(lmd=param)
            # Train a model for this pair of lambda and random state
            estimator.fit(X_train, z_train)

            temp = estimator.predict(X_test)
            temp2 = estimator.predict(X_train)
            
            # Tranforming values which left the predictor space back into the predictor space
            # Special case for this cloud cover predictions.             
            temp = transforming_predictorspace(temp)
            temp2 = transforming_predictorspace(temp2)
            
            # Standardizing the response in order to make the performance metrics comparable. 
            temp = standardicing_responce(temp)
            temp2 = standardicing_responce(temp2)
                
            #n,p = np.shape(X_train) Only nessesary for using adjusted r2 score.
            
            z_test = standardicing_responce(z_test)
            z_train = standardicing_responce(z_train)
            
            self.mse_test.append(mean_squared_error(z_test, temp))
            self.mse_train.append(mean_squared_error(z_train, temp2))
            self.r2_test.append(r2_score(z_test, temp))
            self.r2_train.append(r2_score(z_train, temp2))
            
            self.z_pred.append(temp)
            self.coef_.append(estimator.coef_)
        return self
