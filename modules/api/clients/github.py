import requests

class GitHub:
    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
            )
        body = r.json()

        return body
    
    #метод для пошуку емоджи
    def search_emojis(self, emoji_name):
        r = requests.get(
            "https://api.github.com/emojis",
            params={"q": emoji_name}
            )
        body = r.json()

        return body
    
    #метод для пошуку комітів
    def search_commits(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    
        return r
        
