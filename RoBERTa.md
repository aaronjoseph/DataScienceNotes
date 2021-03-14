RoBERTa - `A Robustly Optimized BERT Pretrained Approach`

RoBERTa was proposed with several improvements on top of BERT, with the main assumption that BERT model was "significatly undertrained", the modification over BERT includes
- Training the model longer, with bigger batches
- Removing the next sentence prediction objective
- Training on longer sequences
- Dynamically changing the masking pattern applied to the training data

