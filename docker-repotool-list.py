#!/usr/bin/env python
#
import requests 
from requests.auth import HTTPBasicAuth
import os
import sys
import json


def catalogs_repositories_tags_data():

	docker_registry_api_url = os.environ.get('DOCKER_REGISTRY_API_URL', None)
	if docker_registry_api_url is None:
		print("A required environment variable 'DOCKER_REGISTRY_API_URL' is not set. Enter the desired URL.", file=sys.stderr)
		sys.exit(1)

	login_user= os.environ.get('LOGIN_USER', None)
	if login_user is None:
		print("A required environment variable 'LOGIN_USER' is not set. Enter the desired LOGIN.", file=sys.stderr)
		sys.exit(2)
	
	password_user= os.environ.get('PASSWORD_USER', None)
	if password_user is None:
		print("A required environment variable 'PASSWORD_USER' is not set. Enter the desired PASSWORD.", file=sys.stderr)
		sys.exit(3)

	try:
		credentials = HTTPBasicAuth(login_user, password_user)
		catalog_url = docker_registry_api_url + "/v2/_catalog"
		catalog_response = requests.get(catalog_url, auth = credentials)
		catalog_repositories_content = catalog_response.json()
		mass_catalog_repositories_content = catalog_repositories_content['repositories']
		
		for repo_name in mass_catalog_repositories_content:
			data_tags_url= docker_registry_api_url + "/v2/%s/tags/list" % repo_name
			tags_data_response = requests.get(data_tags_url, auth = credentials)
			data_tags_repositories_content = tags_data_response.json()
			catalog_name = data_tags_repositories_content['name']
			
			for tag_name in data_tags_repositories_content['tags']:
				time_url = docker_registry_api_url + "/v2/%s/manifests/%s" % (catalog_name, tag_name)  
				time_response = requests.get(time_url, auth = credentials)
				time_repositories_content = time_response.json()
				time_repositories = time_repositories_content['history']
				dict_time_repositories = time_repositories[0]
				dict_tags_repositories = tags_time_repositories['v1Compatibility']
				data_time_repositories = json.loads(dict_tags_repositories)
				tag_date = data_time_repositories['created']
				print(catalog_name+'/'+tag_name, tag_date)
		
	except Exception as ex:
		print("Attempt failure. {0}".format(ex), file=sys.stderr)

catalogs_repositories_tags_data()







	
