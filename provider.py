import webapp2 
from google.appengine.ext import ndb 
import db_defs 
import json 

#code adapted from CS 496 Week 4 lecture video 

class Provider(webapp2.RequestHandler): 
	def post(self): 
	#creates a Service entity 
		self.response.write("Accessing POST variable") 
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
			
		new_provider = db_defs.Provider()
		name = self.request.get('name', default_value = None)
		contact = self.request.get('contact', default_value = None) 
		county = self.request.get('county', default_value = None) 
		services = self.request.get_all('services[]', default_value = None) 
		
		 
		if name: 
			new_provider.name = name 
		else: 
			self.response.status = 400 
			self.response.status_message = "Invalid Request, Name is Required" 
		if contact: 
			new_provider.contact = contact
		else: 
			self.response.status = 400 
			self.response.status_message = "Invalid Request, Contact Info is Required" 
		if services: 
			for serv in services: 
				new_provider.services.append(ndb.Key(db_defs.Service, int(serv)))
		
		if county: 
			new_provider.county = county
		else: 
			self.response.status = 400 
			self.response.status_message = "Invalid Request, County is Required" 
		
		key = new_provider.put() 
		out = new_provider.to_dict() 
		self.response.write(json.dumps(out)) 
		return 
	
	def get(self, **kwargs): 	
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
		if 'id' in kwargs: 
			out = ndb.Key(db_defs.Provider, int(kwargs['id'])).get()
			if not out: 
				self.response.status_message = "ID invalid" 
				return
			out = out.to_dict() 
			self.response.write(json.dumps(out)) 
		else:
			# q = db_defs.Provider.query() 
			# keys = q.fetch() 
			# results = {}
			# for k in keys:
				# id = db_defs.Model.to_dict(k)
				# results = {'name': k.name, 'id': id}
			# self.response.write(json.dumps(results)) 
			
			q = db_defs.Provider.query() 
			provs = q.fetch()
			for p in provs: 
				results = {'id' : p.key.id(), 'name' : p.name} 
				self.response.write(json.dumps(results)) 
	
class ProvSearch(webapp2.RequestHandler): 
	def post(self):
		# search for providers 
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
			
		q = db_defs.Provider.query() 
		if self.request.get('name', None): 
			q = q.filter(db_defs.Provider.name == self.request.get('name')) 
		if self.request.get('county', None): 
			q = q.filter(db_defs.Provider.county == self.request.get('county'))	
		
		provs = q.fetch()
		for p in provs: 
			results = {'id' : p.key.id(), 'name' : p.name} 
			self.response.write(json.dumps(results)) 
			
class ServiceAdd(webapp2.RequestHandler): 
	def put(self, **kwargs): 
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 
			
		if 'pid' in kwargs: 	
			prov_id = ndb.Key(db_defs.Provider, int(kwargs['pid'])).get() 	
			if not prov_id: 
				self.response.status = 404 
				self.response.status_message = "Provider ID not found" 
				return 
				
		if 'sid' in kwargs: 	
			serv_id = ndb.Key(db_defs.Service, int(kwargs['sid']))	
			if not serv_id: 
				self.response.status = 404 
				self.response.status_message = "Service ID not found" 
				return 
		if serv_id not in prov_id.services: 
			prov_id.services.append(serv_id) 
			prov_id.put() 
			self.response.write(json.dumps(prov_id.to_dict()))
			
			
class ProviderDelete(webapp2.RequestHandler): 
	def delete(self, **kwargs): 
	
		if 'application/json' not in self.request.accept: 
			self.response.status = 406 
			self.response.status_message = "API only supports json type" 
			return 	
		
		if 'id' in kwargs: 
			prov_id = ndb.Key(db_defs.Provider, int(kwargs['id'])).get() 
		
			if not prov_id: 
				self.response.status = 404 
				self.response.status_message = "Provider ID not found" 
				return 
			
			prov_id.key.delete()
		 
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
		