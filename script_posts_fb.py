# Chap04/facebook_get_page_posts.py
import os
import json
from argparse import ArgumentParser
import facebook
import requests

empresas = ['claroecua', 'movistarecu', 'marathonsportsec', 'cntecuador',
            'chevroletecuador', 'cocacolaec', 'directvla', 'latamecuador',
            'quicentroshopping', 'sanmarinogye', 'galletasamorecuador', 'nescafe.ec',
            'almacenesdeprati', 'tiaec', 'bancoguayaquil', 'bancopacificoec',
            'bancobolivariano', 'kfcecuador', 'mcdonaldsecuador', 'bancopichinchaecuador',
            'NissanEcuador', 'pronacatqma', 'aviancaenecuador', 'cinemarkecuador',
            'supercines', 'pilsenerec', 'clubpremiumec', 'grupotvcableec',
            'netlife.ecuador', 'pepsiecuador', 'yanbal.ec', 'huaweimobileec', 
            'univisate', 'papajohnsecuador', 'JuanValdezCafeEcuador', 'DominosPizzaEcuador',
            'ElCafedeTere']

for empresa in empresas:
    
    if __name__ == '__main__':
        
        token = "EAAEvpZAMUVr0BAOkMMEhoEVqCigtMZC8Kd1MBoyCRefxRdXZBtHma3PS96OyZAgqJoWRZAF75JKFJpua0cH8aejYJXb2sAT76FbFqFkCwQ3cfohI6guay8R1RI4IrU5pW0G3q7CPDBeEwWDT0U8Twx9BFwzVKSY3481fT7nQGi5OLmXozL2T6mcGd0uiDlQzeMC9Kaxhz1QZDZD"
        
        graph = facebook.GraphAPI(token)
        all_fields = [
          'id',
        	'message',
        	'created_time',
        	'shares',
        	'likes.summary(true)',
        	'comments.summary(true)']
        	
        all_fields = ','.join(all_fields)
        posts = graph.get_connections(empresa, 'posts', fields=all_fields)
        
        downloaded = 0
        
        while True:  # keep paginating
            if downloaded >= 5000:
                break
            try:
                fname = "posts_{}.jsonl".format(empresa)
                with open(fname, 'a') as f:
                    for post in posts['data']:
                        downloaded += 1
                        f.write(json.dumps(post)+"\n")
                    # get next page
                    posts = requests.get(posts['paging']['next']).json()
            except KeyError:
            	# no more pages, break the loop
                break
