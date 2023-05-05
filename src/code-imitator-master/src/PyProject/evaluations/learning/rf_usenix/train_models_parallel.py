import sys
sys.path.insert(0, '/home/seal12/Downloads/Chatgpt/code-imitator-master/src/PyProject')


from featureextractionV2 import utils_extraction
from featureextractionV2.StyloFeaturesProxy import StyloFeaturesProxy
from featureextractionV2.StyloFeatures import StyloFeatures
from classification import StratifiedKFoldProblemId

# import importlib
import typing
import os

import numpy as np
import evasion.utils_launch_attacks
from ConfigurationLearning.ConfigurationLearning import ConfigurationLearning
import ConfigurationGlobalLearning as Config
import classification.NovelAPI.utils_classification

############### Input ##############
parser = evasion.utils_launch_attacks.getProblemIDParser()
args = parser.parse_args()
PROBLEM_ID_LOADED = args.problemid[0]

#2 = original
#3_structcoder = result from structcoder


#MCTS & Structcoder = challenage number
#7 & 15= 3264486_5633382285312000
#8 & 16= 3264486_5654742835396608
#9 & 17= 3264486_5736519012712448
#10 & 18= 5304486_5697460110360576
#11 & 19= 5304486_5760761888505856
#12 & 20= 8294486_5630967708385280
#13 & 21= 8294486_5654117850546176
#14 & 22= 8294486_5681755159789568

pdn = "9"

print(PROBLEM_ID_LOADED,file=sys.stderr)
if PROBLEM_ID_LOADED == "3264486_5633382285312000":
    data_num = pdn+"1"

elif PROBLEM_ID_LOADED == "3264486_5654742835396608":
    data_num = pdn+"2"

elif PROBLEM_ID_LOADED == "3264486_5736519012712448":
    data_num = pdn+"3"

elif PROBLEM_ID_LOADED == "5304486_5697460110360576":
    data_num = pdn+"4"

elif PROBLEM_ID_LOADED == "5304486_5760761888505856":
    data_num = pdn+"5"

elif PROBLEM_ID_LOADED == "8294486_5630967708385280":
    data_num = pdn+"6"

elif PROBLEM_ID_LOADED == "8294486_5654117850546176":
    data_num = pdn+"7"

elif PROBLEM_ID_LOADED == "8294486_5681755159789568":
    data_num = pdn+"8"

suffix = "_2017_8_"+data_num+"_formatted_macrosremoved"
############### Variable Definition ##############

suffix = "_2017_9_3_formatted_macrosremoved"


#suffix = "_2017_11_formatted_macrosremoved"
print(suffix,file=sys.stderr)


configuration_learning: ConfigurationLearning = ConfigurationLearning(
    repo_path=Config.repo_path,
    dataset_features_dir=os.path.join(Config.repo_path, "data/dataset_2017"),
    suffix_data=suffix, #"_2017_8_8_formatted_macrosremoved",
    learnmodelspath=Config.learnmodelspath,
    use_lexems=False,
    use_lexical_features=False,
    stop_words=Config.stop_words_codestylo,
    probsperprogrammer=Config.probsperprogrammer,
    no_of_programmers = 210,
    #no_of_programmers = 205,
    noofparallelthreads= 8,
    hyperparameters={"n_estimators": [204, 250, 300, 350],
                     "max_features": [0.1, 0.2, 0.3, 0.4, 0.5, "log2", "sqrt"],
                     "max_depth": [10, 15, 20, 25, 30, 40, 50],  # 50
                     "min_samples_leaf": [2, 4, 6, 8, 10, 12, 14],
                     }
)



learn_method: str = ["RF", "SVM", "DNN"][0]
feature_method: str = ["Usenix", "CCS18"][0]
threshold_sel: typing.Union[int, float] = [1.0, 800][0]

# Directory where model files will be stored, set None if you do not want to save anything, or specify a path.
if configuration_learning.learnmodelspath is not None:
    modelsavedir = os.path.join(configuration_learning.learnmodelspath, feature_method + "_" + learn_method)
    os.makedirs(modelsavedir) if not os.path.exists(modelsavedir) else print("Use existing dir for models", file=sys.stderr)
else:
    modelsavedir = None


############## Get lexical, layout and syntactic features ##############

if feature_method == "Usenix":
    features_merged: StyloFeaturesProxy = utils_extraction.extract_link_train_test_usenix_features(config_learning=configuration_learning)
    #features_merged2: StyloFeaturesProxy = utils_extraction.extract_link_train_test_usenix_features(config_learning=configuration_learning2)

elif feature_method == "CCS18":
    assert configuration_learning.use_lexems is not True
    unigrammmatrix_train: StyloFeatures = utils_extraction.extract_train_test_unigram(
        config_learning=configuration_learning, tf=True, idf=True, ngram_range=(1, 3))
    features_merged: StyloFeaturesProxy = StyloFeaturesProxy(codestyloreference=unigrammmatrix_train)

else:
    raise Exception("feature_method")

############# Split dataset into train - test set with our our grouped stratified k-fold ##############
skf2 = StratifiedKFoldProblemId.StratifiedKFoldProblemId(iids=features_merged.getiids(), n_splits=8, shuffle=False,
                                                         random_state=411,
                                                         nocodesperprogrammer=configuration_learning.probsperprogrammer)

print("No splits:", skf2.get_n_splits())


############# Do training + testing on each split ##############
accuracy = {}

for train_index, test_index in skf2.split(None, None):
#for train_index, test_index in zip(train_list, test_list):
    # print(train_index,file=sys.stderr)
    # print(test_index,file=sys.stderr)

    curproblemid = "_".join(features_merged.getiids()[test_index[0]].split("_")[0:2])
    if curproblemid == PROBLEM_ID_LOADED:
        print(curproblemid,file=sys.stderr)
        # exit()
        # the following method saves the model and config file into modelsavedir if given
        accuracy, _ = classification.NovelAPI.utils_classification.perform_standard_classification_for_split(
            features_merged=features_merged,
            train_index=train_index,
            test_index=test_index,
            problem_id_test=curproblemid,
            configuration_learning=configuration_learning,
            modelsavedir=modelsavedir,
            threshold_sel=threshold_sel,
            learn_method=learn_method,
            skf2=skf2
        )
        print(accuracy.values(),file=sys.stderr)

print("FINAL",file=sys.stderr)
print(accuracy,file=sys.stderr)
accuracies = np.array([x for x in accuracy.values()])
print(np.mean(accuracies)*100,file=sys.stderr)
print(np.sqrt(np.var(accuracies)),file=sys.stderr)
