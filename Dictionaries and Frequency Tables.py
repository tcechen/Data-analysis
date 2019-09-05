## 1. Storing Data ##

content_ratings=['4+','9+','12+','17+']
numbers=[4433,987,1155,622]
content_rating_numbers=[['4+','9+','12+','17+'],[4433,987,1155,622]]

## 2. Dictionaries ##

content_ratings={'4+':4433,'9+':987,'12+':1155,'17+':622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_9=content_ratings['9+']
over_17=content_ratings['17+']
print(over_9)
print(over_17)

## 4. Alternative Way of Creating a Dictionary ##

content_ratings={}
content_ratings['4+']=4433
content_ratings['9+']=987
content_ratings['12+']=1155
content_ratings['17+']=622
over_12_n_apps=content_ratings['12+']

## 5. Key-Value Pairs ##

d_1 = {'key_1': 'first_value', 
       'key_2': 2,
       'key_3': 3.14,
       'key_4': True,
       'key_5': [4,2,1],
       'key_6': {'inner_key' : 6}}

error = True

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1='9+' in content_ratings
is_in_dictionary_2=987 in content_ratings
if '17+' in content_ratings:
    result='It exists'
    print(result)

## 7. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings={'4+':0,'9+':0,'12+':0,'17+':0}
for row in apps_data[1:]:
    c_rating=row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating]+=1
print(content_ratings)


## 8. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings={}
for row in apps_data[1:]:
    c_rating=row[10]
    if c_rating in content_ratings:
        content_ratings[c_rating]+=1
    else:
        content_ratings[c_rating]=1
print(content_ratings)
                

## 9. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
genre_counting={}
for row in apps_data[1:]:
    genre=row[11]
    if genre in genre_counting:
        genre_counting[genre]+=1
    else:
        genre_counting[genre]=1
print(genre_counting)

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
for iteration_var in content_ratings:
    content_ratings[iteration_var]/=total_number_of_apps
    content_ratings[iteration_var]*=100
percentage_17_plus=content_ratings['17+']
percentage_15_allowed=100-content_ratings['17+']

## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions={}
c_ratings_percentages={}
for key in content_ratings:
    proportion=content_ratings[key]/total_number_of_apps
    c_ratings_proportions[key]=proportion
    proportion*=100
    c_ratings_percentages[key]=proportion


## 12. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
data_sizes=[]
for row in apps_data[1:]:
    size=float(row[2])
    data_sizes.append(size)
min_size=min(data_sizes)
max_size=max(data_sizes)

## 13. Filtering for the Intervals ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
data_size_final={'0-6':0,'6-12':0,'12-18':0,'18-24':0,'24-30':0}
for row in apps_data[1:]:
    data_size=float(row[5])

    if data_size<600000:
        data_size_final['0-6'] +=1
    elif 600000<data_size<=1200000:
        data_size_final['6-12']+=1
    elif 1200000<data_size<=1800000:
        data_size_final['12-18']+=1
    elif 1800000<data_size<=2400000:
        data_size_final['18-24']+=1
    elif 2400000<data_size<=3000000:
        data_size_final['24-30']+=1    
        
print(data_size_final)