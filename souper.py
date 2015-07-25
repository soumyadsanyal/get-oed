from bs4 import BeautifulSoup
import urllib2
import sys


def result(i):
	
	query='http://oxforddictionaries.com/us/definition/american_english/'+i.lower()+'?q=++'+i.capitalize()
	try:
		response=urllib2.urlopen(query)
		html=response.read()
		return html
	except urllib2.HTTPError, e:
		print query, e
	



def returndefex(word):
 soup=BeautifulSoup(result(word))
 parts=soup.find_all(name='span',attrs={'class':'partOfSpeech'})
 definitions=soup.find_all(name='span',attrs={'class':'definition'})
 examples=soup.find_all(name='span',attrs={'class':'exampleGroup exGrBreak'})
 return parts, definitions, examples

def read_from_file(infile):
 read_data=[]
 with open(infile,'r') as f:
  read_data=f.readlines()
 words=[]
 for i in read_data:
  if (i != '' and i != '\n'):
   words.append(i.strip())
 return words

def transform(words):
 result=[]
 for i in words:
  result.append(i)
  result.append(returndefex(i))
 return result

def write_to_output(outfile, result):
 with open(outfile,'w') as f:
  for i in result:
   f.write(str(i))





