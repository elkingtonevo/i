from bottle import route, hook, response, run
import random

words = tuple(set(map(lambda x:x.lower().strip(), open('words.txt').read().splitlines())))

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/')
def index():
	r = random.choice(words)
	template = "<html><head><meta charset=utf-8 /><title>names</title><script src='//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'></script><script src='quojs.js'></script><link href='//fonts.googleapis.com/css?family=Bitter:700' rel='stylesheet' type='text/css'><link rel='stylesheet' type='text/css' href='index.css'><script src='index.js'></script></head><body> <div id='suggestion'>" + r + "</div></body><!-- Source code and full word list can be found at github.com/hashme/burgundy --></html>"
	return template

run(host = '0.0.0.0', port = 8080, server = 'tornado')