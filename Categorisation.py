import DataCleaning
import pickle
from collections import Counter
import visualization

###################################################
import sys
import os
import Summarizer

file_path = "Assets/output.txt"
try:
    os.remove(file_path)
    print(f"The file '{file_path}' has been deleted.")
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except PermissionError:
    print(f"You don't have permission to delete the file '{file_path}'.")
except Exception as e:
    print(f"An error occurred while deleting the file '{file_path}': {str(e)}")

# Open a file in write mode
with open('Assets/output.txt', 'w', encoding='utf-8') as file:
    # Redirect the standard output to the file
    sys.stdout = file
    #################################################

    # reading the data from the file
    with open('Assets/dataset', 'rb') as handle:
        data = handle.read()

    print("Data type before reconstruction : ", type(data))

    # reconstructing the data as dictionary
    sectors = pickle.loads(data)

# will be used for working with ui
    sectorData = []


    def get_sector(job_description):
        sector_count = {key: 0 for key in sectors}
        for sector, jobs in sectors.items():
            for job, skills in jobs.items():
                for skill in skills:
                    if skill.lower() in job_description:
                        sector_count[sector] = sector_count[sector] + 1
        sect_dist = [cat + " : " + str(sector_count[cat]) for cat in sector_count if sector_count[cat] > 0]
        print("----SECTOR-------")
        print(sect_dist)
        max_sect = max(sector_count, key=sector_count.get)
        return max_sect


    def get_job(job_description):
        job_description = job_description.lower()
        max_sect = get_sector(job_description)
        job_sect = sectors[max_sect]
        job_count = {}
        job_skills = {}
        for job, skills in job_sect.items():
            job_count[job] = 0
            job_skills[job] = []
            for skill in skills:
                if skill.lower() in job_description:
                    job_count[job] = job_count[job] + 1
                    job_skills[job].append(skill)

        job_dist = [job + " : " + str(job_count[job]) for job in job_count if job_count[job] > 0]
        print("MATCHED JOBS IN ", max_sect.upper())
        print(job_dist)
        max_job = max(job_count, key=job_count.get)
        if job_count[max_job] > 0:
            print("Job: ", max_job, "(", job_count[max_job], ")", "skills", job_skills[max_job])
        uiData(job_description, max_sect, max_job, job_skills[max_job])
        return max_sect


    def calcImpOfSkills(sectorData):
        for sector in sectorData:
            print("for Sector*****************************:" + str(sector["name"]) )
            for jobs in sector["jobs"]:
                skill_scores = {}
                #for skill in jobs["skills"]:
                skill = jobs["skills"]
                counter = Counter(skill)
                seen = set()
                ordered_list = [x for x in skill if x not in seen and (seen.add(x) or True)]
                ordered_list.sort(key=lambda x: -counter[x])
                jobs["skills"]=ordered_list
                print("for job:"+str(jobs["title"])+"->")
                print(ordered_list)

    def uiData(job_description, max_sect, max_job, skills):
        new_sector = False
        if len(sectorData) > 0:
            for sector in sectorData:
                if sector["name"] == max_sect:
                    new_sector = False
                    new_job = False
                    for job in sector["jobs"]:
                        if job["title"] == max_job:
                            new_job = False
                            job["skills"] = job["skills"] + (skills)
                            print(job["skills"])
                            break
                        else:
                            new_job = True
                    if new_job:
                        sector["jobs"].append({"title": max_job, "skills": (skills)})
                    break
                else:
                    new_sector = True
        else:
            sectorData.append({"name": max_sect, "jobs": [{"title": max_job, "skills": (skills)}]})

        if new_sector:
            sectorData.append({"name": max_sect, "jobs": [{"title": max_job, "skills": (skills)}]})
            new_sector = False
        print(sectorData)


    # I used set in the above code so that skills don't get repeated, the below code does the same thing but with repetitive skills

        # new_sector = False
        # if len(sectorData) > 0:
        #     for sector in sectorData:
        #         print(sector["name"], max_sect)
        #         if sector["name"] == max_sect:
        #             new_sector = False
        #             new_job = False
        #             for job in sector["jobs"]:
        #                 if job["title"] == max_job:
        #                     new_job = False
        #                     job["skills"] = job["skills"] + skills
        #                     break
        #                 else:
        #                     new_job = True
        #             if new_job:
        #                 sector["jobs"].append({"title": max_job, "skills": skills})
        #             break
        #         else:
        #             new_sector = True
        # else:
        #     sectorData.append({"name": max_sect, "jobs": [{"title": max_job, "skills": skills}]})
        #
        # if new_sector:
        #     sectorData.append({"name": max_sect, "jobs": [{"title": max_job, "skills": skills}]})
        #     new_sector = False


    # Categorize job ads
    filtered_jobs = []
    separated_jobs = DataCleaning.dataCleaning()
    # job_count = 0
    for job in separated_jobs:
        if job != "":
            lines = job.strip().split('\n')
            result = {}
            current_key = None
            for line in lines:
                if ':' in line:
                    current_key, value = line.split(':', 1)
                    result[current_key.strip()] = value.strip()
                else:
                    if current_key is not None:
                        result[current_key.strip()] += ' ' + line.strip()

            # job_count = job_count + 1
            job_string = ''
            for key, value in result.items():
                if key.__contains__('Job Description') or key.__contains__('about us') or key.__contains__(
                        'requirement profile') or key.__contains__('Job requirement') or key.__contains__(
                    'Basic knowledge') or key.__contains__(
                    'What you bring') \
                        or key.__contains__('tasks include') or key.__contains__(
                    'Advanced knowledge') or key.__contains__('Expert knowledge') \
                        or key.__contains__('Requirement') or key.__contains__('requirements') or key.__contains__(
                    'she expects') or key.__contains__('out'):
                    job_string = job_string + key.strip() + ": " + value.strip() + "\n"
            filtered_jobs.append(job_string)

    all_sect = {key: 0 for key in sectors}
    for job in filtered_jobs:
        print(f"{job}")
        # summary = Summarizer.summarize_jobs(job)
        category = get_job(job)
        all_sect[category] = all_sect[category] + 1
        print("-" * 200)

    print("Each sector and its number of jobs to be clustered")
    print(all_sect)

    sum_of_all = 0
    for each_sect in all_sect:
        sum_of_all = sum_of_all + all_sect.get(each_sect)
    print("Total categorized:", sum_of_all)

    sys.stdout = sys.__stdout__
    calcImpOfSkills(sectorData)
    print(sectorData)
# vsn_of_jobs = "visualisation of " + str(sum_of_all) + " jobs"
# visualization.visualize_jobs(all_sect, "Sectors", "No of jobs", vsn_of_jobs)