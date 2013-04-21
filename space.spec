%define __os_install_post %{nil}

Name:		space	
Version:	0.0.2
Release:	2%{?dist}
Summary:	Space is a command line interface for Spacewalk

Group:		Applications/Engineering
License:	BSD License
URL:		http://space.readthedocs.org/
Source0:	space-%{version}.tar.gz
Source1:        config.ini.sample

%if 0%{?rhel} < 7
BuildRequires:  python-argparse
%endif

%description
Space is a command line interface, and python wrapper, which gives access to the Spacewalk/RHN api via python and the CLI.

This is the frozen version, that works without any python dependency.

%prep
%setup -q

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/space
%{__cp} %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/space/config.ini
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sharedstatedir}/space
%{__cp} -R $RPM_BUILD_DIR/space-%{version}/* $RPM_BUILD_ROOT%{_sharedstatedir}/space/
ln -s /var/lib/space/space $RPM_BUILD_ROOT%{_bindir}/space

%post
chmod 0755 /var/lib/space/space

%files
%defattr(644,root,root,755)
/etc/space/config.ini
%{_sharedstatedir}/space/*
%attr(755,root,root) %{_bindir}/space


%changelog
* Sat Apr 20 2013 David Johansen <david@makewhatis.com> - 0.0.1-1
- Refactoring spec file
