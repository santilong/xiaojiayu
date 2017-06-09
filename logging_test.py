# import logging
# logging.basicConfig(filename='logging.log',filemode='w',level=logging.DEBUG)
# logging.debug('test debug')
# logging.warning('warning')
#
# logging.debug('ooo')

# import logging
# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('is when this event was logged.')

# import logging
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')


import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H-%M-%S')
logging.warning('???')
logging.basicConfig