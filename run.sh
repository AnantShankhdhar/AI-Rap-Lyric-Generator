#!/bin/env bash
python3 run_clm_flax.py \
    --output_dir="./" \
    --model_type="gpt2" \
    --config_name="./" \
    --tokenizer_name="./" \
    --train_file="/home/anantshankhdhar/gpt2-rap-lyric-generator/Train.tsv" \
    --validation_file="/home/anantshankhdhar/gpt2-rap-lyric-generator/Val.tsv" \
    --block_size="512" \
    --do_train \
    --do_eval \
    --per_device_train_batch_size="64" \
    --per_device_eval_batch_size="32" \
    --learning_rate="5e-4"  \
    --adam_beta1="0.9" --adam_beta2="0.98" --weight_decay="0.01" \
    --overwrite_output_dir \
    --num_train_epochs="60" \
    --logging_steps="100" \
    --save_steps="200" \
    --eval_steps="100" \
