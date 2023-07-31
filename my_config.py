MY_ID = -1
CUSTOMER_ABSENT, CUSTOMER_LOGIN, CUSTOMER_EMAIL = (0, 1, 2)

APP_NAME = "Autorent"
ADMIN_PERM = 0

BACKGROUND = 'GoldenRod2'
FOREGROUND = 'CornSilk1'
ERROR_FOREGROUND = 'red'


def is_float(value):
    
    try:
        return isinstance(float(value), float)
    except ValueError:
        return False


def is_integer(value):
    
    try:
        return isinstance(int(value), int)
    except ValueError:
        return False
