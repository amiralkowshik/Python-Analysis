#Amir Al Kowshik
#final assignment
#machine learning for prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# extracting the data into python datatypes
with open('SeoulBikeData.csv', 'rb') as f:
    text = f.readlines()
    results = []
    for line in text:
        words = line.decode('utf-8', 'ignore').split(',')
        results.append(words)

# arranging the data
def get_list_from_title_name(title,list_2d=results):
    index = None
    for i in range(len(list_2d[0])):
        if results[0][i] == title:
            index = i

    return_list = []
    for l in list_2d[1:]:
        return_list.append(float(l[index]))

    return return_list

rented_bike_count = get_list_from_title_name('Rented Bike Count')
hour = get_list_from_title_name('Hour')
temperature = get_list_from_title_name('Temperature(C)')
humidity = get_list_from_title_name('Humidity(%)')
wind_speed = get_list_from_title_name('Wind speed (m/s)')
visibility = get_list_from_title_name('Visibility (10m)')
dew_point_temperature = get_list_from_title_name('Dew point temperature(C)')
radiation = get_list_from_title_name('Solar Radiation (MJ/m2)')
rainfall = get_list_from_title_name('Rainfall(mm)')
snowfall = get_list_from_title_name('Snowfall (cm)')


output_data = rented_bike_count[:]
input_data = []
for a,b,c,d,e,f,g,h,i in zip(hour,temperature,humidity,wind_speed,visibility,dew_point_temperature,radiation,radiation,snowfall):
    input_data.append([a,b,c,d,e,f,g,h,i])

x_train, x_test, y_train, y_test = train_test_split(input_data, output_data, train_size=0.8)


predictor = LinearRegression(n_jobs=1)
predictor.fit(X=x_train, y=y_train)

result = predictor.predict(X=x_test)

errors = []

for i in range(len(result)):
    if y_test[i] != 0:
        percentageError = abs(y_test[i] - result[i]) / y_test[i]
        errors.append(percentageError)


error_count = {
    "less than 10%":0,
    "10% to 20%": 0,
    "20% to 30%": 0,
    "30% to 40%": 0,
    "40% to 50%": 0,
    "50% to 60%": 0,
    "60% to 70%": 0,
    "70% to 80%": 0,
    "80% to 90%": 0,
    "90% to 100%": 0,
    "more than 100%": 0
}

for err in errors:
    if err < 0.1:
        error_count["less than 10%"] += 1
    elif err > 0.1 and err < 0.2:
        error_count["10% to 20%"] += 1
    elif err > 0.2 and err < 0.3:
        error_count["20% to 30%"] += 1
    elif err > 0.3 and err < 0.4:
        error_count["30% to 40%"] += 1
    elif err > 0.4 and err < 0.5:
        error_count["40% to 50%"] += 1
    elif err > 0.5 and err < 0.6:
        error_count["50% to 60%"] += 1
    elif err > 0.6 and err < 0.7:
        error_count["60% to 70%"] += 1
    elif err > 0.7 and err < 0.8:
        error_count["70% to 80%"] += 1
    elif err > 0.8 and err < 0.9:
        error_count["80% to 90%"] += 1
    elif err > 0.9 and err < 1.0:
        error_count["90% to 100%"] += 1
    elif err > 1.0:
        error_count["more than 100%"] += 1

print(error_count)
