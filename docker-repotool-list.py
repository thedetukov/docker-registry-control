#!/usr/bin/env python
#
import requests 
from requests.auth import HTTPBasicAuth
from os import environ
import sys
import datetime 


def main(docker_registry_api_url: str, login_user: str, password_user: str):
	
	try:
		credentials = HTTPBasicAuth(login_user, password_user)
		catalog_api_url = docker_registry_api_url + "/v2/_catalog"
		catalog_response = requests.get(catalog_api_url, auth = credentials)
		catalog = catalog_response.json()
		mass_catalog = catalog['repositories']
		for repo_name in mass_catalog:
			catalog_tag_api_url= docker_registry_api_url + "/v2/%s/tags/list" % repo_name
			catalog_tag_response = requests.get(catalog_tag_api_url, auth = credentials)
			catalog_tag_list = catalog_tag_response.json()
			catalog_name = catalog_tag_list['name']
			for tag_name in catalog_tag_list['tags']:
				manifest_api_url  = docker_registry_api_url + "/v2/%s/manifests/%s" % (catalog_name, tag_name)  
				headers = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
				manifest_response = requests.head(manifest_api_url, headers =  headers, auth = credentials)
				manifest_docker_content_digest = manifest_response.headers['Docker-Content-Digest']
				manifest_last_modified = manifest_response.headers['Last-Modified']
				converted_manifest_last_modified = datetime.datetime.strptime(manifest_last_modified, "%a, %d %b %Y %H:%M:%S %Z").strftime("%Y-%m-%dT%H:%M:%S")

				print(catalog_name + '/manifest:' + tag_name, converted_manifest_last_modified)
				print(manifest_docker_content_digest)			
		
	except Exception as ex:
		print("Attempt failure. {0}".format(ex), file=sys.stderr)

def _get_environ_variable(name: str, exit_code: int):
	value = environ.get(name, None)
	if value is None:
		print("A required environment variable '%s' is not set." % name, file=sys.stderr)
		sys.exit(exit_code)
	return value

if __name__ == "__main__":
	import sys

	docker_registry_api_url = _get_environ_variable('DOCKER_REGISTRY_API_URL', 1)
	login_user = _get_environ_variable('LOGIN_USER', 2)
	password_user = _get_environ_variable('PASSWORD_USER', 3)
	

	# launch application loop
	main(docker_registry_api_url, login_user, password_user)







	
