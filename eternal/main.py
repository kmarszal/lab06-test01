import sys
import argparse


def calculate(year, month, day):
  ints = [year, month, day]
  for i in ints:
    if not isinstance(i,int):
      raise TypeError
      
  if 0 < month < 13:
    if month == 2:
      if day > 28 or day <1:
        raise BaseException
    elif month in [4,6,9,11]:
      if day > 30 or day <1:
        raise BaseException
    else:
      if day > 31 or day <1:
        raise BaseException
  if month < 3:
    c = 0
    z = year - 1
  else:
    z = year
    c = 2
  ret = (23*month/9 + day + 4 + year + (z/4) + (z/100) + (z/400) - c) % 7
  return ret


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--year',
                        type=int,
                        required=True,
                        help='Year')
    parser.add_argument('--month',
                        type=int,
                        required=True,
                        help='Month')
    parser.add_argument('--day',
                        type=int,
                        required=True,
                        help='Day')
    parsed_args = parser.parse_args(args)
    weekday = calculate(parsed_args.year, parsed_args.month, parsed_args.day)
    print("Weekday {}".format(weekday))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
