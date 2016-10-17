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



# Here for person B

def getcontent( url ):
	s = requests.session()
	r = s.get( url )
	r.encoding = 'utf-8'
	tree = etree.HTML( r.text )
	content_div = tree.xpath( '//div[@class="ptcontent clearfix floatholder"]' )[ 0 ]
	string = "".join( [ x for x in content_div.itertext() ])
	for s in string.split( '\n' ):
		if not s.strip() == "":
			print( s )

# Here for person A again

if __name__ == '__main__':
	News = getlist()
	print( 'No.\tTitle' )
	print( '=' * 50 )
	for i in range( len( News ) ):
		print( '%s\t%s' % ( i, News[ i ][ 0 ] ) )	
	print( '=' * 50 )

	num = input( 'Please input number: ' )
	num = int( num )
	
	if num >= 0 and num < len( News ):
		print( 'Title: %s' % News[ num ][ 0 ] )
		if 'academic.kuas.edu.tw' in News[ num ][ 1 ]:
			getcontent( News[ num ][ 1 ] )
		else:
			print( 'Link is not in this domain' )
	else:
		print( 'Please input a valid number !' )
121234556789123456789
