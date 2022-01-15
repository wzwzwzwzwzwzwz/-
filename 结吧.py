# coding: utf-8

# standard import

import re
# third-party import
from refo import finditer, Predicate, Star, Any
import jieba.posseg as pseg
from jieba import suggest_freq
import jieba

from SPARQLWrapper import SPARQLWrapper, JSON

jieba.load_userdict("./country.txt")
words =pseg.cut("治愈")
for w in words:
 print(w.word,w.flag)

i = "中国"
e = "?Y ub:country_name " + '"' + i + '"' + ". ?Y ub:total_heal ?X ."
print(e)