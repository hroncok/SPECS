SPECS
=====

Spec files for my Fedora packages

Fedora repo
-----------

Can be found here: http://repo.hroncok.cz/reprap/reprap.repo

I want my packages in Fedora
----------------------------

skeinforge: https://bugzilla.redhat.com/show_bug.cgi?id=863793

printrun: https://bugzilla.redhat.com/show_bug.cgi?id=863796

opencsg: https://bugzilla.redhat.com/show_bug.cgi?id=825489 (not mine, but needed)

openscad: https://bugzilla.redhat.com/show_bug.cgi?id=864187

Legal problems
--------------

### perl-Math-Geometry-Voronoi

**Problem:** The perl module is OK, but the C code in it is unlicensed, author is asked.

**TODO:** Wait for 1st author of the C code and see, if he agrees. Ask second author.

**Involved packages:** _self_, slic3r

### perl-Math-Libm

**Problem:** The perl module is unlicensed, but it is autogenerated from LGPL code from glibc using h2xs. The author is dead or similar.

**Didn't work:** I've tried to repeat author's steps, but it doeesn't work. I even tried to use glibc from 2000. I might also try h2xs from 2000 (already downloaded Red Hat Linux 7), but it seem there are some modifications of the code made by the author of Math::Libm.

**TODO:** Shoot myself to the head.

**Involved packages:** _self_, perl-Math-NumSeq, perl-Math-PlanePath, sli3r
