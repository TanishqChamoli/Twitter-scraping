import twint

def key_search(keyword):
	c = twint.Config()
	key = keyword
	c.Search = key
	
	c.Hide_output = True
	c.Limit = 100
	c.Store_object = True

	twint.run.Search(c)
	tweets = [x.__dict__ for x in twint.output.tweets_list]
	twint.output.tweets_list = []

	print(key)
	return tweets

if __name__=="__main__":
	key_search("modi")