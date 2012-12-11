%define pkgname kaa-imlib2

Summary: Set of python modules related to media
Name: python-%{pkgname}
Version: 0.2.3
Release: %mkrel 7
Source0: http://mesh.dl.sourceforge.net/sourceforge/freevo/%{pkgname}-%{version}.tar.gz
License: LGPL
URL: http://sourceforge.net/projects/freevo/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	python-devel
BuildRequires:	python-kaa-base
BuildRequires:	imlib2-devel
BuildRequires:	libpng-devel
BuildRequires:	freetype2-devel
Requires:	python-kaa-base
Requires:	imlib2

%description
Imlib2 wrapper for python.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%dir %py_platsitedir/kaa/imlib2
%py_platsitedir/kaa/imlib2/*
%py_platsitedir/kaa_imlib2-%{version}-*.egg-info


%changelog
* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.2.3-7mdv2011.0
+ Revision: 591979
- Rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2.3-6mdv2010.0
+ Revision: 442206
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-5mdv2009.0
+ Revision: 259652
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-4mdv2009.0
+ Revision: 247495
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-2mdv2008.1
+ Revision: 171062
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Wed Feb 06 2008 Crispin Boylan <crisb@mandriva.org> 0.2.3-1mdv2008.1
+ Revision: 163255
- New release

* Fri Dec 28 2007 Crispin Boylan <crisb@mandriva.org> 0.2.2-1mdv2008.1
+ Revision: 138784
- New release
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Crispin Boylan <crisb@mandriva.org> 0.2.1-1mdv2008.0
+ Revision: 17241
- New release, drop patch 1 (merged upstream)

* Tue Apr 17 2007 Crispin Boylan <crisb@mandriva.org> 0.2.0-3mdv2007.1
+ Revision: 13667
- Rediff patch1, add missing pieces


* Fri Apr 06 2007 Crispin Boylan <crisb@mandriva.org> 0.2.0-2mdv2007.1
+ Revision: 150882
- Bump release
- Add patch1 to fix python2.5 and x86_64 problems (#28259)

* Tue Mar 13 2007 Crispin Boylan <crisb@mandriva.org> 0.2.0-1mdv2007.1
+ Revision: 143104
- BuildRequires png and freetype devel
- BuildRequires python-devel
- Initial Mandriva package
- Create python-kaa-imlib2

