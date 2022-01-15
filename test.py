# coding: utf-8

# standard import

import re
# third-party import
from refo import finditer, Predicate, Star, Any
import jieba.posseg as pseg
from jieba import suggest_freq
import jieba

from SPARQLWrapper import SPARQLWrapper, JSON

sparql_base = SPARQLWrapper("http://localhost:3030/countries/query")

# SPARQL config
SPARQL_PREAMBLE = u"""
PREFIX ua:<http://www.kbqa.com/>
PREFIX ub:<http://www.kbqa.com/properties#>
"""

SPARQL_Tem = u"{preamble}\n" + \
             u"SELECT DISTINCT {select} WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n"

INDENT = "    "


class Word(object):
    """treated words as objects"""
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos

class W(Predicate):
    """object-oriented regex for words"""
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2

class Rule(object):
    def __init__(self, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        #if __name__ == '__main__':
            #print("----------applying %s----------" % self.action.__name__)
        return self.action(matches)

class Video(object):
    def __init__(self,path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)

class Movie_MP4(Video):
    type = 'MP4'

def total_confirm(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode(
                'utf_8') + '"' + ". ?Y ub:total_confirm ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def total_suspect(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode(
                'utf_8') + '"' + ". ?Y ub:total_suspect ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def total_heal(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:total_heal ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def total_dead(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:total_dead ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def total_severe(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode(
                'utf_8') + '"' + ". ?Y ub:total_severe ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def total_input(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:total_input ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql

def today_confirm(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode(
                'utf_8') + '"' + ". ?Y ub:today_confirm ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def today_suspect(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode(
                'utf_8') + '"' + ". ?Y ub:today_suspect ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def today_heal(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:today_heal ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def today_dead(x):
    select = u"?X"
    sparql = None
    for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:today_dead ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                       select=select,
                                       expression="\t" + e)
    # print("\nsparql查询语句是：" + "\n" + sparql)
    return sparql
def today_severe(x):
     select = u"?X"
     sparql = None
     for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:today_severe ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                      select=select,
                                      expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def today_input(x):
     select = u"?X"
     sparql = None
     for i in x:
        if i.pos == 'nr':
            e = "?Y ub:country_name " + '"' + i.token.encode('utf-8').decode('utf_8') + '"' + ". ?Y ub:today_input ?X ."
            sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                      select=select,
                                      expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql

