# roboforex
Example UI test repository for `stockstrader.roboforex.com`.
- `poetry `
- `pytest-bdd`
- `Playwright`

## Install dependencies
```shell
poetry install
poetry run playwright install chromium --with-deps
```

## Run tests
```shell
# Headless
poetry run pytest

# Headed
poetry run pytest --headed

# Headed WSL
export DISPLAY="$(ip route list default | awk '{print $3}'):0"
export LIBGL_ALWAYS_INDIRECT=1
poetry run pytest --headed
```
