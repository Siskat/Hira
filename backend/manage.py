# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from Hira import app, socketio
from Hira import MainModule

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True)
)

@manager.command
def run():
   socketio.run(app,
                host='127.0.0.1',
                port=5000,
                use_reloader=False)

if __name__ == "__main__":
    manager.run()
