# *Raspberry* 3/4 *OpenCv* v4

## TCC II - Guilherme Afonso Elífas Gibosky
Tutorial de Instalação e Codigo dos scripts

Requerimentos:

Esse tutorial assume que a plataforma usada é o Raspian e que o pacote de gerenciamento é o apt e pip (Python).
Para alguns passos é necessário usar um editor de texto.

## Instalação Rápida - Usando PIP

###### Tempo Médio: 10 min

É possível instalar o *OpenCv* usando o pip, porém esse metodo pode dar errado e mesmo a instalação concluida com sucesso alguns algoritmos podem apresentar problemas ou inconsistências. A instação por esse metodo é por conta do usuário. 

Para aumentar as chances de sucesso, garanta que o pip está instalado e **está atualizado com a versão mais recente**.

```
sudo apt-get update
sudo apt-get install libhdf5-dev libhdf5-serial-dev
sudo apt-get install libqtwebkit4 libqt4-test
sudo pip install opencv-contrib-python​
```

Se tudo correr bem é necessário instalar o *libopecv*, através do comando abaixo:

`sudo apt-get install libopencv-dev python-opencv`

Para checar se tudo foi instalado corretamente, basta digitar python no terminal e em seguida digitar import cv2 e a tecla enter.
Se interpretador pular de linha e não acusar erro a instalação foi feita com sucesso.


## Instalação Demorada - Usando MAKE

###### Tempo Médio: 5 horas

Em muitas situações (naturalmente no meu caso) apenas esse metodo apresenta resultados adequados. Esse metodo vai compilar do **source** todas as ferramentas necessárias 

