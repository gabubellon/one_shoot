# new_env_kernel

Add a python virtualenv with new kernel to jupyter on user.

## How

To use this script you need centralize your virtualenvs in a same folder

Change script to your virtualenvs local path 

```bash
## CHANGE TO YOUR LOCAL VIRTUAL ENV STORAGE
VENVS="$HOME/.virtualenvs/"
```

Give run permission to script

```bash
chmod +x new_env_kernel.sh
```

Run script with `-v <name_of_virtual_env>` parameter

```bash
./new_env_kernel.sh -v <name_of_virtual_env>
```

Script will activate virtual env, install `ipython` and `ipykernel` and put this env with a new jupyter kernel with same name of virtual env.

---

If do you like know more all manager your local python versions and virtualenvs take a look  in this [tutorial].(https://www.gabubellon.me/blog/pyenv)
