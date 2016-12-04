from familytree.mongo import get_mongo

def parse_individual(individual):
	retval = {
		"given_name": individual.given_name(),
		"surname": individual.surname(),
		"tag": individual.tag()
	}
	retval['parents'] = [process_individual(parent) for parent in individual.parents()]
	retval['children'] = [process_individual(child) for child in individual.children()]
	retval['death'] = [parse_event(event) for event in individual.death_events]
	retval['birth'] = [parse_event(event) for event in individual.birth_events]
	retval['marriage'] = [parse_event(event) for event in individual.marriages()]
	return retval

def parse_event(ev):
	return {"date":ev.date, "place":ev.place}

def process_individual(ind):
	return {"given_name":ind.given_name(), "surname":ind.surname(), "person":save_individual(ind)}

def save_individual(ind, user, recursive=False):
	db = get_mongo('tree')
	set_command = {"$set":parse_individual(ind)} if recursive else {"$setOnInsert":{"given_name":ind.given_name(),"surname":ind.surname()}}
	ind_doc = db.person.find_one_and_update(
			{"given_name":ind.given_name(),"surname":ind.surname()},
			set_command, upsert=True
		)
	return ind_doc['_id'] if ind_doc else None

def save_family(fam):
	family = {}
	family['events'] = [{"type":event.type, "event":parse_event(event)} for event in fam.other_events]
	db = get_mongo('tree')
	fam_doc = db.family.find_one_and_update(
		{"tag": fam.tag()}, {"$set": family}
 	)
