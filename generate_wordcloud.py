#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from wordcloud import WordCloud

def generate_wordcloud(text):
	cloud = WordCloud(max_font_size=40).generate(text)
	return cloud