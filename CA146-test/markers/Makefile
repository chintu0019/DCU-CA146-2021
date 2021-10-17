
# This assumes that the CWD is something like "/home/blott/ca116/markers", so
# we can pick the current module out of the path.
#
module = $(notdir $(realpath ..))

install:
	# @# Do not run this target on einstein!
	# test $$( hostname ) != "einstein"
	rsync --itemize-changes -a --delete --prune-empty-dirs ./ einstein.computing.dcu.ie:markers/$(module)

watch:
	watch -n 1 $(MAKE) install

.PHONY: install watch
