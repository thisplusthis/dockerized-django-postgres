# middleware/context.py

"""Basic django middleware additional context processor
"""

import datetime


def environment(request):
    """Custom context processer
    """

    # add more data if needed
    return {
        'date': datetime.datetime.today(),
    }
