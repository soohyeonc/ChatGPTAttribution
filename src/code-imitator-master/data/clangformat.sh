#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

#SRC="/home/seal12/Downloads/code-imitator-master/data/dataset_2017/clang_test/"
#OUTPUT_DIR="/home/seal12/Downloads/code-imitator-master/data/dataset_2017/clang_test_formatted/"

# SRC="/home/seal12/Downloads/code-imitator-master/data/dataset_2017/dataset_2017_8_3/"
# OUTPUT_DIR="/home/seal12/Downloads/code-imitator-master/data/dataset_2017/dataset_2017_8_3_formatted/"

SRC="/home/seal12/Downloads/Chatgpt/code-imitator-master/data/dataset_2017/dataset_2017_10/"
OUTPUT_DIR="/home/seal12/Downloads/Chatgpt/code-imitator-master/data/dataset_2017/dataset_2017_10_formatted/"

#SRC="<path-to-repo>/authorship-evasion/data/dataset_2017/dataset_2017_8_3/"
#OUTPUT_DIR="<path-to-repo>/authorship-evasion/data/dataset_2017/dataset_2017_8_3_formatted/"

MAX_TIME=3000
MAX_JOBS=8

# Be careful, output dir should not be src, otherwise a call such as
#   clang-format file.cpp > file.cpp will yield an empty cpp file ;)
if [ "${SRC}" == "${OUTPUT_DIR}" ]; then
    echo "Src and output dir are the same. Will lead to empty files."
    exit 1
fi



echo -e "${RED}Let's start formatting all samples via clang-format${NC}"

# create target dir's, skip first line that is the SRC itself.
find "${SRC}" -type d | tail -n+2 | parallel mkdir -p ${OUTPUT_DIR}{/}

# check that skipping does not lead to any error's.
nofilessrc=`(ls -l ${SRC} | wc -l)`
nofilestar=`(ls -l ${OUTPUT_DIR} | wc -l)`
echo "NoFiles: ${nofilessrc};${nofilestar}"
if [ "${nofilessrc}" -ne "${nofilestar}" ]; then
    echo "mismatch. error"
    exit 1
fi

# We call clang-format on each input file, pipe the output into a new file in output dir
for f in $(find "${SRC}" -type f -regex '\(.*c\|.*cpp\)')
 do
	PARENT=$(basename $(dirname $f))
	AUTHOR=$(basename $f)
    #clang-format $f > ${OUTPUT_DIR}${PARENT}/${AUTHOR}
    g++ $f > ${OUTPUT_DIR}${PARENT}/${AUTHOR}
 done
