out_dir = 'out-science_fiction'
eval_interval = 250
eval_iters = 200
log_interval = 10

always_save_checkpoint = True

wandb_log = False # override via command line if you like
wandb_project = 'science_fiction'
wandb_run_name = 'mini-gpt'

dataset = 'science_fiction'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # context of up to 256 previous characters

n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 20000
lr_decay_iters = max_iters # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100