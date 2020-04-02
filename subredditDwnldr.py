#imports
import praw
import urllib
import random 

#starts reddit instance
reddit = praw.Reddit(client_id='ahwtOvFXN8A7Ow',
                     client_secret='Hi1QFtY_oBBtzjNNQCl11vHsNEQ',
                     user_agent='DJ-Bluntz')

print(reddit.read_only) 
"""
except:
	print("Oops! Couldn't connect to Reddit. Check the client info and your wifi.")
#output: true (connection to reddit established)
"""
#imputs
sub = raw_input('What sub should I search? --->  ')
imgcount_request = raw_input('How many pictures do you want? --->  ')
keyword = raw_input('Enter keyword --->  ')
folder = raw_input('What folder do you want me to save to? --->  ')
filename_request = raw_input('What should the images be named? --->  ')


def dwnldr():
	imgcount = 0
	for submission in reddit.subreddit(sub).top(limit = 999999):
		if imgcount < int(imgcount_request):
			if keyword in submission.title:
				print(submission.title)
				url = submission.url
				filename = filename_request + str(random.randint(0,1000)) + '.jpg'
				try:
					urllib.urlretrieve(url, '/home/nathanielptaylor/' + folder + '/' + filename)
					imgcount = imgcount + 1
					print('That was image number ' + str(imgcount) + ' of ' + imgcount_request)
				except:
					print('Download Failed! ):')
function = dwnldr()
print('All Done! :)')