

- "ls -alsh" :  montre les fichiers avec les dates crées
- "chmod +x" : to give access for reading and writing something like that
- "bash file.sh" :  need to be used to work sh files
- 1- Créer un script `sum.sh` qui prend 2 variables a(=20) et b(=30) et affiche une varibale  sum=a+b
	#!/bin/bash	
	-> nano sum.sh
	-> in nano : sum=$(($1+$2)) , echo "Sum=$sum"
	-> sh sum.sh 20 30
 
- 2- Créer un script `nameUser.sh ` qui afficher le nom de l'utilisateur ainsi que la date du jour. Le script devra demander le nom à l'utilisateur et qui l'écrit dans la console
	#!/bin/bash	
	-> read -p "Enter ur name: " str1
	-> date1=$(date)
	-> echo "name user = $str1 , date = $date1"

- 3- Créer un script `compt.sh ` qui affiche une variable count (compteur) qui s'incrémente et s'arrète au chiffre 5 ?
	#!/bin/bash
	->i=1
	->while [ $i -le 5 ]
	->do
    	->echo $i
    	->i=$(($i+1))
	->done

- 4- Créer un script `for.sh` qui affiche les chiffre de 10 à 1 sur une ligne à l'aide d'une boucle for ?
	#!/bin/bash
	for ((i=10;i>=1;i--))
	do
	    echo $i
	done
	echo ""


- 5- Créer un script `if.sh` qui demande un nombre à l'utilisateur et indique si c'est un nombre à 1, 2 ou 3 chiffres 
	#!/bin/bash
	echo "Enter Num"
	read num
	if [[ $num -lt 0 ]]
	then
	    echo "Veuillez mettre un nombre positif"
	elif [ $num -gt 0 ] && [ $num -lt 10 ]
	then
	    echo "One number Composition"
	elif [ $num -gt 9 ] && [ $num -lt 100 ]
	then
	    echo "two number composition"
	else
	    echo "three number composition"
	fi

- 6- Créer un script `cmd.sh` qui demande deux arguments (X et Y)  à l'utilisateur, qui les lis et affiche la somme dans l'interface de commande 
	
	#!/bin/bash
	echo "Put X: "
	read x
	echo "Put Y: "
	read y

	sum=$(($x+$y))
	echo "Sume=$sum"
	
	#!/bin/bash
	for arg in "$@" // $@ veut dire tous les arguments aprés file.sh
	do
	index=$(echo $arg | cut -f1 -d=)
	val=$(echo $arg | cut -f2 -d=)
	case $index in
	X) x=$val;;
	Y) y=$val;;
	*)
	esac
	done
	((result=x+y))
	echo "X+Y=$result"

- 7- Créer un dossier test et un script `dir.sh` qui affiche les dossiers dans le repertoire
	for f in test/*
	do
	    echo $(basename $f)
	done	 
	
	benjamin correction :
	
	#!/bin/bash
	for dirname in $(ls -d */) # -d c'est filtrer les directories
	do
	echo "$dirname"
	done
- 8- Créer un nouveau fichier txt (non vide) et créer un script `lines.sh` qui itère dans votre répertoire et affiche seulement les fichiers et compte le nombre de lignes et de mots de chacun des fichiers. Afficher seulement les fichier non vides

	for F in $(ls)
	do
	    if [[ -f $F ]]
	    then
		    if [[ -s $F ]]
		    then
			echo "FICHIER : $F"
			echo "LIGNE :  $(wc -l < $F)"
			echo "MOT : $(wc -w < $F)"
			echo ""
		    fi
	    fi
	done



to check file lignes and words 'lines2.sh' : 

#!/bin/sh

echo "Enter filename"
read fname

if [ ! -f "$fname" ]; then
    echo "No such file!" >&2
    exit 1
fi

lines=$( wc -l <"$fname" )
words=$( wc -w <"$fname" )
chars=$( wc -c <"$fname" )

printf 'The file "%s" has %d lines, %d words and %d characters\n' \
    "$fname" "$lines" "$words" "$chars"


- Se renseigner sur le fichier `.bashrc` sur votre VM, éditez le avec un alias (si vous ne savez pas ce que c'est renseignez vous sur les alias)

	- What is an alias ? it s a shortucut creator 

	vim ~/.bashrc
	or joe ~/.bashrc_aliases
	to save : ctrl+K+X

	And then source ~/.bashrc_aliases

	- Instructions :  esc -> ':wq' ou ':x'
 
- Faite un alias sur votre machine pour accéder à votre VM 

	vim ~/.bashrc
	or joe ~/.bashrc_aliases
	to save : ctrl+K+X
	what i editied : VM-mohamed='ssh 34.66.84.89'
	And then source ~/.bashrc_aliases

- Faire une fonction `gitacp()` qui prend en entrée un message de plusieurs mots sous forme de string et qui effectue un push sur un repo git avec les commandes usuelles de git (add, commit et push)

	vim ~/.bashrc : pour éditer : esc -> i to insert -> esc -> :x (pour sauvegarder)


- Petit cadeau, pour retirer les .o, les ~ et # si vous en avez
	#!/bin/sh
	find -type f \( -name "*~" -o -name "#*#" -o  -name "*.o" \) -delete

- pour créer un alias via script rapidement avec le script dans le même répo

	alias [NOM COMMANDE]='bash ./[SCRIPT]'

- Sinon via un répo distance 

	alias [NOM COMMANDE]='bash ~/[REPO DISTANT]/[SCRIPT]'

installing parameters in vim :

- pip3 install all the shit
- python auto install
