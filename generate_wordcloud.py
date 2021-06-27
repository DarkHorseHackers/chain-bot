#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from wordcloud import WordCloud, STOPWORDS

stopwords = set(STOPWORDS)
stopwords.add("http")
stopwords.add("https")

def generate_wordcloud(text):
	cloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
	return cloud