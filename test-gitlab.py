import requests
import json
import os

if __name__ == '__main__':
    print("response")
    token = os.getenv("GitLab_Token")
    id = os.getenv("Project_ID")
    print(token)
    print(id)
    response = requests.get("https://gitlab.tis.trane.com/api/v4/projects/" + id + "/pipeline_schedules",
                            headers={"PRIVATE-TOKEN": token})
    if (response.status_code == 200):
        l_PipelineList = json.loads(response.content)
        print(l_PipelineList)
        print(response)
