SOURCES=index.html.tmpl

PYTHON=python

all: index.html sync

index.html: $(SOURCES) marriage.yaml
	$(PYTHON) tools/build.py marriage.yaml $(SOURCES) $@

sync:
	s3cmd sync . s3://myjywedding --exclude=* --exclude=env --include=images/* --include=index.html --rr --acl-public --config s3cfg

clean:
	rm -f index.html

.PHONY: all clean
