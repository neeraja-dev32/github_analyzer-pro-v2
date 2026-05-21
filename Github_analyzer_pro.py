import requests
import csv

username = input("enter Github username: ")
profile_url = f"https://api.github.com/users/{username}"
repos_url = f"https://api.github.com/users/{username}/repos"

try:
    profile_response = requests.get(profile_url, timeout=5)

    profile_response.raise_for_status()

    profile_data = profile_response.json()
    
    print("\n===== GITHUB PROFILE =====")
    print("username:", profile_data["login"])
    print("followers:", profile_data["followers"])
    print("Public Repositories:", profile_data["public_repos"])
    print("Account Type:", profile_data["type"])
    print("created at:", profile_data["created_at"])

    repos_response = requests.get(repos_url)
    repos = repos_response.json()

    print("\n===== REPOSITORIES =====")

    language = input(
    "\nEnter language filter: "
    )

    found = False

    for repo in repos:

        if repo["language"] == language:

            found = True
            print(
                repo["name"],
                "|Stars:", repo["stargazers_count"],
                "|Language:", repo["language"],
                "|URL:", repo["html_url"]
          )
    if found == False:
        print("No repositories found")
            
            
        
    with open("github_data.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
        "username",
        "followers",
        "Repository",
        "Stars",
        "Language",
        "URL"
        ])
            
        

        for repo in repos:
            writer.writerow([
                profile_data["login"],
                profile_data["followers"],
                repo["name"],
                repo["stargazers_count"],
                repo["language"],
                repo["html_url"]
                ])
            
    print("\nCSV file created successfully")
    print("\n===== EXPORT SUCCESS =====")
    print("file name: github_data.csv")
    print("Repositories saved:", len(repos))
    
    
    
    
except Exception as e:
    print(e)
    
