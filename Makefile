bump:
	git pull origin master
	python bump.py $(app) $(version)
	make commit

commit:
	git add -p
	git commit -m "$(shell cat commit_message.txt)"
	git push origin master
	rm commit_message.txt

make install:
	pip install -r requirements.txt