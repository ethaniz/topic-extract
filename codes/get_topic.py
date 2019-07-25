# -*- coding:utf8 -*-
'''
@Author: 异尘
@Date: 2019/07/25 14:52:32
@Description: 
'''

# here put the import lib

import urllib.request 
from bs4 import BeautifulSoup
import jieba
import jieba.analyse
import string
import zhon
from zhon.hanzi import punctuation
import re
import pdb

punc = string.punctuation + punctuation + '©' + '¥'
jieba.load_userdict('./dict.txt')
stopwords = set([line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()])

def is_stop_word(s):
    if s in stopwords:
        return True
    else:
        return False

def url2html(url):
    html = urllib.request.urlopen(url).read()
    return html

def get_word_splits(html):
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text = re.sub('[%s]+' % re.escape(punc), '', text)
    texts = text.split('\n')
    #pdb.set_trace()

    word_lists = []
    for text in texts:
        word_lists += (list(jieba.cut(text, cut_all=False)))

    word_lists = [w for w in word_lists if not is_stop_word(w)]
    return word_lists

def get_tfidf(word_lists):
    keywords = jieba.analyse.extract_tags(' '.join(word_lists), topK=20, withWeight=True, allowPOS=['n', 'ns', 'nr', 'nt', 'nz'])
    return keywords

def get_topic_from_url(url):
    html = url2html(url)
    word_lists = get_word_splits(html)
    keywords = get_tfidf(word_lists)
    return keywords


if __name__ == "__main__":
    url = "https://www.meb.com/diarylist/17932/"
    
    keywords = get_topic_from_url(url)
    for item in keywords:
        print(item[0],item[1])







