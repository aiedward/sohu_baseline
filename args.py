# -----------ARGS---------------------
ROOT_DIR = "/root/liuyijiang/liu/Bert_Chinese_Ner_pytorch/"
RAW_SOURCE_DATA = "data/source.txt"
RAW_TARGET_DATA = "data/target.txt"
STOP_WORD_LIST = None
CUSTOM_VOCAB_FILE = None
VOCAB_FILE = "model/vocab.txt"
TRAIN = "data/train.json"
VALID = "data/dev.json"
log_path = "output/logs"
plot_path = "output/images/loss_acc.png"
data_dir = "data/"  # 原始数据文件夹，应包括tsv文件
cache_dir = "model/"
output_dir = "output/checkpoint"  # checkpoint和预测输出文件夹

bert_model = "bert-base-chinese"  # BERT 预训练模型种类 bert-base-chinese
task_name = "bert_ner"  # 训练任务名称
bert_cache = '/root/.pytorch_pretrained_bert/distributed_-1'
flag_words = ["[PAD]", "[CLP]", "[SEP]", "[UNK]"]
max_seq_length = 220
do_lower_case = True
train_batch_size = 16
eval_batch_size = 16
learning_rate = 2e-5
num_train_epochs = 20
warmup_proportion = 0.1
no_cuda = False
seed = 233
gradient_accumulation_steps = 1
fp16 = False
loss_scale = 0.
labels = ["B-entity", "I-entity", "O"]
device = "cuda"
