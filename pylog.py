#!/usr/bin/python
import ujson
import time
import datetime
from pprint import pprint

PATH = '/Users/mehrdadpazooki/emacsd/pydid/records/%s.log'

class Record():
    def __init__(self, record):
        self.record = record

    def add(self):
        pprint(self.record)
        with open(PATH % time.strftime("%Y_%m"), 'a') as log:
            log.write(ujson.dumps(self.record) + '\n')


def main():
    import argparse
    parser = argparse.ArgumentParser(description='go log yourself.')

    parser.add_argument(
        '-m',
        '--mode',
        help='what kind of log is it? sleep? food? mood?',
        type=str,
    )
    parser.add_argument(
        '-s',
        '--started',
        help='started at this time. format(%Y-%m-%d %H:%M)',
        default=int(time.time()),
        type=str,
    )
    parser.add_argument(
        '-p',
        '--period',
        help='time period in minutes',
        default=1,
        type=int,
    )
    parser.add_argument(
        '-q',
        '--quantity',
        help='quantity',
        default=1,
        type=float,
    )
    parser.add_argument(
        '-me',
        '--metric',
        help='metric for quantity',
        type=str,
    )
    parser.add_argument(
        '-o',
        '--object',
        help='what material?',
        type=str,
    )
    parser.add_argument(
        '-f',
        '--feeling',
        help='how do you feel?',
        type=str,
    )
    parser.add_argument(
        '-n',
        '--note',
        help='comment?',
        type=str,
    )
    args = parser.parse_args()


    if args.started and ':' in str(args.started):
        try:
            args.started = time.mktime(datetime.datetime.strptime(args.started, '%Y-%m-%d %H:%M').timetuple())
        except Exception:
            date = datetime.datetime.now()
            args.started = time.mktime(datetime.datetime.strptime('%s %s' % (date.strftime('%Y-%m-%d'), args.started), '%Y-%m-%d %H:%M').timetuple())
            print 'I completed it for you: __%s__' % time.ctime(args.started)
        finally:
            args.started = int(args.started)



    record = Record(args.__dict__)
    record.add()



if __name__ == '__main__':
    main()
