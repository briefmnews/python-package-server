bump:
	git pull origin master
	python bump.py $(app) $(version)
	git add -p
	git commit -m "$(shell cat commit_message.txt)"
	git push origin master
	rm commit_message.txt