def every_confirm(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_confirm ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\各国病例数量\各国的感染数.mp4')
     movie.play()
     return sparql
def every_suspect(x):
  print(1)
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_suspect ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def every_heal(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_heal ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\各国的治愈数\各国的治愈数.mp4')
     movie.play()
     return sparql
def every_dead(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_dead ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\各国的死亡人数\各国的死亡人数.mp4')
     movie.play()
     return sparql
def every_severe(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_severe ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def every_input(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:total_input ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql

def everyday_confirm(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_confirm ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\各国新增的感染数\各国新增的感染数.mp4')
     movie.play()
     return sparql
def everyday_suspect(x):
  print(1)
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_suspect ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def everyday_heal(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_heal ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def everyday_dead(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_dead ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def everyday_severe(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_severe ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql
def everyday_input(x):
  for i in x:
    if i.pos == 'na':
     select = u"?X ?Z"
     sparql = None
     e = "?Y ub:country_name ?X. ?Y ub:today_input ?Z."

     sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
     #print("\nsparql查询语句是：" + "\n" + sparql)
     return sparql

def max_confirm(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_confirm ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\哪个国家感染人数最多\某地死亡人数最多.mp4')
        movie.play()
        return sparql
def max_suspect(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_suspect ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        return sparql
def max_dead(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_dead ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\哪个国家死亡人数最多\某地死亡人数最多.mp4')
        movie.play()
        return sparql
def max_heal(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_heal ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        movie = Movie_MP4(r'D:\360MoveData\Users\wz\Desktop\CaseCounts\哪个国家治愈人数最多\某地死亡人数最多.mp4')
        movie.play()
        return sparql
def max_severe(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_severe ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        return sparql
def max_input(x):
    for i in x:
      if i.pos == 'nz':
        select = u"?X"
        sparql = None
        e = "?Y ub:total_input ?q. ?Y ub:country_name ?X. "

        sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                          select=select,
                                          expression="\t" + e) + "ORDER BY DESC(?q) LIMIT 1"
        #print("\nsparql查询语句是：" + "\n" + sparql)
        return sparql

def select_confirm(x): 
    for i in x:
       if i.pos=='m' :
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e="?Y ub:total_confirm?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql   
def select_suspect(x): 
    for i in x:
       if i.pos=='m' :
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e="?Y ub:total_suspect?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql
def select_dead(x):
    for i in x:
       if i.pos=='m' :
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e="?Y ub:total_dead?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql
def select_heal(x): 
    for i in x:
       if i.pos=='m' :
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e="?Y ub:total_heal?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql
def select_severe(x):
    for i in x:
        if i.pos == 'm':
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e="?Y ub:total_severe?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql
def select_input(x):
    for i in x:
       if i.pos =='m':
           print(i.token)
           select=u"?X?Z"
           sparql = None
           e ="?Y ub:total_input?Z.  FILTER(?Z>{})?Y ub:country_name?X.".format(i.token)
           sparql = SPARQL_Tem.format(preamble=SPARQL_PREAMBLE,
                                select=select,
                                expression="\t" + e)
           return sparql


if __name__ == "__main__":
    #default_questions = [
        #u"中国的治愈数",
        #u"各国的感染数",
        #u"某地的死亡人数最多",
    #]

    #questions = default_questions[0:]
 question = ""
 while question != 'quit':
    question = input('请输入问题:')

    seg_lists = []

    jieba.load_userdict("./country.txt")

    # tokenizing questions
    # for question in questions:
    words = pseg.cut(question)
    seg_list = [Word(word, flag) for word, flag in words]

    seg_lists.append(seg_list)

    # some rules for matching
    # TODO: customize your own rules here

    rules = [

##############################################################################################

        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增')+ W("感染"),
             # 某国的新增感染病例数
             action=today_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("患者"),
             # 某国的新增感染病例数
             action=today_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("患病"),
             # 某国的新增感染病例数
             action=today_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("染病"),
             # 某国的新增感染病例数
             action=today_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("感染"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("患者"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("患病"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("染病"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("感染"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("患者"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("患病"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("染病"),
             # 某国的新增疑似感染病例数
             action=today_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("治愈"),
             # 某国的新增治愈病例数
             action=today_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("治好"),
             # 某国的新增治愈病例数
             action=today_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("康复"),
             # 某国的新增治愈病例数
             action=today_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("痊愈"),
             # 某国的新增治愈病例数
             action=today_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("死亡"),
             # 某国的新增死亡病例数
             action=today_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("病死"),
             # 某国的新增死亡病例数
             action=today_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("致死"),
             # 某国的新增死亡病例数
             action=today_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("重病"),
             # 某国的新增重病数
             action=today_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("严重"),
             # 某国的新增重病数
             action=today_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("危重"),
             # 某国的新增重病数
             action=today_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("重症"),
             # 某国的新增重病数
             action=today_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("输入"),
             # 某国的新增输入病例数
             action=today_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("外来"),
             # 某国的新增输入病例数
             action=today_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("境外"),
             # 某国的新增输入病例数
             action=today_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("外输"),
             # 某国的新增输入病例数
             action=today_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W('新增') + W("国外"),
             # 某国的新增输入病例数
             action=today_input),


        #######################################################################################


        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("感染"),
             # 某国的感染病例数
             action=total_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("患者"),
             # 某国的感染病例数
             action=total_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("患病"),
             # 某国的感染病例数
             action=total_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("染病"),
             # 某国的感染病例数
             action=total_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("感染"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("患者"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能")+W("患病"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("染病"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("感染"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("患者"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("患病"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("染病"),
             # 某国的疑似感染病例数
             action=total_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("治愈"),
             # 某国的治愈病例数
             action=total_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("治好"),
             # 某国的治愈病例数
             action=total_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("康复"),
             # 某国的治愈病例数
             action=total_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("痊愈"),
             # 某国的治愈病例数
             action=total_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("死亡"),
             # 某国的死亡病例数
             action=total_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("病死"),
             # 某国的死亡病例数
             action=total_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("致死"),
             # 某国的死亡病例数
             action=total_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("重病"),
             # 某国的重病数
             action=total_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("严重"),
             # 某国的重病数
             action=total_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("危重"),
             # 某国的重病数
             action=total_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("重症"),
             # 某国的重病数
             action=total_severe),
         Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("输入"),
             # 某国的输入病例数
             action=total_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("外来"),
             # 某国的输入病例数
             action=total_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("境外"),
             # 某国的输入病例数
             action=total_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("外输"),
             # 某国的输入病例数
             action=total_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("国外"),
             # 某国的输入病例数
             action=total_input),


        ###################################################################################################

        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("感染"),
             # 各国的感染病例数
             action=every_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("患者"),
             # 各国的感染病例数
             action=every_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("患病"),
             # 各国的感染病例数
             action=every_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("染病"),
             # 各国的感染病例数
             action=every_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("可能") + W("感染"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("可能") + W("患者"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("可能") + W("患病"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("可能") + W("染病"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("疑似") + W("感染"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("疑似") + W("患者"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("疑似") + W("患病"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("疑似") + W("染病"),
             # 各国的疑似感染病例数
             action=every_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("治愈"),
             # 各国的治愈病例数
             action=every_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("治好"),
             # 各国的治愈病例数
             action=every_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("康复"),
             # 各国的治愈病例数
             action=every_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("痊愈"),
             # 各国的治愈病例数
             action=every_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("死亡"),
             # 各国的死亡病例数
             action=every_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("病死"),
             # 各国的死亡病例数
             action=every_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("致死"),
             # 各国的死亡病例数
             action=every_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("重病"),
             # 各国的重病数
             action=every_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("严重"),
             # 各国的重病数
             action=every_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("危重"),
             # 各国的重病数
             action=every_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("重症"),
             # 各国的重病数
             action=every_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("输入"),
             # 各国的输入病例数
             action=every_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("外来"),
             # 各国的输入病例数
             action=every_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("境外"),
             # 各国的输入病例数
             action=every_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("外输"),
             # 各国的输入病例数
             action=every_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W("国外"),
             # 各国的输入病例数
             action=every_input),


        ###################################################################################

        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("感染"),
             # 各国的新增感染病例数
             action=everyday_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("患者"),
             # 各国的新增感染病例数
             action=everyday_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("患病"),
             # 各国的新增感染病例数
             action=everyday_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("染病"),
             # 各国的新增感染病例数
             action=everyday_confirm),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("感染"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("患者"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("患病"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("可能") + W("染病"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("感染"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("患者"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("患病"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("疑似") + W("染病"),
             # 各国的新增疑似感染病例数
             action=everyday_suspect),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("治愈"),
             # 各国的新增治愈病例数
             action=everyday_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("治好"),
             # 各国的新增治愈病例数
             action=everyday_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("康复"),
             # 各国的新增治愈病例数
             action=everyday_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("痊愈"),
             # 各国的新增治愈病例数
             action=everyday_heal),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("死亡"),
             # 各国的新增死亡病例数
             action=everyday_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("病死"),
             # 各国的新增死亡病例数
             action=everyday_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("致死"),
             # 各国的新增死亡病例数
             action=everyday_dead),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("重病"),
             # 各国的新增重病数
             action=everyday_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("严重"),
             # 各国的新增重病数
             action=everyday_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("危重"),
             # 各国的新增重病数
             action=everyday_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("重症"),
             # 各国的新增重病数
             action=everyday_severe),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("输入"),
             # 各国的新增输入病例数
             action=everyday_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("外来"),
             # 各国的新增输入病例数
             action=everyday_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("境外"),
             # 各国的新增输入病例数
             action=everyday_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("外输"),
             # 各国的新增输入病例数
             action=everyday_input),
        Rule(condition=W(pos='na') + Star(Any(), greedy=False) + W('新增') + W("国外"),
             # 各国的新增输入病例数
             action=everyday_input),

#########################################################################################################

        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("感染") + W('数') + W('最多'),
             # 哪个国家的感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("患者") + W('数') + W('最多'),
             # 哪个国家的感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("患病") + W('数') + W('最多'),
             # 哪个国家的感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("染病") + W('数') + W('最多'),
             # 哪个国家的感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("感染") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("患者") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("患病") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("可能") + W("染病") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("感染") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("患者") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("患病") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("疑似") + W("染病") + W('数') + W('最多'),
             # 哪个国家的疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("治愈") + W('数') + W('最多'),
             # 哪个国家的治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("治好") + W('数') + W('最多'),
             # 哪个国家的治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("康复") + W('数') + W('最多'),
             # 哪个国家的治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("痊愈") + W('数') + W('最多'),
             # 哪个国家的治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("死亡") + W('数') + W('最多'),
             # 哪个国家的死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("病死") + W('数') + W('最多'),
             # 哪个国家的死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("致死") + W('数') + W('最多'),
             # 哪个国家的死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("重病") + W('数') + W('最多'),
             # 哪个国家的重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("严重") + W('数') + W('最多'),
             # 哪个国家的重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("危重") + W('数') + W('最多'),
             # 哪个国家的重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("重症") + W('数') + W('最多'),
             # 哪个国家的重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("输入") + W('数') + W('最多'),
             # 哪个国家的输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("外来") + W('数') + W('最多'),
             # 哪个国家的输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("境外") + W('数') + W('最多'),
             # 哪个国家的输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("外输") + W('数') + W('最多'),
             # 哪个国家的输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("国外") + W('数') + W('最多'),
             # 哪个国家的输入病例数最多
             action=max_input),




#########################################################################################################

        Rule(condition=W(pos='nr') + Star(Any(), greedy=False) + W("新增") + W("感染") + W('数') + W('最多'),
             # 哪个国家的新增感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("患者") + W('数') + W('最多'),
             # 哪个国家的新增感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("患病") + W('数') + W('最多'),
             # 哪个国家的新增感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("染病") + W('数') + W('最多'),
             # 哪个国家的新增感染病例数最多
             action=max_confirm),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("可能") + W("感染") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("可能") + W("患者") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("可能") + W("患病") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("可能") + W("染病") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("疑似") + W("感染") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("疑似") + W("患者") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("疑似") + W("患病") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("疑似") + W("染病") + W('数') + W('最多'),
             # 哪个国家的新增疑似感染病例数最多
             action=max_suspect),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("治愈") + W('数') + W('最多'),
             # 哪个国家的新增治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("治好") + W('数') + W('最多'),
             # 哪个国家的新增治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("康复") + W('数') + W('最多'),
             # 哪个国家的新增治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("痊愈") + W('数') + W('最多'),
             # 哪个国家的新增治愈病例数最多
             action=max_heal),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("死亡") + W('数') + W('最多'),
             # 哪个国家的新增死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("病死") + W('数') + W('最多'),
             # 哪个国家的新增死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("致死") + W('数') + W('最多'),
             # 哪个国家的新增死亡病例数最多
             action=max_dead),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("重病") + W('数') + W('最多'),
             # 哪个国家的新增重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("严重") + W('数') + W('最多'),
             # 哪个国家的新增重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("危重") + W('数') + W('最多'),
             # 哪个国家的新增重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("重症") + W('数') + W('最多'),
             # 哪个国家的新增重病数最多
             action=max_severe),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("输入") + W('数') + W('最多'),
             # 哪个国家的新增输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("外来") + W('数') + W('最多'),
             # 哪个国家的新增输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("境外") + W('数') + W('最多'),
             # 哪个国家的新增输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("外输") + W('数') + W('最多'),
             # 哪个国家的新增输入病例数最多
             action=max_input),
        Rule(condition=W(pos='nr') + Star(Any(),  greedy=False) + W("新增") + W("国外") + W('数') + W('最多'),
             # 哪个国家的新增输入病例数最多
             action=max_input),

###################################################################################################

        Rule(condition=W("感染") + Star(Any(), greedy=False) + W(pos="m") ,
             # 某地的感染人数最多
             action=select_confirm),
        Rule(condition=W("治愈") + Star(Any(), greedy=False) + W(pos="m") ,
             # 某地的治愈人数最多
             action=select_heal),
        Rule(condition=W("死亡") + Star(Any(), greedy=False) + W(pos="m") ,
             # 某地的死亡人数最多
             action=select_dead),
        Rule(condition=W("疑似") + Star(Any(), greedy=False) + W(pos="m"),
             # 某地的疑似人数最多
             action=select_suspect),
        Rule(condition=W("严重") + Star(Any(), greedy=False) + W(pos="m"),
             # 某地的严重人数最多
             action=select_severe),
        Rule(condition=W("输入") + Star(Any(), greedy=False) + W(pos="m"),
             # 某地的输入人数最多
             action=select_input),
    ]

    # matching and querying
    for seg in seg_lists:
        # display question each
        for s in seg:
            print(s.token, )
            print(s.pos)   

        for rule in rules:
            query = rule.apply(seg)

            if query is None:
                #print("Query not generated :(\n")
                continue

            # display corresponding query
            # print(query)

            if query:
                sparql_base.setQuery(query)
                sparql_base.setReturnFormat(JSON)
                results = sparql_base.query().convert()

                if not results["results"]["bindings"]:
                    print("No answer found :(")
                    print
                    continue
                if (question[0]=='各'):
                 for result in results["results"]["bindings"]:
                     print("Result: "), print(result["X"]["value"]), print(result["Z"]["value"])

                     print
                else:
                 for result in results["results"]["bindings"]:
                     print("Result: "), print(result["X"]["value"])
                      
                     print
                 break
