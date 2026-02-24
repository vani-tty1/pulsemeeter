srpm:
	dnf install -y git rpm-build
	$(eval VERSION := $(shell awk '/^Version:/ {print $$2}' *.spec))
	git archive --format=tar.gz --prefix=pulsemeeter-$(VERSION)/ -o pulsemeeter-$(VERSION).tar.gz HEAD
	rpmbuild -bs --define "_sourcedir ." --define "_srcrpmdir $(outdir)" *.spec