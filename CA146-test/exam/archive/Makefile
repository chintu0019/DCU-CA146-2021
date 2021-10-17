
asciis = $(wildcard *.ascii)
htmls = $(asciis:.ascii=.html)

build: $(htmls)
	@rsync ./dcu-logo.png ~/downloads/
	@true

watch:
	watch -n 1 $(MAKE) build

%.html: %.ascii
	asciidoc-wrapper $<

exam = 2020-ca116-resit-ca.html
exam = placeholder.html

install:
	scp $(exam) einstein:web/ca116/exam.html

# key = Ro5Iaxee
#
# # https://ca116.computing.dcu.ie/Ro5Iaxee/wrapper.html
# install:
# 	pmake -C /home/smblott/old-teaching/ca116/web
# 	rsync -av --delete ./ einstein:web/ca116/$(key)/

.PHONY: build watch install
