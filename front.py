import webapp2
import os 

class Front(webapp2.RequestHandler):
    def get(self):
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.write("Web Based API for Health Resource Database\n\n")
			self.response.write("Database Resource Functions:\n")
			self.response.write("Provides application/json output\n")
			self.response.write("List of Services: /service\n")
			self.response.write("List of Providers: /provider\n")
			self.response.write("Specific Service: /service/<id #>\n")
			self.response.write("Specific Provider: /provider/<id #>\n")
			self.response.write("Search Provider by Name or County: /provider/search\n")
			self.response.write("Search Provider by Service Name: /service/search\n\n")
			self.response.write("Database Management Functions:\n")
			self.response.write("Add Provider: (POST) /provider\n")
			self.response.write("Add Service: (POST) /service\n")
			self.response.write("Add Service to Existing Provider: /provider/<id #>/service/<id #>\n")
			self.response.write("Remove Provider: /provider/remove/<id #>\n")
			
