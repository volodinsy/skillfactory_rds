# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 07:51:26 2021

@author: volodin
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import re
from collections import Counter

answers={}
 

print('*'*80)
print('Вопрос №1')
print('У какого фильма из списка самый большой бюджет\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
display(movie_bd.original_title[movie_bd['budget'] == movie_bd.budget.max()])
answers['1']='+','Pirates of the Carribean: On Stranger Tides (tt1298650)'
print()


print('*'*80)
print('Вопрос №2')
print('Какой из фильмов самый длительный (в минутах)\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
display(movie_bd.sort_values(by='runtime', ascending = False).head(1)['original_title'])
answers['2']='+','Gods and Generals (tt0279111)'
print()


print('*'*80)
print('Вопрос №3')
print('Какой из фильмов самый короткий (в минутах)\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
display(movie_bd.sort_values(by='runtime', ascending = True).head(1)['original_title'])
answers['3']='+','Winnie the Pooh (tt1449283)'
print()


print('*'*80)
print('Вопрос №4')
print('Какова средняя длительность фильмов\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
display(round(movie_bd.runtime.mean()))
answers['4']='+','110'
print()


print('*'*80)
print('Вопрос №5')
print('Каково медианное значение длительности фильмов\n') 
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 
display(movie_bd['runtime'].median())
answers['5']='+','107'
print()


print('*'*80)
print('Вопрос №6')
print('Какой фильм самый прибыльный\n') 
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 
#прибыль фильма это разница между кассовыми сборами и затраченными на его
#производство средствами
profit=movie_bd.revenue-movie_bd.budget
display(movie_bd[profit == profit.max()]['original_title'])
answers['6']='+','Avatar (tt0499549)'
print()


print('*'*80)
print('Вопрос №7')
print('Какой фильм самый убыточный\n')  
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
profit=movie_bd.revenue-movie_bd.budget
display(movie_bd.original_title[profit == profit.min()])
answers['7']='+','The Lone Ranger (tt1210819)'
print()


print('*'*80)
print('Вопрос №8')
print('''У скольки фильмов из датасета объём сборов оказался выше бюджета
Какой фильм самый убыточный\n''') 
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
display(movie_bd.revenue.loc[movie_bd.revenue>movie_bd.budget].count())
display(movie_bd.original_title[movie_bd.revenue>movie_bd.budget].sort_values(ascending = True).head(1))
answers['8']='+','1478'
print()


print('*'*80)
print('Вопрос №9')
print('Какой фильм оказался самым кассовым в 2008 году\n') 
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['profit']=movie_bd['revenue']-movie_bd['budget']
display(movie_bd[movie_bd['profit']==movie_bd[movie_bd['release_year']==2008]['profit'].max()]['original_title'])
answers['9']='+','The Dark Knight (tt0468569)'
print()


print('*'*80)
print('Вопрос №10')
print('Самый убыточный фильм за период с 2012 по 2014 годы (включительно)\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 
movie_bd['profit']=movie_bd['revenue']-movie_bd['budget']
display(movie_bd[movie_bd['profit'] == movie_bd[(movie_bd['release_year'] > 2011) &  (movie_bd['release_year'] < 2015)]['profit'].min()]['original_title'])
answers['10']='+','The Lone Ranger (tt1210819)'
print()


print('*'*80)
print('Вопрос №11')
print('Какого жанра фильмов больше всего\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 

genre = (movie_bd.set_index(movie_bd.columns.drop('genres',1).tolist())
        .genres.str.split('|', expand=True)
        .stack()
        .reset_index()
        .rename(columns={0:'genres'})
      .loc[:, movie_bd.columns]
   )
display(genre['genres'].value_counts().sort_values(ascending = False).head(1))
answers['11']='+','Drama'
print()


print('*'*80)
print('Вопрос №12')
print('Какого жанра среди прибыльных фильмов больше всего\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 
movie_bd['profit']=movie_bd['revenue']-movie_bd['budget']
genre = (movie_bd.set_index(movie_bd.columns.drop('genres',1).tolist())
        .genres.str.split('|', expand=True)
        .stack()
        .reset_index()
        .rename(columns={0:'genres'})
      .loc[:, movie_bd.columns]
   )
display(genre[genre['profit'] > 0]['genres'].value_counts().head(5))
answers['12']='+','Drama'
print()


print('*'*80)
print('Вопрос №13')
print('У какого режиссёра самые большие суммарные кассовые сборы\n')
movie_bd = pd.read_csv('../.spyder-py3/movie_bd_v5.csv') 
display(movie_bd.groupby(['director'])['revenue'].sum().sort_values(ascending=False).head(1))
answers['13']='+','Peter Jackson'
print()


print('*'*80)
print('Вопрос №14')
print('Какой режисер снял больше всего фильмов в стиле Action\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd.genres='Action'
display(movie_bd.director.value_counts().head(5))
answers['14']='-','Ridley Scott '
print()


print('*'*80)
print('Вопрос №15')
print('Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['profit'] = movie_bd['revenue'] - movie_bd['budget']
actor = (movie_bd.set_index(movie_bd.columns.drop('cast',1).tolist())
      .cast.str.split('|', expand=True)
      .stack()
       .reset_index()
       .rename(columns={0:'cast'})
      .loc[:, movie_bd.columns]
   )
prof = actor[(actor['release_year'] == 2012)]
display(prof.groupby(['cast'])['profit'].sum().sort_values(ascending=False).head(1))
answers['15']='+','Chris Hemsworth'
print()


print('*'*80)
print('Вопрос №16')
print(""" Какой актер снялся в большем количестве высокобюджетных фильмов?
Примечание: в фильмах где бюджет выше среднего по данной выборке.\n""")
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
actor = (movie_bd.set_index(movie_bd.columns.drop('cast',1).tolist())
      .cast.str.split('|', expand=True)
      .stack()
       .reset_index()
       .rename(columns={0:'cast'})
      .loc[:, movie_bd.columns]
   )
display(actor[actor['budget'] > actor['budget'].mean()]['cast'].value_counts().sort_values(ascending=False).head(1))
answers['16']='+','Matt Damon'
print()


print('*'*80)
print('Вопрос №17')
print('В фильмах какого жанра больше всего снимался Nicolas Cage\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
actor = (movie_bd.set_index(movie_bd.columns.drop('cast',1).tolist())
      .cast.str.split('|', expand=True)
      .stack()
       .reset_index()
       .rename(columns={0:'cast'})
      .loc[:, movie_bd.columns]
   )

nicolas = actor[actor['cast'] == 'Nicolas Cage']['genres']
nicolas = nicolas.apply(lambda x: x.split('|'))

nf = []
for genres in nicolas:
    for genre in genres:
        nf.append(genre)
import collections
c = collections.Counter()
for word in nf:
     c[word] += 1
print(c)
answers['17']='+','Action'
print()


print('*'*80)
print('Вопрос №18')
print('Самый убыточный фильм от Paramount Pictures\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['profit'] = movie_bd['revenue'] - movie_bd['budget']
param = movie_bd[movie_bd['production_companies'] == 'Paramount Pictures']
display(param.original_title[param['profit']==param['profit'].min()])
answers['18']='-','Domestic Disturbance - ответа нет в вариантах'
print()


print('*'*80)
print('Вопрос №19')
print('Какой год стал самым успешным по суммарным кассовым сборам\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['profit'] = movie_bd['revenue'] - movie_bd['budget']
group_revenue=movie_bd.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
display(group_revenue.head(1))
answers['19']='+','2015'
print()


print('*'*80)
print('Вопрос №20')
print('Какой самый прибыльный год для студии Warner Bros\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['profit'] = movie_bd['revenue'] - movie_bd['budget']
display(movie_bd[movie_bd['production_companies'].str.contains("Warner", na=False) == True].groupby(['release_year']).sum().sort_values(by='profit', ascending=False).head(1))
answers['20']='+','2014'
print()


print('*'*80)
print('Вопрос №21')
print('В каком месяце за все годы вышло суммарно больше всего фильмов\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd["Month"] = pd.to_datetime(movie_bd["release_date"], format="%m/%d/%Y")
movie_bd["Month"] = pd.DatetimeIndex(movie_bd['Month']).month
xx = movie_bd.groupby(["Month"])['imdb_id'].count()
display(xx.sort_values(ascending=False).head(1))
answers['21']='+','9 - Сентябрь'
print()


print('*'*80)
print('Вопрос №22')
print('Сколько суммарно вышло фильмов летом (за июнь, июль, август)\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd["Month"] = pd.to_datetime(movie_bd["release_date"], format="%m/%d/%Y")
movie_bd["Month"] = pd.DatetimeIndex(movie_bd['Month']).month
display(movie_bd[(movie_bd['Month'] == 6) | (movie_bd['Month'] == 7) | (movie_bd['Month'] == 8)]['imdb_id'].count())
answers['22']='+','450'
print()


print('*'*80)
print('Вопрос №23')
print('Для какого режиссёра зима - самое продуктивное время года')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd["Month"] = pd.to_datetime(movie_bd["release_date"], format="%m/%d/%Y")
movie_bd["Month"] = pd.DatetimeIndex(movie_bd['Month']).month
display(movie_bd[(movie_bd['Month'] == 12) | (movie_bd['Month'] == 1) | (movie_bd['Month'] == 2)].groupby(['director']).count().sort_values(by='imdb_id', ascending=False).head(1))
answers['23']='+','Peter Jackson '
print()


print('*'*80)
print('Вопрос №24')
print('Какая студия даёт самые длинные названия своим фильмам по количеству символов\n')

movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['length'] = movie_bd['original_title'].apply(lambda x: len(x))

product = (movie_bd.set_index(movie_bd.columns.drop('production_companies',1).tolist())
        .production_companies.str.split('|', expand=True)
        .stack()
        .reset_index()
        .rename(columns={0:'production_companies'})
      .loc[:, movie_bd.columns]
   )
display(product.groupby('production_companies')['length'].max().sort_values(ascending=False).head())
answers['24']='+','Four By Two Productions'
print()


print('*'*80)
print('Вопрос №25')
print('Описания фильмо какой студии в среднем самые длинные по количеству слов\n')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
movie_bd['word'] = movie_bd['original_title'].apply(lambda x: len(x.split(' ')))

product = (movie_bd.set_index(movie_bd.columns.drop('production_companies',1).tolist())
        .production_companies.str.split('|', expand=True)
        .stack()
        .reset_index()
        .rename(columns={0:'production_companies'})
      .loc[:, movie_bd.columns]
   )
display(product.groupby('production_companies')['word'].max().sort_values(ascending=False).head(30
                                                                                                ))
answers['25']='-','Warner Bros.'
print()


print('*'*80)
print('Вопрос №26')
print('Какие фильмы входят в один процент лучших по рейтингу')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
#количество фильмов, которое входит в 1%
persent1 = int(len(movie_bd) * 0.01)
#отсортируем по убыванию 1% лучших по рейтингу фильмов 
xx = movie_bd.sort_values(by='vote_average',  ascending=False)[:persent1]
display(xx.original_title)
answers['26']='+','Inside Out,The Dark Knight,12 Years a Slave'
print()


print('*'*80)
print('Вопрос №27')
print('Какие актеры чаще всего снимаются в одном фильме вместе')
movie_bd=pd.read_csv('../.spyder-py3/movie_bd_v5.csv')
#скопируем столбец cast в столбец castcoma и уберем разделители в виде "," и "/"
movie_bd['castcoma'] = movie_bd['cast'].apply(lambda x: x.replace('|', ', '))

jh =  ['Johnny Depp', 'Helena Bonham Carter']
hi =  ['Hugh Jackman', 'Ian McKellen']
vp =  ['Vin Diesel', 'Paul Walker']
ak =  ['Adam Sandler', 'Kevin James']
dr = ['Daniel Radcliffe', 'Rupert Grint']

#ищем совпадения
jhs = movie_bd[(movie_bd.castcoma.str.contains("Johnny Depp", na=False)) & (movie_bd.castcoma.str.contains("Helena Bonham Carter", na=False))]
his = movie_bd[(movie_bd.castcoma.str.contains("Hugh Jackman", na=False)) & (movie_bd.castcoma.str.contains("Ian McKellen", na=False))]
vps = movie_bd[(movie_bd.castcoma.str.contains("Vin Diesel", na=False)) & (movie_bd.castcoma.str.contains("Paul Walker", na=False))]
aks = movie_bd[(movie_bd.castcoma.str.contains("Adam Sandler", na=False)) & (movie_bd.castcoma.str.contains("Kevin James", na=False))]
drs = movie_bd[(movie_bd.castcoma.str.contains("Daniel Radcliffe", na=False)) & (movie_bd.castcoma.str.contains("Rupert Grint", na=False))]
#выводим количество этих совпадений
print()

print("Johnny Depp & Helena Bonham Carter -",len(jhs))
print("Hugh Jackman & Ian McKellen -",len(his))
print("Vin Diesel & Paul Walker -",len(vps))
print("Adam Sandler & Kevin James -",len(aks))
print("Daniel Radcliffe & Rupert Grint -",len(drs))
answers['27']='+','Daniel Radcliffe & Rupert Grint'


display(answers)
display(len(answers))


