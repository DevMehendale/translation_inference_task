# Translation Inference Task
### Web scraper + Translation inference comparison of two models(IndicTrans and HuggingFace)


Steps to run the code-
1)	Clone the github repo-

    ```git clone https://github.com/DevMehendale/translation_inference_task.git```
2)	Primary code is in the ```inference.py``` file and some user-defined functions are in ```web_scraper_func.py``` module which has already been imported in ```inference.py```
3)	Open ```inference.ipynb``` and initialize the variables(3rd cell) before running the code
4)  At the beginning and end of each section(tasks), csv files are read and written respectively. So, if you want to run the code for a particular section(task), csv files can be read at the beginning of each section(which have already been stored in 'data' directory in the repo).


### Notes

For HuggingFace, below multilingual model was used for inference-

``` https://huggingface.co/Helsinki-NLP/opus-mt-mul-en ```


### Results


|Language|	IndicTrans_BLEU	|IndicTrans_CHRF	|HuggingFace_BLEU	|HuggingFace_CHRF|
|:-----------:	|:-----------:|	:-----------:|	:-----------:|	:-----------:|
|Hindi|	37.463862	|63.229363	|32.188361	|51.317558|
|Gujarati	|40.203362|	63.827258	|29.886013	|49.51054|
|Marathi	|35.249601	|63.240492	|26.971916	|46.786138|
|Kannada	|36.995699|	60.285479|	25.299824	|44.039135|
|Malayalam	|38.027959	|62.791203	|22.680365	|46.989573|
|Tamil|	36.375305|	60.167382	|25.387703|	44.418505|
|Telugu	|42.21072|	66.698036	|31.473089	|50.86901|
|Bengali	|42.447655|	67.41484|	27.451132	|48.254301|
|Assamese	|39.329497	|61.974933	|29.393651	|49.319043|
|Punjabi	|37.040062|	64.860026|	28.643374	|49.691875|
|Odia	|39.994758|	63.046099	|27.741221	|46.78206|


