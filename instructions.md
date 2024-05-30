Run all jobs from shikra_experiment directory
## First time setup
* Run env_install.job 
* Run download.job to download llama base and shikra download weights
* Run build_shikra.job to build model from previously downloaded llama and shikra-delta weights

## Snelius env
After running the env install job do these to use env
* module purge
* module load 2022
* module load Anaconda3/2022.05
* module load CUDA/11.8.0
* source activate shikra


## Inference
* Download pope images with download_pope_imgs.py
* RUn shikra_inference.job for inference 
* Results are saved to shikra_experiment/exp/shikra_multi_pope
* The result file we are interested in is extra_predictions.json
Note: you only have to download POPE images once, if you update the questions file with new images run it again.

## Prompt modifications
* Input prompts are in data/coco_pope_adversarial.jsonl - only 8 examples to test on
* Remaining pope questions are in rest_of_pope_question.txt
* Prompt template the model uses can be changed in config/_base_/dataset/template/VQA.json
* Copy paste the other template files to VQA.json to use them
* original VQA templates are saved as original_VQA.json in shikra_experiment directory

