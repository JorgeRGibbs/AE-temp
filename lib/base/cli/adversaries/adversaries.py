from attackcti import attack_client 

'''
groups = lift.get_groups()
groups = lift.remove_revoked(groups)
group_techniques = lift.get_techniques_used_by_group(groups[0])
print(group_techniques)
print(groups[0])
'''

lift = attack_client()
groups = lift.get_groups()
groups = lift.remove_revoked(groups)
groups_list = []

techniques_used = lift.get_techniques_used_by_all_groups()

for g in groups:
	group_dict = dict()
	group_dict[g['name']] = []
	groups_list.append(group_dict)

for group in groups_list:
	for group_name,techniques_list in group.items():
		for gut in techniques_used:
			if group_name == gut['name']:
				technique_dict = dict()
				technique_dict['techniqueId'] = gut['technique_id']
				technique_dict['techniqueName'] = gut['technique']
				technique_dict['comment'] = gut['relationship_description']
				technique_dict['tactic'] = gut['tactic']
				technique_dict['group_id'] = gut['external_references'][0]['external_id']
				techniques_list.append(technique_dict)
n = 'Naikon'
print(groups_list[1]['Chimera'])
	#if i.key() == n:
	#	print(n) 
