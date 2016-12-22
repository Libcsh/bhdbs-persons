import json
import csv

import person



def make_csv(list_of_details):
	with open("output.csv", "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(list_of_details)
	    f.close()



def main():
	cohen_details = []
	for p in person.get_persons("cohen"):
		name = p.name
		person_details = [p.names_of_person, p.tree_num, p.tree_version, p.id, p.sex, p.siblings_count]
		cohen_details.append(person_details)
	
	make_csv(cohen_details)


if __name__ == '__main__':
	main()