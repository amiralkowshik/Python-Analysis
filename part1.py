#Amir Al Kowshik
#Final Assignment
#Machine learning for prediction

import random
from sklearn.linear_model import LinearRegression

training_set = []
result_set = []

for i in range(100):
    x = random.randint(1,999)
    y = random.randint(1,999)
    z = random.randint(1,999)

    training_set.append([x,y,z])
    result_set.append(x*1 + y*2 + z*3)

predictor = LinearRegression(n_jobs=1)
predictor.fit(X=training_set, y=result_set)

test_input = [[10,20,30]]
result = predictor.predict(X=test_input)
coefficients = predictor.coef_

print("Prediction: "+str(result))
print("Coefficients: "+str(coefficients))
