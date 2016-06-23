function g
	cd
	cd Python-scripts
	git add --all
	git commit -m "Bedapudi Praneeth"
	git push
end

function e
	exit
end

function e2
	cd
	cd ES
	cd 2.3.3
	cd bin
	./elasticsearch
end

function e1
	cd
	cd ES
	cd 1.7.3
	cd bin
	./elasticsearch
end

function e2.2
	cd
	cd ES
	cd 2.2.0
	cd bin
	./elasticsearch
end

function cs
   cd $argv
   ls
end
function v
   bash|vnstat -i wlan0 -d
end

alias gg='googler -n 4 -c in'
alias gj='googler -n 4 -c in -j'