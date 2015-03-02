import webapp2


application = webapp2.WSGIApplication([

	('/service', 'service.Service'), 
	('/cat', 'cat.Cat'),
	(r'/service/search', 'service.ServSearch'),
	(r'/provider', 'provider.Provider'),
	(r'/provider/search', 'provider.ProvSearch'),
	(r'/', 'front.Front'), 
], debug=True)
 
application.router.add(webapp2.Route(r'/service/<id:[0-9]+><:/?>', 'service.Service')) 
application.router.add(webapp2.Route(r'/provider/<id:[0-9]+><:/?>', 'provider.Provider')) 
application.router.add(webapp2.Route(r'/provider/<pid:[0-9]+>/service/<sid:[0-9]+><:/?>', 'provider.ServiceAdd'))
application.router.add(webapp2.Route(r'/provider/remove/<id:[0-9]+><:/?>', 'provider.ProviderDelete')) 


#gets service by id number
#app.router.add(webapp2.Route(r'/channel/<cid:[0-9]+>/mod/<mid:[0-9]+><:/?>', 'channel.ChannelMods'))
#app.router.add(webapp2.Route(r'/mod/<id:[0-9]+><:/?>', 'mod.Mod'))

#searches services
#app.router.add(webapp2.Route(r'/service/search', 'service.ServSearch')) 
#get or post to view or add providers
#app.router.add(webapp2.Route(r'/provider', 'provider.Provider')) 
#searches providers
#app.router.add(webapp2.Route(r'/provider/search', 'provider.ProvSearch')) 
#get providers by id number and associated services 
#app.router.add(webapp2.Route(r'/provider/<id:[0-9]+>/service/<sid:[0-9]+><:/?>', 'provider.ProviderServices'))

#(r'/service/<id:[0-9]+><:/?>', 'service.Service'),
	#(r'/provider/<id:[0-9]+>/service/<sid:[0-9]+><:/?>', 'provider.ProvServices'),
	#('/', 'helloworld.MainPage'),