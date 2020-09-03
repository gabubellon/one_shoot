# new_env_kernel

Add a python virtualenv with new kernel to jupyter on user.

## How to use

To use this script you need centralize your virtualenvs in a same folder

Change script line to use your virtualenvs local path:

```bash
## CHANGE TO YOUR LOCAL VIRTUAL ENV STORAGE
VENVS="$HOME/.virtualenvs/"
```

Give run permission to script:

```bash
chmod +x new_env_kernel.sh
```

Create your virtualenv inside virtualenvs local path (e.g. `python3 -m venv $HOME/.virtualenvs/myvenv`)

Run script with `-v <name_of_virtual_env>` parameter:

```bash
./new_env_kernel.sh -v <name_of_virtual_env>
```

Script will activate virtual env, install `ipython` and `ipykernel` and put this env with a new jupyter kernel with same name of virtual env.

Now, when start a new jupyter/jupyerlab instance, your virtualenv can used by a kernel.

---

If do you like know more all manager your local python versions and virtualenvs take a look  in this [tutorial](https://www.gabubellon.me/blog/pyenv).
