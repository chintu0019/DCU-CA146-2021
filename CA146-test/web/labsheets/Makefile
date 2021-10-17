
ascii = $(wildcard *.ascii)
slidy = $(wildcard *.slidy)
html = $(patsubst %.ascii, %.html, $(ascii)) $(patsubst %.slidy, %.html, $(slidy))

build: $(html)
	@true

%.html: %.ascii
	asciidoc-wrapper $<

%.html: %.slidy
	slidy-wrapper $<

watch:
	watch -n 1 $(MAKE) -s

clean:
	-rm -v *.html

.PHONY: build clean watch
