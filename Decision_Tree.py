import pandas as pdimport numpy as npfrom sklearn.model_selection import train_test_splitfrom sklearn.tree import DecisionTreeRegressorfrom sklearn import metricscolumns = ['Frequency', 'Angle of Attack', 'Chord Length', 'Velocity', 'Displacement', 'Sound Pressure']data = pd.read_csv('airfoil_self_noise.dat', sep='\t', names=columns)x = data.drop('Sound Pressure', axis=1)y = data['Sound Pressure']train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.3, random_state=101)regressor = DecisionTreeRegressor(random_state=101)regressor.fit(train_x, train_y)predictor = regressor.predict(test_x)predictor_df = pd.DataFrame(predictor)eval = pd.DataFrame({'test':test_y, 'predict': predictor})mae = metrics.mean_absolute_error(test_y, predictor)mse = metrics.mean_squared_error(test_y, predictor)rmse = np.sqrt(mse)print('######### Decision Tree ###############')print('DTMAE: ', mae)print('DTMSE: ', mse)print('DTRMSE: ', rmse)print(eval.head(50))