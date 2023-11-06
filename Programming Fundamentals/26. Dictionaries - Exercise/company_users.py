companies = {}
info = input()

while info != "End":
	company_name, employee_id = info.split(" -> ")
	if company_name not in companies.keys():
		companies[company_name] = [employee_id]
	else:
		if employee_id not in companies[company_name]:
			companies[company_name].append(employee_id)
	info = input()

for company_name, employee_id in companies.items():
	print(company_name)
	for employee in employee_id:
		print(f"-- {employee}")
