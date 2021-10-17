
ascii = $(wildcard *.ascii)
slidy = $(wildcard *.slidy)
html = $(patsubst %.ascii, %.html, $(ascii)) $(patsubst %.slidy, %.html, $(slidy))

build: $(html)
	@true

%.html: %.ascii
	asciidoc-wrapper $<

%.html: %.slidy
	slidy-wrapper $<

install:
	$(MAKE) $(html)
	$(MAKE) -C .. install

watch:
	watch -n 1 $(MAKE) install

clean:
	-rm -v *.html
	$(MAKE) build

.PHONY: build clean watch install
