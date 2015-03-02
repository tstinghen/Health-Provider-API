import webapp2 
from google.appengine.ext import ndb 
import db_defs 
import json 

#code adapted from CS 496 Week 4 lecture video 


#curl -- data = "name=test" -H "Accept: application/json" http://localhost:11080/service
class Service(webapp2.RequestHandler): 
	def post(self): 
	#creates a Service entity 
		self.response.write("Accessing POST variable") 
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
			
		new_service = db_defs.Service()
		name = self.request.get('name', default_value = None)
		descrip = self.request.get('description', default_value = None) 
		 
		if name: 
			new_service.name = name 
		else: 
			self.response.status = 400 
			self.response.status_message = "Invalid Request, Name is Required" 
		if descrip: 
			new_service.description = descrip 
		slist = [] 
		key = new_service.put() 
		out = new_service.to_dict() 
		slist.append(out)
		self.response.write(json.dumps(slist)) 
		
		return 
	
	def get(self, **kwargs): 	
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
		if 'id' in kwargs: 
			out = ndb.Key(db_defs.Service, int(kwargs['id'])).get().to_dict() 
			self.response.write(json.dumps(out)) 
		else:
			q = db_defs.Service.query() 
			servs = q.fetch()
			slist = []
			for s in servs: 
				results = {'id' : s.key.id(), 'name' : s.name, 'description': s.description} 
				slist.append(results)
			results = {'services' : slist} 
			self.response.write(json.dumps(results)) 
	
class ServSearch(webapp2.RequestHandler): 
	def post(self):
		# search for services 
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
			
		q = db_defs.Service.query() 
		q = q.filter(db_defs.Service.name == self.request.get('name')) 
		serv_key = q.fetch(keys_only = True) 
		
		q2 = db_defs.Provider.query() 
		q2 = q2.filter(db_defs.Provider.services == serv_key[0])
		provs = q2.fetch()
		
		plist = []
		for p in provs: 
			results = {'id' : p.key.id(), 'name' : p.name, 'contact' : p.contact, 'county': p.county} 
			plist.append(results)
		results = {'providers' : plist} 
		self.response.write(json.dumps(results)) 
			
		