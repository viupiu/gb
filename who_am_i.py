import pandas as pd

# условие задачи
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'who_am_i':lst})
data.head()

# создаем 2 новых столбца со значением 0 по умолчанию
data['robot'] = 0
data['human'] = 0

# для тех строк, где ячейка whoAmI == robot записываем в столбец robot: 1 (то же и с human)
data.loc[data['who_am_i'] == 'robot', 'robot'] = 1
data.loc[data['who_am_i'] == 'human', 'human'] = 1

# удаляем столбец whoAmI
data.drop('who_am_i', axis=1, inplace=True)