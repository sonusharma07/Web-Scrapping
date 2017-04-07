# -*- coding: utf-8 -*-
"""


@author: sonu sharma
"""
import re
import requests
from lxml import html
page = requests.get('http://www.imdb.com/search/title?count=100&release_date=2016,2016&title_type=feature')
tree = html.fromstring(page.content)

#title = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "header", " " ))]/text()')
#index = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text-primary", " " ))]/text()')
#name = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "lister-item-header", " " ))]//a/text()')
#runtime = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "runtime", " " ))]/text()')


#rate = tree.xpath('//strong/text()')

#desc = tree.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "ratings-bar", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "text-muted", " " ))]/text()')
#genre  = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "genre", " " ))]/text()')
#data preprocessing keeping only one genre

#one_genre = "".join([re.sub(",.*","",str) for str in genre])

#direct = tree.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "text-muted", " " ))]//p//a[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]/text()')
#votes = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sort-num_votes-visible", " " ))]//span[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
#no_cma_votes = []
#no_cma_votes = "\n".join([re.sub(",","",str) for str in votes])
#actors = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "lister-item-content", " " ))]//*+[contains(concat( " ", @class, " " ), concat( " ", "ghost", " " ))]//a/text()')
#gross = tree.xpath('//*+[contains(concat( " ", @class, " " ), concat( " ", "ghost", " " ))]//*+span[contains(concat( " ", @class, " " ), concat( " ", "text-muted", " " ))]/text()')




index = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "text-primary", " " ))]/text()')
name = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "lister-item-header", " " ))]//a/text()')

runtime = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "runtime", " " ))]/text()')
del runtime[0]
# remo min from
no_min_run = [re.sub("min","",str) for str in runtime]


metascr = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "metascore", " " ))]/text()')
#since some of the metascore values are missing 
for i in [99,84,83,69,47,45,33]:
    metascr.insert(i,"NA")

#removw coms out
votes = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "sort-num_votes-visible", " " ))]//span[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]/text()')
no_cma_votes = []
no_cma_votes = [re.sub(",","",str) for str in votes]

#keeping only the one genre
genre  = tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "genre", " " ))]/text()')
#data preprocessing keeping only one genre
one_genre = [re.sub(",.*","",str) for str in genre]
clean_genre = [re.sub("\n","",str) for str in one_genre]
#cheking for length
"""
print(len(index))
print(len(name))
print(len(runtime))
print(len(metascr))
print(len(no_cma_votes))
print(len(one_genre))
"""

from IPython.core.display import display,HTML
import pandas as pd
df = pd.DataFrame(index,columns=['No'])
df['name'] = name
df['runtime/min'] = no_min_run
df['metascore'] = metascr
df['votes'] = no_cma_votes
df['genre'] = clean_genre
#print(df.head())
display(df.head())
#display(HTML(df.to_html()))
#display(HTML('<h3> hi i am </h3>'))
df.to_csv('imbd.csv', sep='\t', encoding='utf-8')