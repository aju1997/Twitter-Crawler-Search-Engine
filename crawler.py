import json
import tweepy
import requests
import os
from bs4 import BeautifulSoup, SoupStrainer

# http://docs.tweepy.org/en/v3.5.0/index.html
consumerKey = "TRmC2p0y2lzmpUvUssZIlxMrh"
consumerSecret = "ooM6DzAeO46G24Tzvne9OxlphqCNk3K2TUZzMg8I9RTnKYRA56"
accessToken = "3302119946-j1D4vtOJnWgQAlBVQDXc7PYbmo2BFIZhOykWA1m"
accessTokenSecret = "BuNSiUEPjTLnk9ub56gUKaJUU1zkpvXN2oTl1kjzuwdaS"

# Creating the authentication object 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
# Setting your access token and secret
auth.set_access_token(accessToken, accessTokenSecret)
# Creating the API object while passing in auth information
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#class
class Tweet(tweepy.StreamListener):
      def on_status(self, status):
         try:
            with open('tweets.json', 'a') as file:
               dumpContents = json.dumps(status._json)
               loadContents = json.loads(dumpContents)
               if (status.user.geo_enabled): #checks if user has geolocation as true
                  for contents in status.entities["urls"]:
                     # print url
                     url = contents["expanded_url"]
                     try:
                        # HTTP get request for the URL
                        r = requests.get(url)
                     except:
                        continue
                     # specifies what to parse, in this case it is the title
                     urlTitle = SoupStrainer("title")
                     # parsed HTML document for the urlTitle
                     soup = BeautifulSoup(r.text, "html.parser", parse_only = urlTitle)
                     # grabs the title from the HTML parser
                     title = soup.title.string
                     # adds the title along with all the other information in the tweet
                     loadContents.update({"url_title: ": title})
                     #dumps the loadContents into the json file
					 string = '{"index":	{"_index":"tweets", "_type":"tweets", "_id":' + str(status.id) + '}}\n'
                     file.write(string)
                     json.dump(loadContents, file)
                     file.write('\n')
                  return True
         # Allows us to skip the tweets where we get either permission denied or NoneType error
         # since it allows the program to continue on even after the error
         except BaseException as error:
            print ("Error on status: %s" %str(error))
            return True
      # error
      def error(self, status):
         print(status)
         return True
      # timeout
      def timeout(self):
         return True
      # handles ProtocolError('Connection broken: %r' % e, e)
      def on_exception(self, exception):
         print(exception)
         return True
         
if __name__ == '__main__':
   # Using the authentication from above and our Tweet class to store the stream into tweets
   tweets = tweepy.Stream(auth=api.auth, listener=Tweet())
   # Filter the tweets with language as English and with keywords
	twitter_stream.filter(languages=["en"], stall_warnings=True, track=["Politics", "NBA", "Roland Garros", "Pokemon", "Meme", "America", "Japan", "Anime", "Tony Stark", "Iron Man", "Sansa Stark", "Jon Snow", "Targaryen"])