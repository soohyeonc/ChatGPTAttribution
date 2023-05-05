


#!/bin/bash

PYPATH="$(pwd)"
CORES=5

# Short check to assure that we start the script in PyProject directory
if [ ${PYPATH##*/} != "PyProject" ];
then
    echo "go to PyProject directory and start the script there"
    exit 1
fi

# Now start the attack for one or more chosen problems

OUTPUT_FILE="run_train_models_parallel.log"
if [ -f OUTPUT_FILE ] ; then
    rm OUTPUT_FILE
fi
#
# parallel -j $CORES --delay 5 PYTHONPATH=${PYPATH} python3 evaluations/learning/rf_usenix/train_models_parallel.py {}\
#  ::: 3264486_5633382285312000   >> $OUTPUT_FILE


#1  3264486_5633382285312000
#2  3264486_5654742835396608
#3  3264486_5736519012712448
#4  5304486_5697460110360576
#5  5304486_5760761888505856
#6  8294486_5630967708385280
#7  8294486_5654117850546176
#8  8294486_5681755159789568

parallel -j $CORES --delay 5 PYTHONPATH=${PYPATH} python3 evaluations/learning/rf_usenix/train_models_parallel.py {}\
 ::: 3264486_5633382285312000  3264486_5654742835396608  3264486_5736519012712448 \
     5304486_5697460110360576  5304486_5760761888505856  8294486_5630967708385280 \
     8294486_5654117850546176  8294486_5681755159789568 >> $OUTPUT_FILE



# parallel -j $CORES --delay 5 PYTHONPATH=${PYPATH} python evaluations/learning/rf_usenix/train_models_parallel.py {}\
# ::: 8294486_5654117850546176  8294486_5681755159789568  >> $OUTPUT_FILE
