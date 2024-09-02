### Superuser
username: udit-todo
<br>
password: udit-todo
<br>
email: uditnayak027@gmail.com

- [x] `.gitignore` 
- [x] Switch to postgres
- [ ] User Authentication


### Switch to Postgres 
- Ensure that `psycopg2` is there in the system.
- Setup the `role` and `database` in the `pgAdmin` or `psql shell`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo_drf',          # Name of DB
        'USER': 'todo_user',         # Name of owner/role
        'PASSWORD': 'todo_password', # password of the role/group
    }
}
```

#### Peer authentication failed for user "todo_user"
The error Peer authentication failed for user "todo_user" indicates that PostgreSQL is trying to authenticate the todo_user using the "peer" authentication method. Peer authentication is typically used for local connections, where PostgreSQL checks if the OS user running the application matches the PostgreSQL role.

##### Steps to Resolve:
1. Modify the `pg_hba.conf` File:
   - Locate and open the `pg_hba.conf` file. This file controls the client authentication settings for PostgreSQL.

       - The file is usually located in `/etc/postgresql/{version}/main/` on Ubuntu. Replace `{version}` with your PostgreSQL version, e.g., `16`.
       - Edit the file with superuser privileges:
           ```
           sudo nano /etc/postgresql/{version}/main/pg_hba.conf
           ```
       - Find the line that looks like this (for local connections):
           ```
           local   all             all                                     peer
           ```
       - Change `peer` to or `password` or `md5`  to allow password authentication:
           ```
           local   all             all                                     password
           ```
       - Save the file and exit the editor (`Ctrl + O` to save, `Ctrl + X` to exit).
2. Reload the Systemd Daemon:
    ```
    sudo systemctl daemon-reload
    ```
3. Restart PostgreSQL Again:
   ```
    sudo systemctl restart postgresql
    ```
4. Verify the PostgreSQL Status
   ```
   sudo systemctl status postgresql
    ```
5. Now run `makemigrations` and the `migrate` cmds.

### Why?
- How to check the data stored in the pgAdmin
- When i change my database to postgres, it ask me to download the `psycopg2` file. Why this is needed

### Cmd to install `psycopg2`
```
sudo apt-get install libpq-dev python3-dev
```
```
pip install psycopg2-binary
# Before Running this command, Do ensure you are in the virtual env.
```