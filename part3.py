#Amir Al Kowshik
#final assignment
#machine learning for prediction

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# extracting the data into python datatypes
with open('dataset_Facebook.csv', 'rb') as f:
    text = f.readlines()
    results = []
    for line in text:
        words = line.decode('utf-8', 'ignore').split(';')
        results.append(words)

# arranging the data
def get_list_from_title_name(title,list_2d=results):
    index = None
    for i in range(len(list_2d[0])):
        if results[0][i] == title:
            index = i

    return_list = []
    for l in list_2d[1:]:
        if l[index] == '':
            return_list.append(0.0)
        else:
            return_list.append(float(l[index]))

    return return_list

reach = get_list_from_title_name('Lifetime Post Total Reach')
page_total_likes = get_list_from_title_name('Page total likes')
category = get_list_from_title_name('Category')
post_month = get_list_from_title_name('Post Month')
post_weekday = get_list_from_title_name('Post Weekday')
post_hour = get_list_from_title_name('Post Hour')
paid = get_list_from_title_name('Paid')

output_data = reach[:]
input_data = []
for a,b,c,d,e,f in zip(page_total_likes,category,post_month,post_weekday,post_hour,paid):
    input_data.append([a,b,c,d,e,f])

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


