Name:       server99-repositories
Version:    37
Release:    1%{?dist}
Summary:    Repository files for server99

License:    GPL
URL:        https://github.com/Server99-industries/server99-repositories
Source0:    https://github.com/Server99-industries/server99-repositories/archive/refs/heads/main.tar.gz#/server99-repositories-main.tar.gz

BuildArch:  noarch

# For /etc/yum.repos.d
Requires: fedora-repos

%description
Repository files for server99

%prep
%autosetup -n server99-repositories-main

# Place server99.repo in /etc/yum.repos.d
%build
%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
cp server99.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%files
%{_sysconfdir}/yum.repos.d/server99.repo

%changelog
* Mon Aug 28 2023 Core-i99
- Package created
