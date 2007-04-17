%define pkgname kaa-imlib2

Summary: The Kaa Media Repository is a set of python modules related to media
Name: python-%{pkgname}
Version: 0.2.0
Release: %mkrel 3
Source0: http://mesh.dl.sourceforge.net/sourceforge/freevo/%{pkgname}-%{version}.tar.bz2
Patch1:	kaa-imlib2-python2.5x86_64.patch.bz2
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
%patch1 -p0

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


