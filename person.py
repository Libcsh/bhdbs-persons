import json
import requests

class Person:

	def __init__(self, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)

	@property
	def siblings_count(self):
	    return len(self.siblings)


	@property
	def parents_count(self):
	    return len(self.parents)

	@property
	def partners_id(self):
		partners_ids = []
		for partner in self.partners:
			partners_ids.append(partner['id'])
			return partners_ids

	@property
	def names_of_person(self):
		self.name = self.name
		names_of = str(self.name[0].capitalize())
		try:
			return names_of
		except UnicodeEncodeError:
			return "Unknown"
		


def get_persons(last_name):
	ret = []
	for number in range(0,44910,30):
		url = "http://api.dbs.bh.org.il/v1/person?last_name={}&start={}".format(last_name, number)
		response = requests.get(url)
		for i in response.json()['items']:
			ret.append(Person(**i))
	return ret

	File "/home/libigelber/bhdbs-persons/person.py", line 29, in names_of_person
    return str(self.name[0].capitalize())
UnicodeEncodeError: 'ascii' codec can't encode characters in position 6-9: ordinal not in range(128)