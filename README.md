# IDS-Descriptive-Statistics 

[![Docker Image CI Main](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/main.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/main.yml)

[![Docker Image CI Test](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/test.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/test.yml)

[![Docker Image CI Format](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/format.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/format.yml)

[![Docker Image CI Install](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/install.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/install.yml)

[![Docker Image CI Lint](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/lint.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-Project-1/actions/workflows/lint.yml)

## Demo Video

https://youtu.be/4M5TUXnW9u8

## Quick Explanation

* Creates descriptive statistics and outputs them as a pdf and image into [`data folder`](./src/main_workspace/outputs) using [`python script`](./src/main_workspace/stats_pdf.py)
* CI/CD pipline also auto runs script to update [`pdf and image`](./src/main_workspace/outputs)

* jupyter Notebook with: 
    * Cells that perform descriptive statistics using Polars or Panda.
    * Tested by using nbval plugin for pytest

## Set up instructions using VS code + Docker: 
### Docker
1. For Windows, Mac, and maybe Linux, you download Docker Desktop. links can be found [here](https://docs.docker.com/engine/install/). Follow set up instructions and start the application.

2. In vs code add Dev Containers and Docker extensions 

3. clone repo, restart vs code, and open repo in vs code.

4. should see a pop up to (re)open in devcontainer. Click it and let it run. It takes a bit of time for the first run but is much faster after that. Done.

#### Alternatives to Docker
If you choose not to run docker, use a python virtual environment to prevent conflict with local packages and run the makefile.
 
## Testing

### makefile  
* install

* testing:

    tests all "\*test\*.py" files in src/test/ using py.test then tests all files using py.test --nbval-lax (-lax used as pdf generation has time stamps)

* lint

* format

* all 

### VS code testing  
1. Can also use the VS-code testing menu in the same way.

## Things included are:

* [`Makefile`](Makefile)

* `Pylint`

* `.devcontainer` with [`Dockerfile`](/.devcontainer/Dockerfile), [`postinstall.sh`](/.devcontainer/postinstall.sh), and [`devcontainer.json`](/.devcontainer/devcontainer.json)`

*  [`settings.json`](.vscode/settings.json) for testing

*  A base set of libraries in [`requirements.txt`](requirements.txt)
