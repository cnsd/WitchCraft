import os
import glob

__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+'/*.py') ]
amount_of_commands = len([ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+'/*.py') ])