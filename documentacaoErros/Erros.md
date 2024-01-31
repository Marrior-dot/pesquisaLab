*  **CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0)**
	* <u>Causa:</u> não entendi ao certo
	* <u>Solução:</u> pip3 uninstall twint && pip3 install twint && pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
* **Terminal não abrindo, usando ctrl+alt+t ou utilizando o icone no menu**
	 * <u>Causa:</u> direcionar o symlink de python3 para outro PATH que não seja usr/bin/python3.8.
	 * <u>Solução:</u> redirecionar o symlink da seguinte forma.
		 * sudo update-alternatives usr/bin/python3 usr/bin/python3.8 1
		 * sudo update-alternatives usr/bin/python3 usr/bin/python3.10 2
		 * sudo update-alternatives --config python
		 * escolher a opção 1 para voltar tudo ao normal

* **Icone de configurações não aparece disponível**
	* <u>Causa:</u> Desconhecida*
	* <u>Solução:</u> sudo apt-get install --reinstall gnome-control-center

* **sklearn depreciado**
	* **Path**: no <u>fork</u> do projeto NLPyPort: ./setup.py
	* **Causa**:arquivo setup.py no projeot NLPyPort possui os seguintes requirementos
		______________________________________________________________________
		setup.py(13-30)
		  install_requires=[            # I get to this in a second
         "nltk",
		"numpy",
		"pandas",
		"python-crfsuite",
		"python-dateutil",
		"pytz",
		"scikit-learn",
		"scipy",
		"singledispatch",
		"six",
		"sklearn",
		"sklearn-crfsuite",
		"tabulate",
		"tqdm",
		"xmltodict",
      ],
    * **Solução:** Comentar (#) as dependências com nome "sklearn"
	      install_requires=[            # I get to this in a second
         "nltk",
		"numpy",
		"pandas",
		"python-crfsuite",
		"python-dateutil",
		"pytz",
		"scikit-learn",
		"scipy",
		"singledispatch",
		"six",
		#"sklearn",
		#"sklearn-crfsuite",
		"tabulate",
		"tqdm",
		"xmltodict",

      ],

* **Text() não foi definido**
	* **Causa:** Indefinida, arquivo Fullpipeline.py chama a classe Text, porém não importa do seu arquivo
		* **Path** /usr/local/lib/python3.10/dist-packages/NLPyPort/FullPipeline.py
	* **Solução:** Colar classe Text do arquivo <u>text.py</u> em Fullpipeline.py
		* **Path**: /usr/local/lib/python3.10/dist-packages/NLPyPort/text.py
		text.py:
		class Text:
			def __init__(self):
				self.tokens = []
				self.pos_tags = []
				self.lemas = []
				self.entities = []
				self.np_tags = []
		
			def set_tokens(self,tokens):
				self.tokens = tokens
		
		
			def set_pos_tags(self,pos_tags):
				self.pos_tags = pos_tags
				for index,elem in enumerate(self.tokens):
					if(elem=="\n"):
						self.pos_tags[index] = ""
					if(elem=="EOS"):
						self.pos_tags[index] = "EOS"
		
			def set_lemas(self,lemas):
				self.lemas = lemas
				for index,elem in enumerate(self.tokens):
					if(elem=="\n"):
						self.lemas[index] = ""
					if(elem=="EOS"):
						self.lemas[index] = "EOS"
		
			def set_entities(self,entities):
				self.entities = entities
				for index,elem in enumerate(self.tokens):
					if(elem=="\n"):
						self.entities[index] = ""
					if(elem=="EOS"):
						self.entities[index] = "EOS"
		
			def set_np_tags(self,np_tags):
				self.np_tags = np_tags
				for index,elem in enumerate(self.tokens):
					if(elem=="\n"):
						self.np_tags[index] = ""
					if(elem=="EOS"):
						self.np_tags[index] = "EOS"
		
			def print_text_order(self,lista):
				for elem in lista:
					print(elem)
		
			def print_conll(self):
				current_line = ""
				for index in range(len(self.tokens)):
					if(self.tokens!=[]):
						current_line += self.tokens[index]
					if(self.pos_tags!=[]):
						current_line += " " + self.pos_tags[index]
					if(self.lemas!=[]):
						current_line += " " + self.lemas[index]
					if(self.entities!=[]):
						current_line += " " + self.entities[index]
					if(self.np_tags!=[]):
						current_line += " " + self.np_tags[index]
					print(current_line)
					current_line=""

*  **No such file or directory: 'global.properties'***( a Documentar)