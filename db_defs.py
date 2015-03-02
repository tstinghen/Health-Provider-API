from google.appengine.ext import ndb 

class Model(ndb.Model): 
	def to_dict(self): 
		d = super(Model, self).to_dict() 
		d['key'] = self.key.id() 
		return d

	
class Service(Model):
	name = ndb.StringProperty(required = True) 
	description = ndb.StringProperty(required = True)
	
class Provider(Model): 
	name = ndb.StringProperty(required = True)
	#for usable API, contact broken down into: 
	#contact name, phone number, email, website 
	#street address, but for ease of implementation
	#only using one field for now. 
	contact = ndb.StringProperty(required = True)
	county = ndb.StringProperty(required = True)
	services = ndb.KeyProperty(repeated = True) 
	 
	def to_dict(self): 
		d = super(Provider, self).to_dict() 
		d['services'] = [s.id() for s in d['services']]
		return d
		
class Individual(Provider): 
	organization = ndb.KeyProperty

class Cat(Model): 
	name = ndb.StringProperty(required = True)
	color = ndb.StringProperty(required = True)
	nap_spot = ndb.StringProperty(required = True)