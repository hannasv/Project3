# Project 3 
## Versions of Python packages 
There are three available envornments, use env_nn.txt when running the notebooks; LinearRegression.ipynb,  	NeuralNetworks_1timestep.ipynb, NeuralNetworks_7days.ipynb and NeuralNetworks_1timestep_logit.ipynb. The enviornments tflow.txt is for the notebooks; tensorflow_nn.ipynb and tensorflow_nn_different_results.ipynb. The notebooks trees_7days.ipynb and trees_t0.ipynb. We underline that these enviornments are different and that they are used on different operationssystems. The invormation on how to create an evirnment and which platform it run on can be found in the first lines in the txt-file.

## Abstract

In this article, we describe the  first attempt on predicting total cloud cover fraction over the Europa based on pressure, temperature, specific- and relative humidity data measured at the ground. The data was obtained from European centre for medium range weather forecasting, ECMWF.

We will using a wide range of models; Linear regression, self-implemented fully connected feed forward neural networks, neural networks from the Python libraries Keras and TensorFlow and Random forest trees in a attempt to find the most suitable model.
All the codes are available in this GitHub repositoy.

The self-implemented neural networks performance worsened for a increasing number of hidden layers. The best performance with one layer was $MSE \approx 0.75$. Using one layer all combinations of nodes converged toward this value, we didn't really see a clear difference. The best performance using four layers was a $MSE \approx 1$, this is worse than linear regression (OLS) which had a $MSE \approx 0.9$. This could be because we didn't find the correct numbers of nodes, but is most likely its a to simple model to describe such a complex problem. Keras performed a lot better the the self-implemented network conforming that increased complexity in a neural network increases performance of the prediction. Keras showed the best performance for 2 layers here the $MSE \approx 0.48$. 

% Describing the best preformance
Random forest performed best with a MSE of approximately 0.45. This had a larger tendency to underestimate than decision trees. Decision trees had a MSE around 0.6, a R2-score of 0.4, which tells us that the model explains roughly 40\% of the variation in the data. This is actually not that bad in a meteorological context. 



## Structure and implementations
The programs are written inn python scrips and the results are produced in the notebooks. Writing these article produced a lot of results, we found it best to use many notebooks to keep a good order. 

deepNN.py contains the program for our self-implemented neural network. This is a implroved version of project 2 ann.py, this version is improved to build networks with different numbers of nodes and number of hidden layers. The code for using linear regression has been updated with a normalization of the response. The results of this can be found in the notebooks, LinearRegression.ipynb and NeuralNetworks*.ipynb. The notebooks containing results by using keras, tensorflow (tflow)
 and trees have notebooks named accordingly.
 
The folder with results contain all the figures created with the notebooks.



