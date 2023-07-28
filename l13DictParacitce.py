

# #
# #
# # # the questions are
# # # What is the industry of the company? #Data Science
# # # List all the projects "John" is working on.
# # # Which employees worked on the "Anomaly Detection" project?

# # # Find the average age of all employees.
# #
# # # print(data_dict['employees']['Mary']['projects'][0]['project_name'])
# # # john_age = data_dict['employees']['John']['age']
# # # mary_age = data_dict['employees']['Mary']['age']
# # # average_age = int((john_age+mary_age) / 2)
# # # print(average_age)
# #
# userinput = input("Enter who you want to see : ")
# dict = data_dict.get('employees').get(userinput).get('projects') # list
# dict = data_dict['employees'][userinput]['projects']
# list = ['apple','orange','bacon','meat']
# for i in dict:
#     print(i['project_name'])
#
# car_dict = {'name':'marcidee',
#                 'wheel':{
#                     'name':'hona','price':'2000','warranty':'2 years'
#                 },
#                 'number_of_wheel':4,
#                 'body':{
#                     'door':[4,{'color':'gray'},{'frame':'deel'}]
#                     'mirror':[6,{'warranty':'2 years'}]
#                 },
#                 'engine':'model2'
#             }

# print(data_dict["employees"]["Mary"]["projects"][1]["project_name"])
# team_members = ["John","Mary","David"]
#
# projects = data_dict["employees"]["Mary"]["projects"][0]['team_members']
# for i in projects:
#     print(i)
data_dict = {
    "employees": {
        "John": {
            "age": 32,
            "department": "Data Science",
            "salary": 75000,
            "projects": [
                {"project_name":"Sales Forecasting", },
                {"project_name":"Image Classification"},
{
                    "project_name": "AI Detection",
                    "status": "completed",
                    "start_date": "2022-09-20",
                    "end_date": "2023-03-31",
                    "team_members": ["Alex", "Emily"],
                    "tasks": {
                        "data_collection": True,
                        "data_preprocessing": True,
                        "model_building": True,
                        "model_evaluation": True,
                    },
                },

            ],
        },
        "Mary": {
            "age": 28,
            "department": "Machine Learning",
            "salary": 70000,
            "projects": [
                {
                    "project_name": "Image Classification",
                    "status": "completed",
                    "start_date": "2021-11-01",
                    "end_date": "2022-02-28",
                    "team_members": ["John", "David", "Sophie"],
                    "tasks": {
                        "data_collection": True,
                        "data_preprocessing": True,
                        "model_building": True,
                        "model_evaluation": True,
                    },
                },
                {
                    "project_name": "Anomaly Detection",
                    "status": "completed",
                    "start_date": "2022-09-20",
                    "end_date": "2023-03-31",
                    "team_members": ["Alex", "Emily"],
                    "tasks": {
                        "data_collection": True,
                        "data_preprocessing": True,
                        "model_building": True,
                        "model_evaluation": True,
                    },
                },

            ],
        },

    },
    "departments": {
        "Data Science": ["John", "Emily"],
        "Machine Learning": ["Mary", "Alex", "Sophie"],
    },
    "company_info": {
        "company_name": "DataTech Corp",
        "founded": "2005-08-10",
        "location": "New York",
        "industry": "Data Science",
        "website": "https://datatechcorp.com",
    },
}
# # # Calculate the total number of projects in the company.
# get the projects from each employees
mary_projects = []
john_projects = []
projects = []
projects_name = data_dict["employees"]["Mary"]["projects"]
for i in projects_name:
    projects.append(i["project_name"])

print(mary_projects)
projects_name = data_dict["employees"]["John"]["projects"]
for i in projects_name:
    projects.append(i["project_name"])

print(john_projects)


# for i in mary_projects: # 3
#     for j in john_projects: # 2
#
#         if i != j:
#             project_count += 1
#         else:
#             pass


# anthoer way for if count is not equal
#['Image Classification', 'Anomaly Detection', 'Sales Forecasting', 'Image Classification']

print(projects)
# project_count = set(projects)
# list = []
# for i in project_count:
#     list.append(i)
# print(list)
# for i in range(len(projects)): # length
#     start  = projects[i]
#     if i != project_length - 1:
#         end = projects[i+1]
#     else:
#         end = None
#
#
#     if start != end:
#         project_count += 1
print("project_count is count")
project_count = 0
for i in projects:
    if i not in projects[:project_count]:
        print(projects[:project_count])
        project_count += 1
# for i in projects:
#     if i in projects[:2]:
#         print(projects[:project_count])
#         project_count += 1
print(f"Project count is {project_count}")

projects[0:1]






