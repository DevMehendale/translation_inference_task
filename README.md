# translation_inference_task
### Web scraper + Translation inference comparison of two models(IndicTrans and HuggingFace)


Steps to run the code-
1)	Clone the github repo-

    ```git clone https://github.com/DevMehendale/translation_inference_task.git```
3)	Primary code is in the ```inference.py``` file and some user-defined functions are in ```web_scraper_func.py``` module which has already been imported in ```inference.py```
4)	Open ```inference.ipynb``` and initialize the variables(3rd cell) before running the code



Language	IndicTrans_BLEU	IndicTrans_CHRF	HuggingFace_BLEU	HuggingFace_CHRF
0	Hindi	37.463862	63.229363	32.188361	51.317558
1	Gujarati	40.203362	63.827258	29.886013	49.510540
2	Marathi	35.249601	63.240492	26.971916	46.786138
3	Kannada	36.995699	60.285479	25.299824	44.039135
4	Malayalam	38.027959	62.791203	22.680365	46.989573
5	Tamil	36.375305	60.167382	25.387703	44.418505
6	Telugu	42.210720	66.698036	31.473089	50.869010
7	Bengali	42.447655	67.414840	27.451132	48.254301
8	Assamese	39.329497	61.974933	29.393651	49.319043
9	Punjabi	37.040062	64.860026	28.643374	49.691875
10	Odia	39.994758	63.046099	27.741221	46.782060
