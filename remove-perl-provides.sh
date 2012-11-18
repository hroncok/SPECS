#!/bin/bash
for DEP in `rpm -q --provides perl | cut -d= -f1`; do
	sed -i "s/BuildRequires:  $DEP//" perl-*.spec slic3r.spec
	# TODO remove whitespace
done

if [ "$1" == "--bumpspec" ]; then
	rpmdev-bumpspec -c "Removed BRs provided by perl package" perl-*.spec slic3r.spec
fi
