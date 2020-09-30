from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from configparser import ConfigParser
from flask_httpauth import HTTPBasicAuth
from threading import Lock

conffile = 'app.conf'

def ParseConfig(section, param, filename=conffile):
	# create a parser
	parser = ConfigParser()
	
	# read config file
	parser.read(filename)

	# get section, default to postgresql
	if parser.has_section(section):
		params = parser.items(section)
		for p in params:
			if p[0] == param:
				return p[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, filename))

	return None

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ParseConfig('database', 'url')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#allows cross-domain call
CORS(app)

database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

FlaskAPI = Api(app)

auth = HTTPBasicAuth()