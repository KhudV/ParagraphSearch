from colorama import Fore, Back, Style



def log(*args, **kwargs):
    '''Prints message into console'''

    print(args, kwargs)

def logact(act: str, *args, **kwargs):
    '''Prints message with header into console'''

    print(Fore.MAGENTA + act + Style.RESET_ALL)
    print(args, kwargs)

def logerr(*args, **kwargs):
    '''Prints colorized error message into console'''
    print(Fore.RED)
    print(args, kwargs)
    print(Style.RESET_ALL)
