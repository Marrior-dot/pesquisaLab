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
