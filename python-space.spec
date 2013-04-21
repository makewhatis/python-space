%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:		python-space	
Version:	0.0.1
Release:	1%{?dist}
Summary:	Space is a command line interface for Spacewalk

Group:		Applications/Engineering
License:	BSD License
URL:		http://space.readthedocs.org/
Source0:	python-space-%{version}.tar.gz

BuildRequires:	python
BuildRequires:  python-setuptools
BuildRequires:  python-prettytable

%if 0%{?rhel} < 7
BuildRequires:  python-argparse
%endif

%description
Space is a command line interface, and python wrapper, which gives access to the Spacewalk/RHN api via python and the CLI.

%prep
%setup -q


%build
%{__python} setup.py build 

%install
%{__python} setup.py install \
        --skip-build \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{python_sitelib}/*
%attr(755,root,root) %{_bindir}/space


%changelog
* Sat Apr 20 2013 David Johansen <david@makewhatis.com> - 0.0.1-1
- Refactoring spec file
