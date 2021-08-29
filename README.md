## AI RAP LYRIC GENERATOR

Generating rap lyrics from using artist name and song title <br/>
GPT2 finetuned on over 10000 songs from multiple artists using google cloud TPU-VM<br/>
### The model has been deployed as a demo on huggingface spces the link to the demo - [click here](https://huggingface.co/spaces/Shankhdhar/Rap-Lyric-generator)<br/>
The dataset used for training can be found [here](https://huggingface.co/datasets/Cropinky/rap_lyrics_english/tree/main) <br/>
You can even use this google colab notebook for making predictions [click here](https://colab.research.google.com/drive/1aibR06TrFGnt-TPmyIRDD2-8eT7PU5Kl#scrollTo=rgE3QbiTFIMQ)<br/>
For the entire code with model file also available checkout the huggingface repository [here](https://huggingface.co/flax-community/gpt2-rap-lyric-generator/tree/main)<br/>

### Files in the repository:-<br/>
1) run_clm_flax.py contains the training script<br/>
2) run.sh can be used to run the training script and the hyperparameters can be directly specified there<br/>
3) genius.py contains the file to download songs from genius.com<br/>

#### An example of how demo works <br/>










