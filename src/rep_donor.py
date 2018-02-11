import sys
import os
import math
import re
import bisect


def rounded(num):
  if int(str(num).split('.')[1])>=5:
    return math.ceil(num)
  else:
    return math.floor(num)


def calc_percentile(p, arr):
  n = len(arr)
  ind = (p/100)*n
  index = math.ceil(ind) - 1
  val = rounded(arr[index])
  return val


def malformed(oid, date, zc, name, cmte, amt):
  oid = re.sub(r' ','',oid)
  date = re.sub(r' ','',date)
  zc = re.sub(r' ','', zc)
  cmte = re.sub(r' ','', cmte)
  amt = re.sub(r' ','', amt)
  if oid:
    return True
  elif len(date) != 8:
    return True
  elif len(zc) < 5:
    return True
  elif not name:
    return True
  elif not cmte:
    return True
  elif not amt:
    return True
  else:
    return False




def repeat_contrib_finder(argv):
  try:
    donor_info = argv[1]
    percentile = int(open(sys.argv[2],'r').readline())
    output_file = argv[3]
    op_f = open(output_file, 'w')

    donor_identity = {}
    total = {}
    transaction_count = {}
    contribs = {}

    with open(donor_info, 'r') as f:
      for line in f:
        info = line.split('|')
        CMTE_ID = info[0]
        NAME = info[7]
        ZIP = info[10][:5]
        DATE = info[13]
        # for above [4:]
        AMOUNT = info[14]
        # float above
        O_ID = info[15]

        if malformed(O_ID, DATE, ZIP, NAME, CMTE_ID, AMOUNT):
          continue

        donor = NAME+ZIP  
        if donor not in donor_identity:
          donor_identity[donor] = int(DATE[4:])

        else:
          if donor_identity[donor] < int(DATE[4:]):
            recipient = CMTE_ID+ZIP+DATE[4:]

            #percentile
            if recipient not in contribs:
              contribs[recipient]= [float(AMOUNT)]

            else:
              bisect.insort(contribs[recipient],float(AMOUNT))

            #contributions summed  
            if recipient not in total:
              total[recipient] = float(AMOUNT)

            else:
              total[recipient] += float(AMOUNT)

            # number of contributions
            if recipient not in transaction_count:
              transaction_count[recipient] = 1
            else:
              transaction_count[recipient] += 1

            total_amount = int(total[recipient])
            running_percentile = calc_percentile(percentile,contribs[recipient])

            op_f.write(CMTE_ID+'|'+ZIP+'|'+DATE[4:]+'|'+str(running_percentile)+'|'+str(total_amount)+'|'+str(transaction_count[recipient])+'\n')

      op_f.close()

            

  except IndexError:
    print('This Python script requires you to specify two input .txt files, one containing \
  individual campaign contribution data and another containing a percentile value. In addition, you must provide a name for the output file')
    sys.exit(1)


if __name__ == '__main__':
  repeat_contrib_finder(sys.argv)