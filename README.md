Regression-Algorithm-Comparison

Data set:
The data set is obtained from a series of aerodynamic and acoustic tests of two and three-dimensional airfoil blade sections conducted in an anechoic wind tunnel by NASA.
The data set comprises of different size NACA 0012 airfoils at various wind tunnel speeds and angles of attack. The span of the airfoil and the observer position were the same in all of the experiments.

Machine Learning: Regression Operations:
Three Different Regression Operations were carried on an airfoil noise data set
1. Support vector Regression
2. Decision Tree Regression
3. Random Forest Regression
These Linear Regression and Polynomial Regression Operations were considered for this data set but during the data set exploration process, it is discovered that the relation between the input attributes, ['Frequency', 'Angle of Attack', 'Chord Length', 'Velocity', 'Displacement'] and the output attribute, ['Sound Pressure'] is neither linear nor polynomial, hence both operations were ignored

Evaluation Metrics:
These Algorithm were compared using Evaluated using
1. Mean Absolute Error (mae)
2. Mean Squared Error (mse)
3. Root Mean Squared Error (rmse)

Performance
Support Vector Regression performed the least impressive with the highest value of mae, mse and rmse, this followed by Decision Tree Regression and the best performing Algorithm for this data set is Random forest Regression with the lowest values of mae, mse and rmse