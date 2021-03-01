import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from wordcloud import WordCloud
%matplotlib inline


class KakaoAnalysis:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.user = self.df['User'].drop_duplicates().values
        self.start = self.start_meta()
        self.end = self.end_meta()

    def meta(self):
        print(self.start)
        print(self.end)
        print(self.user)
    
    def rename(self, user):
        if len(self.user) == len(user):
            for i in range(len(self.user)):
                self.df['User'].replace(self.user[i], user[i], inplace=True)
            for i in range(len(self.user)):
                self.df['Message'] = self.df['Message'].str.replace('@'+self.user[i], '@'+user[i])
            self.user = user
        else:
            print('유저맵의 길이가 일치하지않음')
            print(self.user)
            print(user)

    def start_meta(self):
        date = self.df.head(1)['Date'].values[0]
        dt = date.split()
        res = {
            "datetime": date,
            "date": dt[0],
            "time": dt[1]
        }
        return res

    def end_meta(self):
        date = self.df.tail(1)['Date'].values[0]
        dt = date.split()
        res = {
            "datetime": date,
            "date": dt[0],
            "time": dt[1]
        }
        return res

    def clear(self, token=False, emo=True, photo=True, delete=True, url=True):
        df = self.df
        regex = r'\(http|https\):\/\/\(\w+:{0,1}\w*@\)?\(\S+\)\(:[0-9]+\)?\(\/|\/\([\w#!:.?+=&%@!\-\/]\)\)?'

        if emo == True:
            df = df[df['Message'] != '이모티콘']
        if photo == True:
            df = df[df['Message'] != '사진']
        if delete == True:
            df = df[df['Message'] != '삭제된 메시지입니다.']
        if url == True:
            df = df[df['Message'].str.contains(regex, regex=True) == False]
        # df['Message'] = df['Message'].str.replace(regex, '')
        return df

    def test(self):
        # a = self.df['Message'].str.len()
        df = self.clear()
        self.word_cloud(self.clear())

    def word_cloud(self, df=None):
        if df.empty:
            df = self.df
        text = df['Message'].values
        wordcloud = WordCloud(font_path=fontpath).generate(' '.join(text))
        plt.figure(figsize = (15 , 10))
        plt.imshow(wordcloud, interpolation='bilinear') 
        plt.axis('off')
        plt.show()
