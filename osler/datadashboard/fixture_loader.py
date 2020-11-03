import random
import datetime
import json

path = "osler//osler//fixtures//"

with open(path+"extra_patients.json","r") as p:
	patients = json.load(p)

with open(path+"extra_workups.json","r") as w:
	workups = json.load(w)

names = ['Calvin Lawson', 'Perry Garcia', 'Gertrude Schneider', 'Forrest Cain', 'Margaret Dunn', 'Sadie Richards', 'Nora Leonard', 'Vicki Castro', 'Everett Kennedy', 'Ervin Padilla', 'Chad Boone', 'Kelly Lamb', 'Tara Martinez', 'Erick Cobb', 'Eunice Adkins', 'Julie Sims', 'Blanca Gonzales', 'Kristin Henry', 'Amelia Harper', 'Terrence Howard', 'Leonard Barnett', 'Winston Mckenzie', 'Armando Lindsey', 'Virginia Matthews', 'Phillip Saunders', 'Leigh Gilbert', 'Catherine Sanchez', 'Carol Weber', 'Brett Palmer', 'Paulette Bass', 'Leroy West', 'Howard Ryan', 'Rachael Swanson', 'Amos Ramsey', 'Sergio Vaughn', 'Pat Brady', 'Bernadette Cruz', 'Wayne Thomas', 'Tyler Love', 'Claude Soto', 'Jacquelyn Burton', 'Kenneth Zimmerman', 'Hubert Peterson', 'Virgil Morris', 'Jacqueline Miller', 'Rachel Hanson', 'Danielle Douglas', 'Billy Fleming', 'Enrique Vega', 'Rosa Mccarthy', 'Alison Henderson', 'Jeremy Oliver', 'Melanie Marsh', 'Bertha Garza', 'Alexis Roberts', 'Andrew Park', 'Alicia Ortega', 'Monique Patterson', 'Delia Burns', 'Dewey Weaver', 'Marsha Walton', 'Willie Goodwin', 'Geoffrey Parsons', 'Salvador Morales', 'Susan Jones', 'Clay Neal', 'Craig Mullins', 'Brandi Banks', 'Meredith Gonzalez', 'Ruben Holland', 'Norma Barton', 'Adrian Ramos', 'Jackie Herrera', 'Henrietta Lawrence', 'Kimberly Perkins', 'Orville Franklin', 'Velma Gardner', 'Melinda Watts', 'Christina Mills', 'Heidi Maxwell', 'Gregory Pena', 'Melba Fox', 'Bill Robinson', 'Rudy Jennings', 'Rudolph Sandoval', 'Delbert Olson', 'Kate Lucas', 'Jamie Foster', 'Violet Maldonado', 'Maxine Powers', 'Bobbie Wise', 'Norman Ball', 'Gwendolyn Ellis', 'Ivan Grant', 'Agnes Pearson', 'Nettie Parks', 'Elijah Phelps', 'Kristy Mason', 'Owen Jensen', 'Kay Lee']
dates = []

def generate_date():
	for i in range(100):
		r = random.randint(18,80)
		days = random.randint(1,365)
		d = datetime.datetime.now()-datetime.timedelta(days=r*days)
		d = d.date()
		dates.append(str(d))


ethnicities = ["White", "Black or African American", "American Indian or Alaska Native",
               "Asian", "Native Hawaiian or Other Pacific Islander", "Hispanic or Latino", "Other"]

generate_date()

def load_fixtures():
	pk = 5
	for p in range(6,100):
		patient = patients[0].copy()
		patient["pk"] = p
		f = patient["fields"].copy()
		name = names[p].split(" ")
		f["first_name"] = name[0]
		f["last_name"] = name[1]
		f["date_of_birth"] = dates[p]
		g = random.randint(0,1)
		if(g==0):
			f["gender"] = "Male"
		else:
			f["gender"] = "Female"
		f["ethnicities"] = random.sample(ethnicities, random.randint(1, 3))
		patient["fields"] = f
		patients.append(patient)
		num_workups = random.randint(1,5)
		for w in range(num_workups):
			workup = workups[6].copy()
			workup["pk"] = pk
			f = workup["fields"].copy()
			f["bp_sys"] = str(random.randint(100,180))
			f["patient"] = p
			r = random.randint(0,1)
			if(r==0):
				f["diagnosis"] = "hypertension"
			else:
				f["diagnosis"] = "diabetes"
			workup["fields"] = f
			workups.append(workup)
			pk+=1
			

load_fixtures()

with open(path+"extra_patients.json","w") as p:
	json.dump(patients,p, indent=4)

with open(path+"extra_workups.json","w") as w:
	json.dump(workups,w,indent=4)

