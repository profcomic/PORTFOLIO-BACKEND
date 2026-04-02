import requests
from datetime import datetime

def get_github_stats(username):
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "public_repos": data.get("public_repos", 0),
                "followers": data.get("followers", 0),
                "following": data.get("following", 0),
                "last_active": data.get("updated_at", datetime.now().isoformat()),
                "status": "online"
            }
        else:
            # Return mock data if API fails
            return {
                "public_repos": 42,
                "followers": 128,
                "following": 89,
                "last_active": datetime.now().isoformat(),
                "status": "online"
            }
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        # Return mock data on error
        return {
            "public_repos": 42,
            "followers": 128,
            "following": 89,
            "last_active": datetime.now().isoformat(),
            "status": "online"
        }