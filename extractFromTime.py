import requests

def getSubString(data, start_str, end_str, next_index = 0):
	start_sec = data.index(start_str, next_index)
	end_sec = data.index(end_str, start_sec)
	return data[start_sec+len(start_str):end_sec].strip()

def getEachStory(data):
	link_begin = "href="
	link_end = "/>"
	title_end = "</a>"
	link = "https://time.com" + getSubString(data, link_begin, link_end)
	title = getSubString(data, link_end, title_end)
	return {"title": title, "link": link}

def getStories(data):
	story_begin = "<a "
	story_end = "</h2>"
	result = []
	next_index = -1
	while 1:
		story_data = ""
		next_index = data.find(story_begin, next_index+1)
		if(next_index > -1):
			story_data = getSubString(data, story_begin, story_end, next_index)
			result += [getEachStory(story_data)]
		else:
			break
	return result

def getLatestStories(URL):
	resp = requests.get(url = URL)  # hit url
	data = resp.text
	sec_begin = "<section class=\"homepage-module latest\" data-module_name=\"Latest Stories\">"
	sec_end = "</section>"
	sec_data = getSubString(data, sec_begin, sec_end)
	return getStories(sec_data)

if __name__ == '__main__':
	url = "https://time.com"
	print(getLatestStories(url))