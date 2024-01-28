import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'] [0] ['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_chart_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

#перевірка, що конкретний емоджи є в списку всіх емоджи 
@pytest.mark.api
def test_emoji_can_be_found(github_api):
    r = github_api.search_emojis('zombie_woman')
    assert 'zombie_woman' in r

#перевірка, що неіснуючого емоджи немає в загальному списку
@pytest.mark.api
def test_nonexisted_emoji(github_api):
    r = github_api.search_emojis('nonexisted_emoji')
    assert 'nonexisted_emoji' not in r

#перевірка, що існує власник репозиторію з іменем Spiritus839
@pytest.mark.api 
def test_repository_owner_exists(github_api):
    r = github_api.get_user('spiritus839')
    assert r['login'].lower() == 'spiritus839'

#перевірка, що запит успішний
@pytest.mark.api 
def test_search_commits(github_api):
    r = github_api.search_commits('Spiritus839', 'OlenaQA')
    assert r.status_code == 200

#перевірка, що кожен коміт має ключі 'author', 'commit'
@pytest.mark.api 
def test_search_commits_key_exists(github_api):
    r = github_api.search_commits('Spiritus839', 'OlenaQA').json()
    for commit in r:
        assert 'author' in commit
        assert 'commit' in commit
    
