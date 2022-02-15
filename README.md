
Docker Registry List
Docker Registry Control is a application used for check last modified date and digest content of repository files.

### Quick Start
```shell
python3 -m venv .venv
source .venv/bin/activate
pip install --requirement requirements.txt
```

### Launch
```shell
export DOCKER_REGISTRY_CONTROL_URL="url"
export DOCKER_REGISTRY_CONTROL_USER="login"
export DOCKER_REGISTRY_CONTROL_PASSWORD="xxxxxxxx"
./drctl-list.py | tee result.txt
```

### Re-new requirements.txt

```shell
python3 -m pip freeze > requirements.txt
```

### References

```shell
https://docs.docker.com/registry/spec/api/#listing-repositories
```
