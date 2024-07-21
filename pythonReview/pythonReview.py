likes = 0
dislikes = 0
def create_youtube_video(title, description):
	youtubevideo = {'title': title, 'description': description, 'dislikes':dislikes, 'likes' :likes , 'comments':{}}
	return youtubevideo

def like(youtubevideo):
	if 'likes' in youtubevideo:
		likes = likes+1
	return youtubevideo

def dislike(youtubevideo):
	if 'dislikes' in youtubevideo:
		dislikes = dislikes+1
	return youtubevideo

def add_comment(youtubevideo,username,comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

#i didn't understand 6 



