import requests
import re

def getLatestStories(URL):
	result = []
	resp = requests.get(url = URL)  # hit url
	data = resp.text				# store the html data in a variable

	latest = re.findall(r'<section class=\"homepage-module latest\" data-module_name=\"Latest Stories\">((.|\n)*?)<\/section>', data)[0]

	stories = re.findall(r'<a ((.|\n)*?)<\/h2>', str(latest))

	for story in stories:
		sto = {}
		ref = re.findall(r'href=((.|\n)*?)\/>', str(story))
		heads = re.findall(r'\/>((.|\n)*?)<\/a>', str(story))
		sto["title"] = heads[0][0]
		sto["link"] = URL+ref[0][0]
		result += [sto]

	return result

if __name__ == '__main__':
	url = "https://time.com"
	print(getLatestStories(url))