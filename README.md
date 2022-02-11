
# Tags and Repositories Catalogs

Tags and Repositories Catalogs - this application uses two methods:
    1) get the list of repositories;
    2) get a list of tags by repository

## Quick Start

```shell
python3 -m venv .venv
source .venv/bin/activate
To start the program, enter the following environment variables:url,login,password.
For example: export DOCKER_REGISTRY_API_URL="url"
             export LOGIN_USER="login"
             export PASSWORD_USER="password"
             ./docker-repotool-list.py
```

### From sources
#### Prerequisites

```shell
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```
## Developer Notes

### Init
* Open the project in [VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
* Setup recommended extensions in VS Code such a [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.  python)
* Initialize Virtual Environment
    ```
    python3 -m venv .venv
    ```

### Re-new requirements.txt

```shell
python3 -m pip freeze > requirements.txt
```

### API Documentation

```shell
https://docs.docker.com/registry/spec/api/#listing-repositories
```
