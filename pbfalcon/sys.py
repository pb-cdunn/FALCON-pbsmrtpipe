from contextlib import contextmanager
import logging
import os

log = logging.getLogger(__name__)

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    say('CD: %r <- %r' %(newdir, prevdir))
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        say('CD: %r -> %r' %(newdir, prevdir))
        os.chdir(prevdir)

def lg(msg):
    #print(msg)
    log.info(msg)

say=lg

def symlink(actual, symbolic=None):
    """Symlink into cwd, relatively.
    symbolic name is basename(actual) if not provided.
    """
    symbolic = os.path.basename(actual) if not symbolic else symbolic
    rel = os.path.relpath(actual)
    lg('ln -s %s %s' %(rel, symbolic))
    if os.path.lexists(symbolic):
        os.unlink(symbolic)
    if os.path.exists(symbolic) and os.path.samefile(symbolic, actual):
        say("Warning: Cannot symlink('{}', '{}') because they are already the same file.".format(
            actual, symbolic))
        return
    os.symlink(rel, symbolic)

def system(cmd):
    lg('system(%s)' %repr(cmd))
    rc = os.system(cmd)
    if rc:
        raise Exception('%d <- %r' %(rc, cmd))

def filesize(path):
    statinfo = os.stat(path)
    return statinfo.st_size
