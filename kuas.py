#! /usr/bin/python3


 Here for person A

import requests
from lxml import etree

def getlist():
	url = 'http://academic.kuas.edu.tw/bin/home.php'
	News = list()
	s = requests.session()
	r = s.get( url )
	
	# Set The response's encoding
	r.encoding = 'utf-8'
	
	tree = etree.HTML( r.text )
	bulletin_table = tree.xpath( '//table[@summary="list"]//a[@title]' )
	for t in bulletin_table:
		News.append( [ t.text, t.attrib[ 'href' ] ] )

	return News


"""
# Here for person B

if num >= 0 and num < len( News ):
		print( 'Title: %s' % News[ num ][ 0 ] )
		if 'academic.kuas.edu.tw' in News[ num ][ 1 ]:
			getcontent( News[ num ][ 1 ] )
		else:
			print( 'Link is not in this domain' )
	else:
		print( 'Please input a valid number !' )
"""
