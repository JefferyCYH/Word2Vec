# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:14:55 2019

@author: cai
"""
import gensim
from gensim.models import Word2Vec

en_wiki_word2vec_model=Word2Vec.load('wiki.zh.model')

testwords =['孩子','数学','学术','白痴','篮球']
for i in range(5):
    res = en_wiki_word2vec_model.most_similar(testword[i])
    print(res)
    
    sim1=model.similarity(u'勇敢',u'战斗')
    sim2=model.similarity(u'勇敢',u'胆小')
    sim3=model.similarity(u'高兴',u'开心')
    sim4=model.similarity(u'伤心',u'开心')
    print(sim1)
    print(sim2)
    print(sim3)
    print(sim4)
    
    list1=[u'今天',u'我',u'很',u'开心']
     list2=[u'空气',u'清新',u'善良',u'开心']
      list3=[u'国家电网',u'再次',u'宣告',u'破产','重新']
      list_sim1=model.n_similarity(list1,list2)
      print(list_sim1)
      list_sim2=model.n_similarity(list1,list3)
      print(list_sim2)
      
       list=[u'纽约',u'北京',u'上海',u'西安']
      print(model.doesnt_match(list))
       list=[u'纽约',u'北京',u'上海',u'西瓜']
       print(model.doesnt_match(list))