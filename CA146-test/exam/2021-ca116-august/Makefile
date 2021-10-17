
module = ca116

asciis = $(wildcard *.ascii)
html = $(asciis:.ascii=.html)

path = $(shell realpath .)
name = $(shell basename $(path))

build: $(html)
	@true

watch:
	watch -n 1 $(MAKE) build

install:
	$(MAKE) web
	rsync -av --delete ./ einstein:web/$(module)/$(name)

web:
	make -C ../../web install

clean:
	$(MAKE) web

%.html: %.ascii
	asciidoc-wrapper $<
	cp -v dcu-logo.png ~/downloads/

.PHONY: build watch install clean web
