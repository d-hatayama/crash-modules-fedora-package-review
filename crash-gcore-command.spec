%global reponame crash-gcore

Summary: Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.6.2
Release: 0%{?dist}
License: GPLv2
Source0: https://github.com/fujitsu/crash-gcore/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-gcore
ExclusiveOS: Linux
ExclusiveArch: x86_64 aarch64
BuildRequires: crash-devel >= 5.1.5
Requires: crash >= 5.1.5

%description
Command for creating a core dump file of a user-space task that was
running in a kernel dump file.

%prep
%autosetup -n %{reponame}-%{version}

%build
make -C src -f gcore.mk

%install
mkdir -p %{buildroot}%{_libdir}/crash/extensions/
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions/ %{_builddir}/%{reponame}-%{version}/src/gcore.so

%files
%defattr(-,root,root)
%{_libdir}/crash/extensions/gcore.so
%doc COPYING

%changelog
* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.2-0
- Initial crash-gcore-command package
