
from flaskblog import create_app,db
from flask_script import Manager,Server
from flaskblog.models import User,Post
from flask_migrate import Migrate,MigrateCommand



app = create_app('development')
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)





@manager.shell
def make_shell_context():
  return dict(app = app,db = db,User = User,Post = Post)

if __name__ == '__main__':
  manager.run()