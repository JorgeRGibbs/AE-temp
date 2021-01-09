from http.server import test, SimpleHTTPRequestHandler, HTTPServer

'''
#MODULE OPTIONS
	config  = Config({
	        Option(
	            'PORT',
	            "Set to an integer to choose which port to use on web server.",
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ):  80,
			Option(
	            'A',
	            "",
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): " ",
	    })
'''
if __name__ == '__main__':
	#main()
	httpd = HTTPServer(('localhost',8000),SimpleHTTPRequestHandler)
	httpd.serve_forever()