from pexpect import pxssh
import getpass
def operation():
    try:                                                            
        s = pxssh.pxssh()
        hostname = raw_input('hostname: ')
        username = raw_input('username: ')
        password = getpass.getpass('password: ')
        s.login (hostname, username, password)
        s.sendline ('uptime')
        s.prompt()             
        print s.before

        s.sendline ('ls -l')
        s.prompt()
        print s.before

        s.sendline ('df')
        s.prompt()
        print s.before()

        s.sendline('sudo lsof -i -n | egrep "\<ssh\>"')
        s.prompt()
        print s.before
        
        s.logout()
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)

if __name__ == "__main__":
    operation()