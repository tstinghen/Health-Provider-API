import webapp2
import time
import os 

class MainPage(webapp2.RequestHandler):
    def get(self):
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write("Hey check this out...\n")
			self.response.write(time.strftime("\n\n%a, %b %d %Y \n%H:%M %p\n\n", time.localtime()))
			self.response.write("That's your local time, right? \nMaybe? \n\nWell it's somebody's local time anyway. \nPretty dynamic, right??")
			

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
